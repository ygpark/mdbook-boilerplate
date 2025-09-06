# mdBook 전용 기능

## 코드 줄 숨기기

mdBook에는 특정 접두어를 앞에 붙여서 코드 줄을 숨길 수 있는 기능이 있습니다.

Rust 언어의 경우, [Rustdoc과 마찬가지로][rustdoc-hide] `# `(공백이 뒤따르는 `#`)를 줄 앞에 붙여서 숨길 수 있습니다.
이 접두어는 `##`로 이스케이프하여 리터럴 문자열 `# `으로 시작해야 하는 줄의 숨김을 방지할 수 있습니다 (자세한 내용은 [Rustdoc 문서][rustdoc-hide] 참조)

[rustdoc-hide]: https://doc.rust-lang.org/stable/rustdoc/write-documentation/documentation-tests.html#hiding-portions-of-the-example

```bash
# fn main() {
    let x = 5;
    let y = 6;

    println!("{}", x + y);
# }
```

다음과 같이 렌더링됩니다

```rust
# fn main() {
    let x = 5;
    let y = 6;

    println!("{}", x + y);
# }
```

코드 블록을 탭하거나 마우스를 호버하면, 숨겨진 줄의 가시성을 토글하는 눈알 아이콘(<i class="fa fa-eye"></i>)이 나타납니다.

기본적으로 이것은 `rust`로 주석이 달린 코드 예제에만 작동합니다.
그러나 `book.toml`에서 언어 이름과 접두어 문자를 사용하여 새로운 줄 숨김 접두어를 추가함으로써 다른 언어에 대한 사용자 정의 접두어를 정의할 수 있습니다:

```toml
[output.html.code.hidelines]
python = "~"
```

접두어는 주어진 접두어로 시작하는 모든 줄을 숨깁니다. 위에 표시된 python 접두어를 사용하면 다음과 같습니다:

```bash
~hidden()
nothidden():
~    hidden()
    ~hidden()
    nothidden()
```

다음과 같이 렌더링됩니다

```python
~hidden()
nothidden():
~    hidden()
    ~hidden()
    nothidden()
```

이 동작은 다른 접두어로 로컬에서 재정의할 수 있습니다. 이것은 위와 같은 효과를 가집니다:

~~~markdown
```python,hidelines=!!!
!!!hidden()
nothidden():
!!!    hidden()
    !!!hidden()
    nothidden()
```
~~~

## Rust 플레이그라운드

Rust 언어 코드 블록은 자동으로 코드를 실행하고 코드 블록 바로 아래에 출력을 표시하는 재생 버튼(<i class="fa fa-play"></i>)을 받습니다.
이는 코드를 [Rust Playground]로 전송하여 작동합니다.

```rust
println!("Hello, World!");
```

`main` 함수가 없으면 코드가 자동으로 하나로 래핑됩니다.

코드 블록에 대해 재생 버튼을 비활성화하려면 다음과 같이 코드 블록에 `noplayground` 옵션을 포함할 수 있습니다:

~~~markdown
```rust,noplayground
let mut name = String::new();
std::io::stdin().read_line(&mut name).expect("failed to read line");
println!("Hello {}!", name);
```
~~~

또는 책의 모든 코드 블록에 대해 재생 버튼을 비활성화하려면 다음과 같이 `book.toml`에 설정을 작성할 수 있습니다.

```toml
[output.html.playground]
runnable = false
```

## Rust 코드 블록 속성

추가 속성은 언어 용어 바로 뒤에 쉼표, 공백 또는 탭으로 구분된 용어로 Rust 코드 블록에 포함될 수 있습니다. 예를 들어:

~~~markdown
```rust,ignore
# This example won't be tested.
panic!("oops!");
```
~~~

이것들은 Rust 예제를 테스트하기 위해 [`mdbook test`]를 사용할 때 특히 중요합니다.
이것들은 몇 가지 추가 사항과 함께 [rustdoc 속성]과 동일한 속성을 사용합니다:

* `editable` --- [에디터]를 활성화합니다.
* `noplayground` --- 재생 버튼을 제거하지만 여전히 테스트됩니다.
* `mdbook-runnable` --- 재생 버튼을 강제로 표시합니다.
  이것은 테스트되어서는 안 되지만 독자가 실행할 수 있도록 하고 싶은 예제에 대해 `ignore` 속성과 결합하여 사용할 목적입니다.
* `ignore` --- 테스트되지 않고 재생 버튼도 표시되지 않지만, 여전히 Rust 문법으로 강조 표시됩니다.
* `should_panic` --- 실행되면 패닉을 발생시켜야 합니다.
* `no_run` --- 테스트할 때 코드가 컴파일되지만 실행되지는 않습니다.
  재생 버튼도 표시되지 않습니다.
