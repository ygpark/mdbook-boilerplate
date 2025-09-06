# 일반 설정

***book.toml*** 파일에서 책의 매개변수를 설정할 수 있습니다.

***book.toml*** 파일이 어떤 모습일지에 대한 예시입니다:

```toml
[book]
title = "Example book"
authors = ["John Doe"]
description = "The example book covers examples."

[rust]
edition = "2018"

[build]
build-dir = "my-example-book"
create-missing = false

[preprocessor.index]

[preprocessor.links]

[output.html]
additional-css = ["custom.css"]

[output.html.search]
limit-results = 15
```

## 지원되는 설정 옵션

설정에서 지정된 **모든** 상대 경로는 항상 설정 파일이 위치한
책의 루트를 기준으로 상대적으로 취해진다는 점이 중요합니다.

### 일반 메타데이터

이는 당신의 책에 대한 일반적인 정보입니다.

- **title:** 책의 제목
- **authors:** 책의 저자(들)
- **description:** 각 페이지의 html `<head>`에 메타 정보로 추가되는 책에 대한 설명
- **src:** 기본적으로 소스 디렉토리는 루트 폴더 바로 아래의
  `src`라는 디렉토리에서 찾습니다. 하지만 이는 설정 파일의 `src`
  키로 구성할 수 있습니다.
- **language:** 책의 주요 언어로, 예를 들어 `<html lang="ko">` 같은 언어 속성으로 사용됩니다.
  이는 또한 책 내에서 텍스트의 방향(RTL, LTR)을 결정하는 데도 사용됩니다.
- **text-direction**: 책에서 텍스트의 방향: 왼쪽에서 오른쪽(LTR) 또는 오른쪽에서 왼쪽(RTL). 가능한 값: `ltr`, `rtl`.
  지정되지 않으면 텍스트 방향은 책의 `language` 속성에서 파생됩니다.

**book.toml**
```toml
[book]
title = "Example book"
authors = ["John Doe", "Jane Doe"]
description = "The example book covers examples."
src = "my-src"  # the source files will be found in `root/my-src` instead of `root/src`
language = "en"
text-direction = "ltr"
```

### Rust 옵션

테스트 실행 및 플레이그라운드 통합과 관련된 Rust 언어 옵션.

```toml
[rust]
edition = "2015"   # 코드 블록의 기본 에디션
```

- **edition**: 코드 스니펫에 기본적으로 사용할 Rust 에디션. 기본값은
  `"2015"`입니다. 개별 코드 블록은 다음과 같이 `edition2015`,
  `edition2018`, `edition2021` 또는 `edition2024` 주석으로 제어할 수 있습니다:

  ~~~text
  ```rust,edition2015
  // 이는 2015에서만 작동합니다.
  let try = true;
  ```
  ~~~

### 빌드 옵션

이는 당신의 책 빌드 과정을 제어합니다.

```toml
[build]
build-dir = "book"                # 출력이 배치되는 디렉토리
create-missing = true             # 누락된 페이지를 생성할지 여부
use-default-preprocessors = true  # 기본 전처리기 사용
extra-watch-dirs = []             # 빌드 트리거를 위해 감시할 디렉토리
```

- **build-dir:** 렌더링된 책을 넣을 디렉토리. 기본적으로 이는
  책의 루트 디렉토리에 있는 `book/`입니다.
  이는 `--dest-dir` CLI 옵션으로 오버라이드할 수 있습니다.
- **create-missing:** 기본적으로 `SUMMARY.md`에 지정된 누락된 파일은
  책이 빌드될 때 생성됩니다 (즉, `create-missing = true`). 이것이
  `false`이면 대신 어떤 파일이 존재하지 않을 경우 빌드 프로세스가 오류와 함께 종료됩니다.
- **use-default-preprocessors:** 이 옵션을 `false`로 설정하여 기본 전처리기(`links` &
  `index`)를 비활성화합니다.

  동일한 및/또는 다른 전처리기가 설정 테이블을 통해 선언된 경우
  대신 그것들이 실행됩니다.

  - 명확성을 위해, 전처리기 설정이 없으면 기본 `links`와
    `index`가 실행됩니다.
  - `use-default-preprocessors = false`로 설정하면 이러한
    기본 전처리기가 실행되지 않습니다.
  - 예를 들어 `[preprocessor.links]`를 추가하면 `use-default-preprocessors`에 관계없이
    `links`가 실행됩니다.
- **extra-watch-dirs**: `watch` 및 `serve` 명령에서 감시될 디렉토리에 대한 경로 목록.
  이러한 디렉토리 아래의 파일 변경사항은 리빌드를 트리거합니다. 당신의 책이 `src` 디렉토리 외부의 파일에 의존하는 경우 유용합니다.
