#!/usr/bin/env python3
"""
Mermaid 코드 블록을 코드 예제 + 실제 차트 형식으로 변환하는 스크립트
중복된 코드 블록 제거 기능 포함
"""

import re
import os
from typing import List, Tuple, Optional


class MermaidBlock:
    """Mermaid 코드 블록을 나타내는 클래스"""
    
    def __init__(self, content: List[str], start_line: int, end_line: int):
        self.content = content
        self.start_line = start_line
        self.end_line = end_line
        self.hash = hash('\n'.join(content))
    
    def to_code_example(self) -> List[str]:
        """코드 예제 블록으로 변환"""
        return ['````'] + self.content + ['````']
    
    def to_render_block(self) -> List[str]:
        """렌더링 블록으로 반환"""
        return self.content.copy()


def extract_mermaid_block(lines: List[str], start_idx: int) -> Optional[MermaidBlock]:
    """지정된 위치에서 mermaid 블록을 추출"""
    if start_idx >= len(lines) or not lines[start_idx].strip() == '```mermaid':
        return None
    
    content = [lines[start_idx]]
    i = start_idx + 1
    
    # mermaid 내용 수집
    while i < len(lines) and lines[i].strip() != '```':
        content.append(lines[i])
        i += 1
    
    # 닫는 ``` 추가
    if i < len(lines):
        content.append(lines[i])
        return MermaidBlock(content, start_idx, i)
    
    return None


def skip_code_example_block(lines: List[str], start_idx: int) -> int:
    """코드 예제 블록(````로 감싼 블록)을 건너뜀"""
    if (start_idx >= len(lines) or 
        lines[start_idx].strip() != '````' or
        start_idx + 1 >= len(lines) or
        lines[start_idx + 1].strip() != '```mermaid'):
        return start_idx
    
    i = start_idx + 1  # ```mermaid로 이동
    
    # mermaid 블록 내용 건너뛰기
    while i < len(lines) and lines[i].strip() != '```':
        i += 1
    i += 1  # 닫는 ``` 건너뛰기
    
    # 닫는 ````
    if i < len(lines) and lines[i].strip() == '````':
        i += 1
    
    return i


def skip_empty_lines(lines: List[str], start_idx: int) -> int:
    """빈 줄들을 건너뜀"""
    i = start_idx
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    return i


def process_mermaid_content(content: str) -> str:
    """Mermaid 내용을 처리하여 최적화된 형태로 변환"""
    lines = content.split('\n')
    result_lines = []
    processed_blocks = set()  # 처리된 블록의 해시를 저장
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # 단순한 ```mermaid 블록 처리
        if line.strip() == '```mermaid':
            block = extract_mermaid_block(lines, i)
            if block and block.hash not in processed_blocks:
                # 코드 예제와 렌더링 블록 추가
                result_lines.extend(block.to_code_example())
                result_lines.append('')
                result_lines.extend(block.to_render_block())
                processed_blocks.add(block.hash)
                i = block.end_line + 1
                continue
        
        # 기존 코드 예제 블록 처리 (````로 감싸진 것)
        elif line.strip() == '````':
            if (i + 1 < len(lines) and 
                lines[i + 1].strip() == '```mermaid'):
                
                # 이미 올바른 형태이므로 그대로 복사하고 중복 제거
                block = extract_mermaid_block(lines, i + 1)
                if block:
                    # 코드 예제 블록 복사
                    result_lines.append(line)  # ````
                    result_lines.extend(block.content)
                    
                    # 닫는 ````
                    next_idx = block.end_line + 1
                    if next_idx < len(lines) and lines[next_idx].strip() == '````':
                        result_lines.append(lines[next_idx])
                        next_idx += 1
                    else:
                        result_lines.append('````')
                    
                    result_lines.append('')
                    
                    # 다음 중복 블록들 건너뛰기
                    next_idx = skip_empty_lines(lines, next_idx)
                    
                    # 중복된 코드 예제 블록들 건너뛰기
                    while (next_idx < len(lines) and
                           lines[next_idx].strip() == '````'):
                        next_idx = skip_code_example_block(lines, next_idx)
                        next_idx = skip_empty_lines(lines, next_idx)
                    
                    # 중복된 렌더링 블록들 건너뛰기
                    while (next_idx < len(lines) and
                           lines[next_idx].strip() == '```mermaid'):
                        duplicate_block = extract_mermaid_block(lines, next_idx)
                        if duplicate_block and duplicate_block.hash == block.hash:
                            next_idx = duplicate_block.end_line + 1
                            next_idx = skip_empty_lines(lines, next_idx)
                        else:
                            break
                    
                    # 하나의 렌더링 블록만 추가 (중복이 아닌 경우에만)
                    if block.hash not in processed_blocks:
                        result_lines.extend(block.to_render_block())
                        processed_blocks.add(block.hash)
                    
                    i = next_idx - 1  # 다음 루프에서 +1이 될 것을 고려
                else:
                    result_lines.append(line)
            else:
                result_lines.append(line)
        else:
            result_lines.append(line)
        
        i += 1
    
    return '\n'.join(result_lines)


def process_file(file_path: str) -> None:
    """파일을 읽고 변환하여 저장"""
    print(f"Processing file: {file_path}")
    
    try:
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 변환 처리
        print("Processing mermaid blocks...")
        processed_content = process_mermaid_content(content)
        
        # 통계 계산
        original_blocks = len(re.findall(r'```mermaid', content))
        processed_blocks = len(re.findall(r'```mermaid', processed_content))
        
        # 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print("Processing completed!")
        print(f"   - Original mermaid blocks: {original_blocks}")
        print(f"   - Processed mermaid blocks: {processed_blocks}")
        print(f"   - Added blocks: {processed_blocks - original_blocks}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        raise


def main():
    """메인 함수"""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python fix_mermaid.py <file_path>")
        print("Example: python fix_mermaid.py src/93_mermaid/mindmap.md")
        return 1
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return 1
    
    try:
        process_file(file_path)
        print("All done!")
        return 0
    except Exception as e:
        print(f"Failed to process file: {e}")
        return 1


if __name__ == "__main__":
    exit(main())