# 마크다운

mdBook의 [파서](https://github.com/raphlinus/pulldown-cmark)는 아래에 설명된 몇 가지 확장을 포함한 [CommonMark](https://commonmark.org/) 명세를 따릅니다.
[튜토리얼](https://commonmark.org/help/tutorial/)을 빠르게 살펴보거나,
CommonMark를 실시간으로 [체험해 볼](https://spec.commonmark.org/dingus/) 수 있습니다. 완전한 마크다운 개요는 이 문서의 범위를 벗어나지만, 아래에서는 기본 사항 중 일부에 대한 높은 수준의 개요를 제공합니다. 더 자세한 경험을 원한다면 [마크다운 가이드](https://www.markdownguide.org)를 확인하세요.

## 텍스트와 단락

텍스트는 비교적 예측 가능하게 렌더링됩니다: 

```markdown
여기는 텍스트 한 줄입니다.

이것은 새 줄입니다.
```

예상하는 대로 다음과 같이 보일 것입니다:

여기는 텍스트 한 줄입니다.

이것은 새 줄입니다.

## 제목

제목은 `#` 마커를 사용하며 한 줄에 단독으로 있어야 합니다. 더 많은 `#`은 더 작은 제목을 의미합니다:

```markdown
### 제목 

어떤 텍스트.

#### 더 작은 제목 

더 많은 텍스트.
```

### 제목 

어떤 텍스트.

#### 더 작은 제목 

더 많은 텍스트.

## 목록

목록은 순서가 없거나 순서가 있을 수 있습니다. 순서가 있는 목록은 자동으로 순서가 매겨집니다:

```markdown
* 우유
* 달걀
* 버터

1. 당근
1. 셀러리
1. 무
```

* 우유
* 달걀
* 버터

1. 당근
1. 셀러리
1. 무

## 링크

URL이나 로컬 파일에 링크하는 것은 쉬습니다:

```markdown
[mdBook](https://github.com/rust-lang/mdBook)을 사용하세요. 

[mdBook](mdbook.md)에 대해 읽어보세요.

위와 달리 인라인이 아닌 [mdBook 링크] 입니다.

남겨진 URL: <https://www.rust-lang.org>.

[mdBook 링크]: https://github.com/rust-lang/mdBook
```

[mdBook](https://github.com/rust-lang/mdBook)을 사용하세요. 

[mdBook](mdbook.md)에 대해 읽어보세요.

위와 달리 인라인이 아닌 [mdBook 링크] 입니다.

남겨진 URL: <https://www.rust-lang.org>.

[mdBook 링크]: https://github.com/rust-lang/mdBook
----

`.md`로 끝나는 상대 링크는 `.html` 확장자로 변환됩니다.
가능하면 `.md` 링크를 사용하는 것이 권장됩니다.
이는 마크다운을 자동으로 렌더링하는 GitHub나 GitLab과 같이 mdBook 외부에서 마크다운 파일을 볼 때 유용합니다.

`README.md`로의 링크는 `index.html`로 변환됩니다.
이는 GitHub과 같은 일부 서비스는 README 파일을 자동으로 렌더링하지만, 웹 서버는 일반적으로 루트 파일이 `index.html`로 불리기를 기대하기 때문입니다.

`#` 프래그먼트를 사용하여 개별 제목에 링크할 수 있습니다.
예를 들어, `mdbook.md#text-and-paragraphs`는 위의 [텍스트와 단락](#text-and-paragraphs) 섹션에 링크됩니다.
ID는 소문자로 변환하고 공백을 대시로 바꾸는 등 제목을 변환하여 생성됩니다.
어떤 제목이든 클릭하고 브라우저의 URL을 보면 프래그먼트가 어떻게 생겼는지 확인할 수 있습니다.

## 이미지

이미지를 포함하는 것은 단순히 위의 _링크_ 섹션과 같이 이미지에 링크를 포함하는 문제입니다. 다음 마크다운은
이 파일과 같은 레벨의 `images` 디렉토리에 있는 Rust 로고 SVG 이미지를 포함합니다:

```markdown
![Rust 로고](images/rust-logo-blk.svg)
```

mdBook로 빌드할 때 다음 HTML을 생성합니다:

```html
<p><img src="images/rust-logo-blk.svg" alt="Rust 로고" /></p>
```

물론 다음과 같이 이미지를 표시합니다:

![Rust 로고](images/rust-logo-blk.svg)

## 확장

mdBook은 표준 CommonMark 명세를 넘어서는 여러 확장을 가지고 있습니다.

### 취소선

텍스트 양쪽에 하나 또는 두 개의 물결(달표) 문자로 감싸서 텍스트 중앙에 가로선을 그어 렌더링할 수 있습니다:

```text
~~취소선 텍스트~~의 예시.
```

이 예시는 다음과 같이 렌더링됩니다:

> ~~취소선 텍스트~~의 예시.

이는 [GitHub 취소선 확장][strikethrough]을 따릉니다.

### 각주

각주는 텍스트에 작은 번호가 매겨진 링크를 생성하며, 클릭하면
독자를 항목 하단의 각주 텍스트로 이동시킵니다. 각주
레이블은 앞에 캐럿(^)이 있는 링크 참조와 비슷하게 작성됩니다. 각주
텍스트는 링크 참조 정의처럼 작성되며, 레이블 다음에 텍스트가 옵니다. 예시:

```text
이것은 각주[^note]의 예시입니다.

[^note]: 이 텍스트는 각주의 내용으로, 하단 쪽에 렌더링됩니다.
```

이 예시는 다음과 같이 렌더링됩니다:

> 이것은 각주[^note]의 예시입니다.
>
> [^note]: 이 텍스트는 각주의 내용으로, 하단 쪽에 렌더링됩니다.

각주는 각주가 작성된 순서에 따라 자동으로 번호가 매겨집니다.

### 표

표는 파이프와 대시를 사용하여 표의 행과 열을 그려서 작성할 수 있습니다. 이는 모양에 맞는 HTML 표로 변환됩니다. 예시:

```text
| 헤더1 | 헤더2 |
|-------|-------|
| abc   | def   |
```

이 예시는 다음과 비슷하게 렌더링됩니다:

| 헤더1 | 헤더2 |
|-------|-------|
| abc   | def   |

지원되는 정확한 문법에 대한 자세한 내용은 [GitHub 표 확장][tables] 명세를 참조하세요.

### 작업 목록

작업 목록은 완료된 항목의 체크리스트로 사용할 수 있습니다.
예시:

```md
- [x] 완료된 작업
- [ ] 미완료 작업
```

이는 다음과 같이 렌더링됩니다:

> - [x] 완료된 작업
> - [ ] 미완료 작업

자세한 내용은 [작업 목록 확장] 명세를 참조하세요.

### 스마트 문장 부호

일부 ASCII 문장 부호 시퀀스는 자동으로 고급 유니코드
문자로 변환됩니다:

| ASCII 시퀀스 | 유니코드 |
|-------------|---------|
| `--`        | –       |
| `---`       | —       |
| `...`       | …       |
| `"`         | " 또는 ", 문맥에 따라 |
| `'`         | ' 또는 ', 문맥에 따라 |

따라서 이러한 유니코드 문자를 수동으로 입력할 필요가 없습니다!

이 기능은 기본적으로 활성화되어 있습니다.
비활성화하려면 [`output.html.smart-punctuation`] 설정 옵션을 참조하세요.

[strikethrough]: https://github.github.com/gfm/#strikethrough-extension-
[tables]: https://github.github.com/gfm/#tables-extension-
[task list extension]: https://github.github.com/gfm/#task-list-items-extension-
[`output.html.smart-punctuation`]: configuration/renderers.md#html-renderer-options

### 제목 속성

제목에는 사용자 정의 HTML ID와 클래스를 가질 수 있습니다. 이를 통해 제목의 텍스트를 변경하더라도 동일한 ID를 유지할 수 있으며, 제목에 여러 클래스를 추가할 수도 있습니다.

예시:
```md
# 예시 제목 { #first .class1 .class2 }
```

이는 내용이 `예시 제목`이고, ID가 `first`이며, 클래스가 `class1`과 `class2`인 레벨 1 제목을 만듭니다. 속성은 공백으로 구분되어야 합니다.

자세한 정보는 [제목 속성 명세 페이지](https://github.com/raphlinus/pulldown-cmark/blob/master/pulldown-cmark/specs/heading_attrs.txt)에서 찾을 수 있습니다.
