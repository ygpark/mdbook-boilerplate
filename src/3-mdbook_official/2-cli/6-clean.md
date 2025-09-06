# clean 명령어

clean 명령어는 생성된 책과 기타 빌드 아티팩트를 삭제하는 데 사용됩니다.

```bash
mdbook clean
```

#### 디렉토리 지정

`clean` 명령어는 현재 작업 디렉토리 대신 책의 루트로 사용할 디렉토리를 인수로 받을 수 있습니다.

```bash
mdbook clean path/to/book
```

#### `--dest-dir`

`--dest-dir` (`-d`) 옵션을 사용하면 이 명령어에 의해 삭제될 책의 출력 디렉토리를 재정의할 수 있습니다. 상대 경로는 현재 디렉토리를 기준으로 해석됩니다. 지정되지 않으면 `book.toml`의 `build.build-dir` 키 값 또는 `./book`이 기본값이 됩니다.

```bash
mdbook clean --dest-dir=path/to/book
```

`path/to/book`은 절대 경로나 상대 경로를 사용할 수 있습니다.
