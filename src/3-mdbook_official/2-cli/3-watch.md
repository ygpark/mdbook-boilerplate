# watch 명령어

`watch` 명령어는 파일이 변경될 때마다 책이 렌더링되기를 원할 때 유용합니다. 파일이 변경될 때마다 `mdbook build`를 반복적으로 실행할 수 있습니다. 하지만 `mdbook watch`를 한 번 사용하면 파일들을 모니터링하고 파일을 수정할 때마다 자동으로 빌드를 트리거합니다. 여기에는 `SUMMARY.md`에 여전히 언급되어 있는 삭제된 파일들을 다시 생성하는 것도 포함됩니다!

#### 디렉토리 지정

`watch` 명령어는 현재 작업 디렉토리 대신 책의 루트로 사용할 디렉토리를 인수로 받을 수 있습니다.

```bash
mdbook watch path/to/book
```

#### `--open`

`--open` (`-o`) 옵션을 사용하면, mdbook이 렌더링된 책을 기본 웹 브라우저에서 열어줍니다.

#### `--dest-dir`

`--dest-dir` (`-d`) 옵션을 사용하면 책의 출력 디렉토리를 변경할 수 있습니다. 상대 경로는 현재 디렉토리를 기준으로 해석됩니다. 지정되지 않으면 `book.toml`의 `build.build-dir` 키 값 또는 `./book`이 기본값이 됩니다.

{{#include arg-watcher.md}}

#### 제외 패턴 지정

`watch` 명령어는 책 루트 디렉토리의 `.gitignore` 파일에 나열된 파일들에 대해서는 자동으로 빌드를 트리거하지 않습니다. `.gitignore` 파일에는 [gitignore 문서](https://git-scm.com/docs/gitignore)에 설명된 파일 패턴이 포함될 수 있습니다. 이는 일부 에디터에서 생성되는 임시 파일들을 무시하는 데 유용할 수 있습니다.

_주의: 책 루트 디렉토리의 `.gitignore`만 사용됩니다. 전역 `$HOME/.gitignore`나 상위 디렉토리의 `.gitignore` 파일들은 사용되지 않습니다._
