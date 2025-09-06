# 환경 변수

모든 설정 값은 해당 환경 변수를 설정하여 명령줄에서 오버라이드할 수 있습니다.
많은 운영 체제에서 환경 변수를 영숫자 문자나 `_`로만 제한하기 때문에
설정 키는 일반적인 `foo.bar.baz` 형식과는 약간 다르게 포맷해야 합니다.

`MDBOOK_`로 시작하는 변수들이 설정에 사용됩니다. 키는 `MDBOOK_` 접두사를 제거하고
결과 문자열을 `kebab-case`로 변환하여 생성됩니다. 이중 밑줄(`__`)은 중첩된 키를 분리하고,
단일 밑줄(`_`)은 대시(`-`)로 바뀝니다.

예를 들어:

- `MDBOOK_foo` -> `foo`
- `MDBOOK_FOO` -> `foo`
- `MDBOOK_FOO__BAR` -> `foo.bar`
- `MDBOOK_FOO_BAR` -> `foo-bar`
- `MDBOOK_FOO_bar__baz` -> `foo-bar.baz`

따라서 `MDBOOK_BOOK__TITLE` 환경 변수를 설정하면 `book.toml`을 건드리지 않고도
책의 제목을 오버라이드할 수 있습니다.

> **참고:** 더 복잡한 설정 항목을 설정하기 쉽게 하기 위해 환경 변수의 값은
> 먼저 JSON으로 파싱되고, 파싱에 실패하면 문자열로 대체됩니다.
>
> 이는 원한다면 다음과 같은 것으로 책을 빌드할 때 모든 책 메타데이터를
> 오버라이드할 수 있다는 것을 의미합니다.
>
> ```shell
> $ export MDBOOK_BOOK='{"title": "My Awesome Book", "authors": ["Michael-F-Bryan"]}'
> $ mdbook build
> ```

후자의 경우는 스크립트나 CI에서 `mdbook`을 호출하는 상황에서 유용할 수 있으며,
빌드하기 전에 `book.toml`을 업데이트하는 것이 때때로 불가능한 경우에 해당합니다.