* `compile_fail` --- 코드가 컴파일에 실패해야 합니다.
* `edition2015`, `edition2018`, `edition2021`, `edition2024` --- 특정 Rust 에디션의 사용을 강제합니다.
  이를 전역적으로 설정하려면 [`rust.edition`]을 참조하세요.

[`mdbook test`]: ../cli/test.md
[rustdoc attributes]: https://doc.rust-lang.org/rustdoc/documentation-tests.html#attributes
[editor]: theme/editor.md
[`rust.edition`]: configuration/general.md#rust-options

## 파일 포함하기

다음 문법으로 책에 파일을 포함할 수 있습니다:

```hbs
\{{#include file.rs}}
```

파일 경로는 현재 소스 파일로부터 상대적이어야 합니다.

mdBook은 포함된 파일을 마크다운으로 해석합니다. include 명령은 주로 코드 스니펫과 예제를 삽입하는 데 사용되므로, 파일 내용을 해석하지 않고 표시하기 위해 명령을 ```` ``` ````로 래핑하는 경우가 많습니다.

````hbs
```
\{{#include file.rs}}
```
````

## 파일의 일부 포함하기
종종 파일의 특정 부분만 필요할 때가 있습니다. 예를 들어 예제에 관련된 줄들만요. 네 가지 다른 부분 포함 모드를 지원합니다:

```hbs
\{{#include file.rs:2}}
\{{#include file.rs::10}}
\{{#include file.rs:2:}}
\{{#include file.rs:2:10}}
```

첫 번째 명령은 파일 `file.rs`의 두 번째 줄만 포함합니다. 두 번째
명령은 10번째 줄까지 모든 줄을 포함합니다. 즉, 11번째부터 파일 끝까지의
줄들은 생략됩니다. 세 번째 명령은 2번째 줄부터 모든 줄을 포함합니다. 즉,
첫 번째 줄은 생략됩니다. 마지막 명령은 2번째부터 10번째 줄로 구성된
`file.rs`의 발췌를 포함합니다.

포함된 파일을 수정할 때 책이 깨지는 것을 방지하기 위해, 줄 번호 대신
앵커를 사용하여 특정 섹션을 포함할 수도 있습니다.
앵커는 일치하는 줄의 쌍입니다. 앵커를 시작하는 줄은 정규식
`ANCHOR:\s*[\w_-]+`와 일치해야 하고, 마찬가지로 끝나는 줄은 정규식
`ANCHOR_END:\s*[\w_-]+`와 일치해야 합니다. 이렇게 하면 앵커를
모든 종류의 주석 줄에 넣을 수 있습니다.

포함할 다음 파일을 고려해 보세요:
```rs
/* ANCHOR: all */

// ANCHOR: component
struct Paddle {
    hello: f32,
}
// ANCHOR_END: component

////////// ANCHOR: system
impl System for MySystem { ... }
////////// ANCHOR_END: system

/* ANCHOR_END: all */
```

그러면 책에서는 다음과 같이 하기만 하면 됩니다:
````hbs
다음은 컴포넌트입니다:
```rust,no_run,noplayground
\{{#include file.rs:component}}
```

다음은 시스템입니다:
```rust,no_run,noplayground
\{{#include file.rs:system}}
```

이것은 전체 파일입니다.
```rust,no_run,noplayground
\{{#include file.rs:all}}
```
````

포함된 앵커 내부의 앵커 패턴이 포함된 줄은 무시됩니다.

## 파일을 포함하지만 지정된 줄을 제외하고는 초기에 숨기기

`rustdoc_include` 헬퍼는 완전한 예제를 포함하는 외부 Rust 파일에서 코드를
포함하지만 `include`와 동일한 방식으로 줄 번호나 앵커로 지정된 특정 줄만
초기에 보여주는 데 사용됩니다.

줄 번호 범위에 없거나 앵커 사이에 없는 줄들도 여전히 포함되지만,
`#`으로 접두어가 붙습니다. 이렇게 하면 독자가 스니펫을 확장하여 완전한 예제를 볼 수 있고,
`mdbook test`를 실행할 때 Rustdoc이 완전한 예제를 사용합니다.

예를 들어, 다음 Rust 프로그램을 포함하는 `file.rs`라는 파일을 고려해 보세요:

```rust
fn main() {
    let x = add_one(2);
    assert_eq!(x, 3);
}

fn add_one(num: i32) -> i32 {
    num + 1
}
```

이 문법을 사용하여 초기에 2번째 줄만 보여주는 스니펫을 포함할 수 있습니다:

````hbs
`add_one` 함수를 호출하려면 `i32`를 전달하고 반환된 값을 `x`에 바인딩합니다:

```rust
\{{#rustdoc_include file.rs:2}}
```
````

이것은 수동으로 코드를 삽입하고 2번째 줄을 제외하고는 모든 것을
`#`를 사용하여 숨긴 것과 동일한 효과를 가집니다:

````hbs
`add_one` 함수를 호출하려면 `i32`를 전달하고 반환된 값을 `x`에 바인딩합니다:

```rust
# fn main() {
    let x = add_one(2);
#     assert_eq!(x, 3);
# }
#
# fn add_one(num: i32) -> i32 {
#     num + 1
# }
```
````

즉, 다음과 같이 보입니다 (파일의 나머지를 보려면 "expand" 아이콘을 클릭하세요):

```rust
# fn main() {
    let x = add_one(2);
#     assert_eq!(x, 3);
# }
#
# fn add_one(num: i32) -> i32 {
#     num + 1
# }
```

## 실행 가능한 Rust 파일 삽입하기

다음 문법으로 실행 가능한 Rust 파일을 책에 삽입할 수 있습니다:

```hbs
\{{#playground file.rs}}
```

Rust 파일의 경로는 현재 소스 파일로부터 상대적이어야 합니다.

재생을 클릭하면 코드 스니펫이 [Rust Playground]로 전송되어
컴파일되고 실행됩니다. 결과는 다시 전송되어 코드 바로 아래에
직접 표시됩니다.

렌더링된 코드 스니펫은 다음과 같습니다:

{{#playground example.rs}}

파일명 뒤에 전달된 모든 추가 값은 코드 블록의 속성으로 포함됩니다.
예를 들어 `\{{#playground example.rs editable}}`는 다음과 같은 코드 블록을 생성합니다:

~~~markdown
```rust,editable
# Contents of example.rs here.
```
~~~

그리고 `editable` 속성은 [Rust 코드 블록 속성](#rust-code-block-attributes)에서 설명한 대로 [에디터]를 활성화합니다.

[Rust Playground]: https://play.rust-lang.org/

## 페이지 \<title\> 제어하기

챕터는 페이지 상단 근처에 `\{{#title ...}}`를 포함하여 목차
(사이드바)에서의 항목과 다른 \<title\>을 설정할 수 있습니다.

```hbs
\{{#title My Title}}
```

## mdBook에서 제공하는 HTML 클래스

<img class="right" src="images/rust-logo-blk.svg" alt="The Rust logo">

### `class="left"` 및 `"right"`

이 클래스들은 인라인 HTML이 이미지를 플로팅할 수 있도록 기본적으로 제공됩니다.

```html
<img class="right" src="images/rust-logo-blk.svg" alt="The Rust logo">
```

### `class="hidden"`

클래스 `hidden`이 있는 HTML 태그는 표시되지 않습니다.

```html
<div class="hidden">이것은 보이지 않습니다.</div>
```

<div class="hidden">이것은 보이지 않습니다.</div>

### `class="warning"`

경고나 비슷한 메모를 눈에 띄게 하려면 warning div로 감싸세요.

```html
<div class="warning">

주의를 기울여야 할 나쁜 상황입니다.

경고 블록은 문서에서 제한적으로 사용해야 합니다. "경고 피로"를 피하기 위해서인데, 이는 사람들이 보통 자신이 하는 일에 중요하지 않기 때문에 경고를 무시하도록 훈련되는 것을 말합니다.

</div>
```

<div class="warning">

주의를 기울여야 할 나쁜 상황입니다.

경고 블록은 문서에서 제한적으로 사용해야 합니다. "경고 피로"를 피하기 위해서인데, 이는 사람들이 보통 자신이 하는 일에 중요하지 않기 때문에 경고를 무시하도록 훈련되는 것을 말합니다.

</div>

## Font-Awesome 아이콘

mdBook에는 [Font Awesome Free의](https://fontawesome.com)
MIT 라이센스 SVG 파일들의 복사본이 포함되어 있습니다. `<i>` 문법을 에뮬레이트하지만 결과를 인라인 SVG로 변환합니다. regular, solid, brands 아이콘만 포함되어 있고, light 아이콘과 같은 유료 기능은 포함되지 않습니다.

예를 들어, 다음 HTML 문법이 주어진 경우:

```hbs
결과는 다음과 같습니다: <i class="fas fa-print"></i>
```

결과는 다음과 같습니다: <i class="fas fa-print"></i>
