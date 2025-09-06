# 렌더러 설정

렌더러("백엔드"라고도 함)는 책의 출력을 생성하는 역할을 담당합니다.

다음과 같은 백엔드가 내장되어 있습니다:

* [`html`](#html-renderer-options) --- 이는 책을 HTML로 렌더링합니다.
  `book.toml`에 다른 `[output]` 테이블이 정의되지 않았다면 기본적으로 활성화됩니다.
* [`markdown`](#markdown-renderer) --- 이는 전처리기를 실행한 후 책을 마크다운으로 출력합니다.
  전처리기 디버깅에 유용합니다.

커뮤니티에서 여러 백엔드를 개발했습니다.
사용 가능한 백엔드 목록은 [Third Party Plugins] 위키 페이지를 참조하세요.

새 백엔드를 만드는 방법에 대한 정보는 [Backends for Developers] 챕터를 참조하세요.

[Third Party Plugins]: https://github.com/rust-lang/mdBook/wiki/Third-party-plugins
[Backends for Developers]: ../../for_developers/backends.md

## 출력 테이블

백엔드는 백엔드 이름과 함께 `book.toml`에 `output` 테이블을 포함하여 추가할 수 있습니다.
예를 들어, `mdbook-wordcount`라는 백엔드가 있다면 다음과 같이 포함할 수 있습니다:

```toml
[output.wordcount]
```

이 테이블을 사용하면 mdBook이 `mdbook-wordcount` 백엔드를 실행합니다.

이 테이블에는 백엔드에 특정한 추가 키-값 쌍을 포함할 수 있습니다.
예를 들어, 예시 백엔드에 추가 설정 옵션이 필요한 경우:

```toml
[output.wordcount]
ignores = ["예시 챕터"]
```

`[output]` 테이블을 정의한 경우 `html` 백엔드는 기본적으로 활성화되지 않습니다.
`html` 백엔드를 계속 실행하려면 `book.toml` 파일에 포함만 하면 됩니다.
예를 들어:

```toml
[book]
title = "나의 멋진 책"

[output.wordcount]

[output.html]
```

둘 이상의 `output` 테이블이 포함된 경우 출력 디렉토리의 레이아웃 동작이 변경됩니다.
백엔드가 하나만 있다면 `book` 디렉토리에 직접 출력을 배치합니다(이 위치를 오버라이드하려면 [`build.build-dir`] 참조).
백엔드가 둘 이상 있다면 각 백엔드는 `book` 아래의 별도 디렉토리에 배치됩니다.
예를 들어, 위의 예시는 `book/html`과 `book/wordcount` 디렉토리를 가질 것입니다.

[`build.build-dir`]: general.md#build-options

### 사용자 정의 백엔드 명령

기본적으로 `book.toml` 파일에 `[output.foo]` 테이블을 추가하면
`mdbook`은 `mdbook-foo` 실행 파일을 호출하려고 시도합니다.
다른 프로그램 이름을 사용하거나 명령줄 인수를 전달하려면
`command` 필드를 추가하여 이 동작을 오버라이드할 수 있습니다.

```toml
[output.random]
command = "python random.py"
```

### 선택적 백엔드

설치되지 않은 백엔드를 활성화하면 기본 동작은 오류를 발생시키는 것입니다.
백엔드를 선택사항으로 표시하여 이 동작을 변경할 수 있습니다:

```toml
[output.wordcount]
optional = true
```

이는 오류를 경고로 감소시킵니다.


## HTML 렌더러 옵션

HTML 렌더러는 아래에 상세히 설명된 다양한 옵션을 가지고 있습니다.
이러한 옵션들은 `book.toml` 파일의 `[output.html]` 테이블에 지정되어야 합니다.

```toml
# 모든 출력 옵션을 사용한 예시 book.toml 파일.
[book]
title = "예시 책"
authors = ["홍길동", "김철수"]
description = "예시 책은 예시들을 다룹니다."

[output.html]
theme = "my-theme"
default-theme = "light"
preferred-dark-theme = "navy"
smart-punctuation = true
mathjax-support = false
additional-css = ["custom.css", "custom2.css"]
additional-js = ["custom.js"]
no-section-label = false
git-repository-url = "https://github.com/rust-lang/mdBook"
git-repository-icon = "fab-github"
edit-url-template = "https://github.com/rust-lang/mdBook/edit/master/guide/{path}"
site-url = "/example-book/"
cname = "myproject.rs"
input-404 = "not-found.md"
sidebar-header-nav = true
```

다음과 같은 설정 옵션을 사용할 수 있습니다:

- **theme:** mdBook에는 기본 테마와 필요한 모든 리소스 파일이 제공됩니다.
  하지만 이 옵션이 설정되면 mdBook은 지정된 폴더에서 찾은 파일로
  테마 파일을 선택적으로 덮어씁니다.
- **default-theme:** '테마 변경' 드롭다운에서 기본으로 선택할 테마 색상 배치.
  기본값은 `light`입니다.
- **preferred-dark-theme:** 기본 어두운 테마. 브라우저가
  [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
  CSS 미디어 쿼리를 통해 사이트의 다크 버전을 요청하면 이 테마가 사용됩니다.
  기본값은 `navy`입니다.
- **smart-punctuation:** 인용부호를 굴절 인용부호로, `...`을 `…`로, `--`를 en-대시로, `---`를 em-대시로 변환합니다.
  [스마트 문장 부호](../markdown.md#smart-punctuation)를 참조하세요.
  기본값은 `true`입니다.
- **mathjax-support:** [MathJax](../mathjax.md) 지원을 추가합니다. 기본값은
  `false`입니다.
- **additional-css:** 전체 스타일을 덮어쓰지 않고 책의 외모를 약간 변경해야 한다면
  기본 스타일시트 다음에 로드될 스타일시트 집합을 지정하여
  스타일을 수술적으로 변경할 수 있습니다.
- **additional-js:** 현재 동작을 제거하지 않고 책에 일부 동작을 추가해야 한다면
  기본 파일과 함께 로드될 JavaScript 파일 집합을 지정할 수 있습니다.
- **no-section-label:** mdBook은 기본적으로 목차 열에 숫자 섹션 레이블을 추가합니다.
  예를 들어, "1.", "2.1". 이 레이블을 비활성화하려면 이 옵션을 true로 설정하세요.
  기본값은 `false`입니다.
- **git-repository-url:** 책의 git 저장소에 대한 URL. 제공되면
  책의 메뉴 바에 아이콘 링크가 출력됩니다.
- **git-repository-icon:** git 저장소 링크에 사용할 FontAwesome 아이콘 클래스.
  기본값은 `fab-github`이며 <i class="fa fab-github"></i>처럼 보입니다.
  GitHub를 사용하지 않는다면 <i class="fa fa-code-fork"></i>처럼 보이는 `fa-code-fork`를 고려해보세요.
- **edit-url-template:** 편집 URL 템플릿. 제공되면 현재 보고 있는 페이지의 편집으로 직접 이동하는
  "편집 제안" 버튼(<i class="fa fa-edit"></i>처럼 보임)을 보여줍니다. 예를 들어 GitHub 프로젝트는
  `https://github.com/<owner>/<repo>/edit/<branch>/{path}`로 설정하거나
  Bitbucket 프로젝트는
  `https://bitbucket.org/<owner>/<repo>/src/<branch>/{path}?mode=edit`로 설정합니다.
  여기서 {path}는 저장소에서 파일의 전체 경로로 바뀜니다.
- **input-404:** 누락된 파일에 사용되는 마크다운 파일의 이름.
  해당 출력 파일은 확장자가 `html`로 바뀐 동일한 파일이 될 것입니다.
  기본값은 `404.md`입니다.
- **site-url:** 책이 호스팅될 URL. 서브디렉토리의 URL에 액세스할 때에도
  404 파일의 내비게이션 링크와 script/css 임포트가 올바르게 작동하도록 하기 위해 필요합니다.
  기본값은 `/`입니다. `site-url`이 설정된 경우
  자산에 대해 문서 상대 링크를 사용해야 하며, 즉 `/`로 시작하면 안 됩니다.
- **cname:** 책이 호스팅될 DNS 서브도메인 또는 최상위 도메인.
  이 문자열은 GitHub Pages에서 요구하는 대로 사이트 루트에 CNAME이라는 파일로 작성됩니다
  ([*GitHub Pages 사이트를 위한 사용자 정의 도메인 관리*][custom domain] 참조).
- **hash-files:** 정적 자산 파일명에 파일 내용의 암호화 "지문"을 포함시켜
  파일 내용이 변경되면 파일 이름도 따라서 변경되도록 합니다.
  예를 들어, `css/chrome.css`는 `css/chrome-9b8f428e.css`가 될 수 있습니다.
  챕터 HTML 파일은 이름이 바뀌지 않습니다.
  정적 CSS와 JS 파일은 `{{ resource "filename" }}` 지시어를 사용하여 서로를 참조할 수 있습니다.
  기본값은 `true`입니다.
- **sidebar-header-nav:** `true`이면 사이드바에 현재 페이지의 헤더에 대한 내비게이션이 포함됩니다. 기본값은 `true`입니다.

[custom domain]: https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site

### `[output.html.print]`

`[output.html.print]` 테이블은 인쇄 가능한 출력을 제어하기 위한 옵션을 제공합니다.
기본적으로 mdBook은 책의 오른쪽 상단에 <i class="fa fa-print"></i>처럼 보이는 아이콘을 포함하여 책을 단일 페이지로 인쇄합니다.

```toml
[output.html.print]
enable = true    # 인쇄 가능한 출력 지원 포함
page-break = true # 각 챕터 뒤에 페이지 나누기 삽입
```

- **enable:** 인쇄 지원을 활성화합니다. `false`이면 모든 인쇄 지원이
  렌더링되지 않습니다. 기본값은 `true`입니다.
- **page-break:** 챕터 간에 페이지 나누기를 삽입합니다. 기본값은 `true`입니다.

### `[output.html.fold]`

`[output.html.fold]` 테이블은 내비게이션 사이드바에서 챕터 목록의 접기를 제어하기 위한 옵션을 제공합니다.

```toml
[output.html.fold]
enable = false    # 섹션 접기를 활성화할지 여부
level = 0         # 접기를 시작할 깊이
```

- **enable:** 섹션 접기를 활성화합니다. 비활성화되면 모든 접기가 열린 상태입니다.
  기본값은 `false`입니다.
- **level:** 값이 높을수록 더 많은 접힌 영역이 열려 있습니다. level이 0이면 모든
  접기가 닫힌 상태입니다. 기본값은 `0`입니다.

### `[output.html.playground]`

`[output.html.playground]` 테이블은 Rust 샘플 코드 블록과 [Rust Playground]와의 통합을 제어하기 위한 옵션을 제공합니다.

[Rust Playground]: https://play.rust-lang.org/

```toml
[output.html.playground]
editable = false         # 소스 코드 편집 허용
copyable = true          # 코드 스니펫 복사를 위한 복사 버튼 포함
copy-js = true           # 코드 편집기를 위한 JavaScript 포함
line-numbers = false     # 편집 가능한 코드에 줄 번호 표시
runnable = true          # rust 코드에 실행 버튼 표시
```

- **editable:** 소스 코드 편집을 허용합니다. 기본값은 `false`입니다.
- **copyable:** 코드 스니펫에 복사 버튼을 표시합니다. 기본값은 `true`입니다.
- **copy-js:** 편집기를 위한 JavaScript 파일을 출력 디렉토리로 복사합니다.
  기본값은 `true`입니다.
- **line-numbers:** 편집 가능한 코드 섹션에 줄 번호를 표시합니다. `editable`과 `copy-js`가 모두 `true`여야 합니다. 기본값은 `false`입니다.
- **runnable:** rust 코드 스니펫에 실행 버튼을 표시합니다. 이를 `false`로 변경하면 플레이그라운드에서 실행 기능이 전역적으로 비활성화됩니다. 기본값은 `true`입니다.

[Ace]: https://ace.c9.io/

### `[output.html.code]`

`[output.html.code]` 테이블은 코드 블록을 제어하기 위한 옵션을 제공합니다.

```toml
[output.html.code]
# 언어별 접두사 문자열 (하나 이상의 문자).
# 공백+접두사로 시작하는 모든 줄은 숨겨집니다.
hidelines = { python = "~" }
```

- **hidelines:** 각 언어별로 [숨겨진 코드 라인](../mdbook.md#hiding-code-lines)이 작동하는 방식을 정의하는 테이블입니다.
  키는 언어이고 값은 해당 접두사로 시작하는 코드 라인을 숨기게 하는 문자열입니다.

### `[output.html.search]`

`[output.html.search]` 테이블은 내장 텍스트 [검색]을 제어하기 위한 옵션을 제공합니다.
mdBook은 `search` 기능이 활성화된 상태로 컴파일되어야 합니다(기본적으로 활성화됨).

[검색]: ../../guide/reading.md#search

```toml
[output.html.search]
enable = true            # 검색 기능 활성화
limit-results = 30       # 최대 검색 결과 수
teaser-word-count = 30   # 검색 결과 티저에 사용될 단어 수
use-boolean-and = true   # 여러 검색어가 모두 일치해야 함
boost-title = 2          # 헤더에서 일치되는 경우의 랭킹 부스트 계수
boost-hierarchy = 1      # 페이지 이름에서 일치되는 경우의 랭킹 부스트 계수
boost-paragraph = 1      # 텍스트에서 일치되는 경우의 랭킹 부스트 계수
expand = true            # 부분 단어가 더 긴 용어와 일치
heading-split-level = 3  # 결과를 헤딩 레벨에 링크
copy-js = true           # 검색을 위한 JavaScript 코드 포함
```

- **enable:** 검색 기능을 활성화합니다. 기본값은 `true`입니다.
- **limit-results:** 최대 검색 결과 수입니다. 기본값은 `30`입니다.
- **teaser-word-count:** 검색 결과 티저에 사용될 단어 수입니다.
  기본값은 `30`입니다.
- **use-boolean-and:** 여러 검색어 간의 논리 링크를 정의합니다.
  true이면 모든 검색어가 각 결과에 나타나야 합니다. 기본값은 `false`입니다.
- **boost-title:** 검색어가 헤더에 나타날 경우 검색 결과 점수의
  부스트 계수입니다. 기본값은 `2`입니다.
- **boost-hierarchy:** 검색어가 계층에 나타날 경우 검색 결과 점수의
  부스트 계수입니다. 계층에는 상위 문서의 모든 제목과
  모든 상위 헤딩이 포함됩니다. 기본값은 `1`입니다.
- **boost-paragraph:** 검색어가 텍스트에 나타날 경우 검색 결과 점수의
  부스트 계수입니다. 기본값은 `1`입니다.
- **expand:** 검색이 더 긴 결과와 일치해야 하는 경우 true입니다. 예를 들어 `micro`로
  검색하면 `microwave`와 일치해야 합니다. 기본값은 `true`입니다.
- **heading-split-level:** 검색 결과는 결과를 포함하는 문서의 섹션에 링크됩니다.
  문서는 이 레벨 이하의 헤딩으로 섹션으로 분할됩니다. 기본값은 `3`입니다. (`### 이것은 레벨 3 헤딩입니다`)
- **copy-js:** 검색 구현을 위한 JavaScript 파일을 출력 디렉토리로
  복사합니다. 기본값은 `true`입니다.

#### `[output.html.search.chapter]`

[`output.html.search.chapter`] 테이블은 챕터 또는 디렉토리별로 검색 설정을 수정할 수 있는 기능을 제공합니다. 각 키는 챕터 소스 파일 또는 디렉토리의 경로이고, 값은 해당 경로에 적용할 설정 테이블입니다. 이는 재귀적으로 병합되며, 더 구체적인 경로가 우선순위를 가집니다.

```toml
[output.html.search.chapter]
# `appendix` 디렉토리의 모든 챕터에 대한 검색 인덱싱을 비활성화합니다.
"appendix" = { enable = false }
# 이 하나의 부록 챕터에만 검색 인덱싱을 활성화합니다.
"appendix/glossary.md" = { enable = true }
```

- **enable:** 주어진 챕터에 대한 검색 인덱싱을 활성화하거나 비활성화합니다. 기본값은 `true`입니다. 이는 전체 `output.html.search.enable` 설정을 오버라이드하지 않습니다. 모든 검색 기능이 활성화되려면 해당 설정이 `true`여야 합니다. 챕터에 대한 인덱싱을 비활성화할 때는 사용자가 용어를 검색하고 찾을 것으로 기대할 때 혼란을 일으할 수 있으므로 주의해야 합니다. 이는 챕터를 인덱스에 유지하는 것이 검색 결과의 품질에 문제를 일으킬 수 있는 예외적인 상황에서만 사용해야 합니다.

### `[output.html.redirect]`

`[output.html.redirect]` 테이블은 리다이렉트를 추가하는 방법을 제공합니다.
이는 페이지를 이동, 이름 변경 또는 제거할 때 이전 URL에 대한 링크가 새 위치로 이동하도록 하는 데 유용합니다.

```toml
[output.html.redirect]
"/appendices/bibliography.html" = "https://rustc-dev-guide.rust-lang.org/appendix/bibliography.html"
"/other-installation-methods.html" = "../infra/other-installation-methods.html"

# 프래그먼트 리다이렉트도 작동합니다.
"/some-existing-page.html#old-fragment" = "some-existing-page.html#new-fragment"

# 삭제된 페이지에 대해서도 프래그먼트 리다이렉트가 작동합니다.
"/old-page.html" = "new-page.html"
"/old-page.html#old-fragment" = "new-page.html#new-fragment"
```

테이블에는 키-값 쌍이 포함되어 있으며, 키는 빌드 디렉토리로부터의 절대 경로로 리다이렉트 파일을 생성해야 하는 위치입니다(예: `/appendices/bibliography.html`).
값은 브라우저가 내비게이션해야 하는 유효한 URI가 될 수 있습니다(예: `https://rust-lang.org/`, `/overview.html`, 또는 `../bibliography.html`).

이는 주어진 위치로 자동으로 리다이렉트할 HTML 페이지를 생성합니다.

프래그먼트 리다이렉트가 지정되면 페이지는 JavaScript를 사용하여 올바른 위치로 리다이렉트해야 합니다. 이는 섹션 헤더를 이름 변경하거나 이동할 때 유용합니다. 프래그먼트 리다이렉트는 기존 페이지와 삭제된 페이지 모두에서 작동합니다.

## 마크다운 렌더러

마크다운 렌더러는 전처리기를 실행한 다음 결과
마크다운을 출력합니다. 이는 주로 전처리기 디버깅에 유용하며, 특히
`mdbook test`와 함께 사용하여 `mdbook`이 `rustdoc`에 전달하는
마크다운을 확인하는 데 유용합니다.

마크다운 렌더러는 `mdbook`에 포함되어 있지만 기본적으로 비활성화되어 있습니다.
다음과 같이 `book.toml`에 빈 테이블을 추가하여 활성화하세요:

```toml
[output.markdown]
```

현재 마크다운 렌더러에 대한 설정 옵션은 없으며
단지 활성화 또는 비활성화만 가능합니다.

마크다운 렌더러 이전에 실행해야 할 전처리기를 지정하는 방법은
[전처리기 문서](preprocessors.md)를 참조하세요.
