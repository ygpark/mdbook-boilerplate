# 에디터

실행 가능한 코드 플레이그라운드 제공 외에도, mdBook은 선택적으로 편집 가능하도록 할 수 있습니다. 편집 가능한 코드 블록을 활성화하려면 ***book.toml***에 다음을 추가해야 합니다:

```toml
[output.html.playground]
editable = true
```

편집 가능한 코드 블록을 활성화한 후, 코드 블록을 편집 가능하게 만들려면 `editable` 속성을 추가해야 합니다:

~~~markdown
```rust,editable
fn main() {
    let number = 5;
    print!("{}", number);
}
```
~~~

위의 코드는 다음과 같은 편집 가능한 플레이그라운드를 생성합니다:

```rust,editable
fn main() {
    let number = 5;
    print!("{}", number);
}
```

편집 가능한 플레이그라운드에서 새로운 `변경 취소` 버튼을 확인할 수 있습니다.

## 에디터 사용자 정의

기본적으로 에디터는 [Ace](https://ace.c9.io/) 에디터이지만, 원하는 경우 다른 폴더를 제공하여 기능을 재정의할 수 있습니다:

```toml
[output.html.playground]
editable = true
editor = "/path/to/editor"
```

에디터 변경사항이 올바르게 작동하려면, `theme` 폴더 내의 `book.js`가 기본 Ace 에디터와 일부 결합되어 있으므로 재정의해야 합니다.
