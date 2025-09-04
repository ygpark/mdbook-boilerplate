#!/usr/bin/env python3
"""
Mermaid 코드 블록을 코드 예제 + 실제 차트 형식으로 변환하는 스크립트
중복된 코드 블록 제거 기능 포함
"""

import re
import os

def clean_duplicate_blocks(content):
    """
    중복된 mermaid 코드 블록을 제거하고 올바른 패턴으로 정리
    """
    lines = content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # ````로 시작하는 코드 예제 블록을 찾음
        if line.strip() == '````':
            # 다음 줄이 ```mermaid인지 확인
            if i + 1 < len(lines) and lines[i + 1].strip() == '```mermaid':
                # 코드 예제 블록 시작
                result_lines.append(line)  # ````
                
                # mermaid 블록 전체를 수집
                mermaid_block_lines = []
                i += 1  # ```mermaid로 이동
                
                # ```mermaid부터 ```까지 수집
                while i < len(lines):
                    mermaid_block_lines.append(lines[i])
                    if lines[i].strip() == '```':
                        break
                    i += 1
                
                # 코드 예제 블록에 추가
                for mermaid_line in mermaid_block_lines:
                    result_lines.append(mermaid_line)
                
                # 닫는 ````
                i += 1
                if i < len(lines) and lines[i].strip() == '````':
                    result_lines.append(lines[i])
                else:
                    result_lines.append('````')
                
                result_lines.append('')  # 빈 줄
                
                # 실제 렌더링용 블록 추가 (중복 체크)
                # 다음에 오는 동일한 mermaid 블록들을 스킵하고 하나만 추가
                next_idx = i + 1
                
                # 빈 줄들 스킵
                while next_idx < len(lines) and lines[next_idx].strip() == '':
                    next_idx += 1
                
                # 중복된 코드 예제 블록들 스킵
                while (next_idx < len(lines) and 
                       lines[next_idx].strip() == '````' and
                       next_idx + 1 < len(lines) and 
                       lines[next_idx + 1].strip() == '```mermaid'):
                    
                    # 이 코드 예제 블록을 스킵
                    next_idx += 1  # ````
                    next_idx += 1  # ```mermaid
                    while next_idx < len(lines) and lines[next_idx].strip() != '```':
                        next_idx += 1
                    next_idx += 1  # ```
                    if next_idx < len(lines) and lines[next_idx].strip() == '````':
                        next_idx += 1  # closing ````
                    # 빈 줄들도 스킵
                    while next_idx < len(lines) and lines[next_idx].strip() == '':
                        next_idx += 1
                
                # 중복된 실제 렌더링 블록들 스킵 (같은 내용인 것들)
                skipped_render_blocks = 0
                while (next_idx < len(lines) and 
                       lines[next_idx].strip() == '```mermaid'):
                    
                    # 이 렌더링 블록의 내용을 확인
                    render_start = next_idx
                    next_idx += 1
                    while next_idx < len(lines) and lines[next_idx].strip() != '```':
                        next_idx += 1
                    next_idx += 1  # closing ```
                    
                    # 내용이 같은지 확인
                    render_content = '\n'.join(lines[render_start:next_idx])
                    original_content = '\n'.join(mermaid_block_lines)
                    
                    if render_content == original_content:
                        skipped_render_blocks += 1
                        # 빈 줄들도 스킵
                        while next_idx < len(lines) and lines[next_idx].strip() == '':
                            next_idx += 1
                    else:
                        break
                
                # 하나의 렌더링 블록만 추가
                for mermaid_line in mermaid_block_lines:
                    result_lines.append(mermaid_line)
                
                # 인덱스를 스킵된 위치로 이동
                i = next_idx - 1  # -1은 다음 루프에서 +1 될 것을 고려
                
            else:
                result_lines.append(line)
        else:
            result_lines.append(line)
        
        i += 1
    
    return '\n'.join(result_lines)

def process_file(file_path):
    """
    파일을 읽고 변환하여 저장
    """
    print(f"Processing file: {file_path}")
    
    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 중복 블록 정리
    print("Cleaning duplicate blocks...")
    cleaned_content = clean_duplicate_blocks(content)
    
    # 정리 결과 확인
    original_mermaid_blocks = len(re.findall(r'```mermaid', content))
    cleaned_mermaid_blocks = len(re.findall(r'```mermaid', cleaned_content))
    
    # 파일 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"Duplicate cleanup completed!")
    print(f"   - Original mermaid blocks: {original_mermaid_blocks}")
    print(f"   - Cleaned mermaid blocks: {cleaned_mermaid_blocks}")
    print(f"   - Removed duplicates: {original_mermaid_blocks - cleaned_mermaid_blocks}")

if __name__ == "__main__":
    file_path = r"C:\Users\ghost\Documents\GitHub\mdbook-boilerplate\src\93_mermaid\flowchart.md"
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit(1)
    
    process_file(file_path)
    print("All done!")