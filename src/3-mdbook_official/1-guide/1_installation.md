# 설치

mdBook CLI 도구를 설치하는 여러 가지 방법이 있습니다.
필요에 맞는 아래 방법 중 하나를 선택하세요.
자동 배포를 위해 mdBook을 설치하는 경우, 설치 방법에 대한 더 많은 예시를 위해 [지속적 통합] 챕터를 확인하세요.

[지속적 통합]: ../continuous-integration.md

## 사전 컴파일된 바이너리

실행 가능한 바이너리는 [GitHub 릴리즈 페이지][releases]에서 다운로드할 수 있습니다.
플랫폼(Windows, macOS, 또는 Linux)에 맞는 바이너리를 다운로드하고 아카이브를 추출하세요.
아카이브에는 책을 빌드하는 데 실행할 수 있는 `mdbook` 실행 파일이 포함되어 있습니다.

실행을 용이하게 하려면 바이너리 경로를 `PATH`에 추가하세요.

[releases]: https://github.com/rust-lang/mdBook/releases

## Rust를 사용하여 소스에서 빌드

소스에서 `mdbook` 실행 파일을 빌드하려면 먼저 Rust와 Cargo를 설치해야 합니다.
[Rust 설치 페이지]의 지침을 따르세요.
mdBook은 현재 최소 Rust 버전 1.85가 필요합니다.

Rust를 설치한 후, 다음 명령어를 사용하여 mdBook을 빌드하고 설치할 수 있습니다:

```sh
cargo install mdbook
```

이것은 [crates.io]에서 mdBook을 자동으로 다운로드하고, 빌드하고, Cargo의 전역 바이너리 디렉토리(기본적으로 `~/.cargo/bin/`)에 설치합니다.

새 버전으로 업데이트하고 싶을 때마다 `cargo install mdbook`을 다시 실행할 수 있습니다.
해당 명령어는 더 새로운 버전이 있는지 확인하고, 더 새로운 버전이 발견되면 mdBook을 다시 설치합니다.

제거하려면 `cargo uninstall mdbook` 명령어를 실행하세요.

[Rust 설치 페이지]: https://www.rust-lang.org/tools/install
[crates.io]: https://crates.io/

### 최신 마스터 버전 설치

crates.io에 게시된 버전은 GitHub에 호스팅된 버전보다 약간 뒤처질 것입니다.
최신 버전이 필요한 경우 mdBook의 git 버전을 직접 빌드할 수 있습니다.
Cargo가 이를 ***매우 쉽게*** 만듭니다!

```sh
cargo install --git https://github.com/rust-lang/mdBook.git mdbook
```

다시 한번, Cargo bin 디렉토리를 `PATH`에 추가하는 것을 잊지 마세요.

## 수정 및 기여

mdBook 자체를 수정하는 데 관심이 있다면, 자세한 정보는 [기여 가이드]를 확인하세요.

[기여 가이드]: https://github.com/rust-lang/mdBook/blob/master/CONTRIBUTING.md
