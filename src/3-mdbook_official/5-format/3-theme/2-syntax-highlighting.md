# 구문 하이라이팅

mdBook은 구문 하이라이팅을 위해 커스텀 테마와 함께 [Highlight.js](https://highlightjs.org)를 사용합니다.

자동 언어 감지가 비활성화되어 있으므로, 다음과 같이 사용하는 프로그래밍 언어를 지정해야 합니다:

~~~markdown
```rust
fn main() {
    // Some code
}
```
~~~

## 지원되는 언어

다음 언어들이 기본으로 지원되지만, 자체 `highlight.js` 파일을 제공하여 더 많은 언어를 추가할 수 있습니다:

- apache
- armasm
- bash
- c
- coffeescript
- cpp
- csharp
- css
- d
- diff
- go
- handlebars
- haskell
- http
- ini
- java
- javascript
- json
- julia
- kotlin
- less
- lua
- makefile
- markdown
- nginx
- nim
- nix
- objectivec
- perl
- php
- plaintext
- properties
- python
- r
- ruby
- rust
- scala
- scss
- shell
- sql
- swift
- typescript
- x86asm
- xml
- yaml

## 커스텀 테마
나머지 테마와 마찬가지로, 구문 하이라이팅에 사용되는 파일들도 사용자 정의 파일로 재정의할 수 있습니다.

- ***highlight.js*** 일반적으로 더 최신 버전을 사용하려는 경우가 아니라면 이 파일을 덮어쓸 필요는 없습니다.
- ***highlight.css*** 구문 하이라이팅을 위해 highlight.js에서 사용하는 테마입니다.

`highlight.js`에 다른 테마를 사용하고 싶다면 그들의 웹사이트에서 다운로드하거나 직접 만들어서 `highlight.css`로 이름을 바꾸고 책의 `theme` 폴더에 넣으세요.

이제 기본 테마 대신 사용자의 테마가 사용됩니다.

## 기본 테마 개선

특정 언어에 대해 기본 테마가 적절하지 않다고 생각하거나 개선될 수 있다면, 언제든지 [새 이슈를 제출](https://github.com/rust-lang/mdBook/issues)하여 생각하신 내용을 설명해 주세요. 검토해 보겠습니다.

제안된 개선사항으로 풀 리퀘스트를 생성할 수도 있습니다.

전체적으로 테마는 너무 많은 화려한 색상 없이 밝고 차분해야 합니다.
