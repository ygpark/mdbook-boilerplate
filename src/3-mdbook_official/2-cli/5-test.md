# test 명령어

책을 작성할 때 일부 테스트를 자동화해야 하는 경우가 있습니다. 예를 들어, [The Rust Programming Book](https://doc.rust-lang.org/stable/book/)은 오래될 수 있는 많은 코드 예시를 사용합니다. 따라서 이러한 코드 예시들을 자동으로 테스트할 수 있는 것이 매우 중요합니다.

mdBook은 책에서 사용 가능한 모든 테스트를 실행할 수 있는 `test` 명령어를 지원합니다. 현재는 Rust 테스트만 지원됩니다.

#### 코드 블록에서 테스트 비활성화

rustdoc은 `ignore` 속성을 포함하는 코드 블록을 테스트하지 않습니다:

    ```rust,ignore
    fn main() {}
    ```

rustdoc은 또한 Rust 외의 언어를 지정하는 코드 블록도 테스트하지 않습니다:

    ```markdown
    **Foo**: _bar_
    ```

rustdoc은 언어가 지정되지 않은 코드 블록은 테스트합니다:

    ```
    This is going to cause an error!
    ```

#### 디렉토리 지정

`test` 명령어는 현재 작업 디렉토리 대신 책의 루트로 사용할 디렉토리를 인수로 받을 수 있습니다.

```bash
mdbook test path/to/book
```

#### `--library-path`

`--library-path` (`-L`) 옵션을 사용하면 `rustdoc`이 예시를 빌드하고 테스트할 때 사용하는 라이브러리 검색 경로에 디렉토리를 추가할 수 있습니다. 여러 디렉토리를 여러 옵션(`-L foo -L bar`)으로 지정하거나 쉼표로 구분된 목록(`-L foo,bar`)으로 지정할 수 있습니다. 경로는 프로젝트의 빌드 출력이 포함된 Cargo [build cache](https://doc.rust-lang.org/cargo/guide/build-cache.html) `deps` 디렉토리를 가리켜야 합니다. 예를 들어, Rust 프로젝트의 책이 `my-book`이라는 디렉토리에 있다면, 다음 명령어는 `test`를 실행할 때 크레이트의 종속성들을 포함합니다:

```shell
mdbook test my-book -L target/debug/deps/
```

자세한 정보는 `rustdoc` 명령줄 [문서](https://doc.rust-lang.org/rustdoc/command-line-arguments.html#-l--library-path-where-to-look-for-dependencies)를 참조하세요.

#### `--chapter`

`--chapter` (`-c`) 옵션을 사용하면 챕터 이름이나 챕터에 대한 상대 경로를 사용하여 책의 특정 챕터를 테스트할 수 있습니다.
