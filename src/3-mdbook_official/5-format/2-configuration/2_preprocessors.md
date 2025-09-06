# 전처리기 설정

전처리기는 원본 마크다운 소스가 렌더러로 전송되기 전에 수정할 수 있는 확장 기능입니다.

다음 전처리기들이 내장되어 있으며 기본적으로 포함됩니다:

- `links`: 챕터 내의 `{{ #playground }}`, `{{ #include }}`, `{{ #rustdoc_include }}` 핸들바
  헬퍼를 확장하여 파일의 내용을 포함시킵니다.
  자세한 내용은 [파일 포함하기]를 참조하세요.
- `index`: `README.md`라는 이름의 모든 챕터 파일을 `index.md`로 변환합니다. 즉,
  모든 `README.md`는 렌더링된 책에서 인덱스 파일 `index.html`로 렌더링됩니다.

내장 전처리기는 [`build.use-default-preprocessors`] 설정 옵션으로 비활성화할 수 있습니다.

커뮤니티에서 여러 전처리기를 개발했습니다.
사용 가능한 전처리기 목록은 [Third Party Plugins] 위키 페이지를 참조하세요.

새 전처리기를 만드는 방법에 대한 정보는 [개발자를 위한 전처리기] 챕터를 참조하세요.

[파일 포함하기]: ../mdbook.md#including-files
[`build.use-default-preprocessors`]: general.md#build-options
[Third Party Plugins]: https://github.com/rust-lang/mdBook/wiki/Third-party-plugins
[개발자를 위한 전처리기]: ../../for_developers/preprocessors.md

## 커스텀 전처리기 설정

전처리기는 전처리기의 이름과 함께 `book.toml`에 `preprocessor` 테이블을 포함하여 추가할 수 있습니다.
예를 들어, `mdbook-example`이라는 전처리기가 있다면 다음과 같이 포함할 수 있습니다:

```toml
[preprocessor.example]
```

이 테이블을 사용하면 mdBook이 `mdbook-example` 전처리기를 실행합니다.

이 테이블에는 전처리기에 특정한 추가 키-값 쌍을 포함할 수 있습니다.
예를 들어, 예시 전처리기에 추가 설정 옵션이 필요한 경우:

```toml
[preprocessor.example]
some-extra-feature = true
```

## 전처리기 의존성을 렌더러에 고정하기

전처리기가 특정 렌더러에서만 실행되도록 두 개를 서로 바인딩하여
명시적으로 지정할 수 있습니다.

```toml
[preprocessor.example]
renderers = ["html"]  # example 전처리기는 HTML 렌더러에서만 실행됩니다
```

## 자체 명령 제공하기

기본적으로 `book.toml` 파일에 `[preprocessor.foo]` 테이블을 추가하면
`mdbook`은 `mdbook-foo` 실행 파일을 호출하려고 시도합니다. 다른 프로그램 이름을 사용하거나
명령줄 인수를 전달하려면 `command` 필드를 추가하여
이 동작을 오버라이드할 수 있습니다.

```toml
[preprocessor.random]
command = "python random.py"
```

### 선택적 전처리기

설치되지 않은 전처리기를 활성화하면 기본 동작은 오류를 발생시키는 것입니다.
전처리기를 선택사항으로 표시하여 이 동작을 변경할 수 있습니다:

```toml
[preprocessor.example]
optional = true
```

이는 오류를 경고로 감소시킵니다.

## 특정 순서 요구하기

전처리기가 실행되는 순서는 `before`와 `after` 필드로 제어할 수 있습니다.
예를 들어, `linenos` 전처리기가 `{{#include}}`될 수 있는 라인을 처리하도록 하려면, 내장 `links` 전처리기 다음에 실행되어야 하며, 이는 `before` 또는 `after` 필드 중 하나를 사용하여 요구할 수 있습니다:

```toml
[preprocessor.linenos]
after = [ "links" ]
```

또는

```toml
[preprocessor.links]
before = [ "linenos" ]
```

동일한 설정 파일에서 위의 두 가지를 모두 지정하는 것도 가능하지만 중복됩니다.

`before`와 `after`를 통해 지정된 동일한 우선순위를 가진 전처리기는 이름순으로 정렬됩니다.
무한 루프는 감지되어 오류를 발생시킵니다.
