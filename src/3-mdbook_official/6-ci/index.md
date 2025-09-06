# 지속적 통합에서 `mdbook` 실행하기

[GitHub Actions]나 [GitLab CI/CD]와 같은 다양한 서비스를 사용하여 책을 자동으로 테스트하고 배포할 수 있습니다.

다음은 mdBook을 실행하도록 서비스를 구성하는 방법에 대한 일반적인 가이드라인을 제공합니다.
구체적인 방법들은 [Automated Deployment] 위키 페이지에서 찾을 수 있습니다.

[GitHub Actions]: https://docs.github.com/en/actions
[GitLab CI/CD]: https://docs.gitlab.com/ee/ci/
[Automated Deployment]: https://github.com/rust-lang/mdBook/wiki/Automated-Deployment

## mdBook 설치하기

mdBook을 설치하는 여러 가지 전략이 있습니다.
특정 방법은 필요와 선호도에 따라 달라집니다.

### 사전 컴파일된 바이너리

가장 쉬운 방법은 [GitHub 릴리즈 페이지][releases]에서 찾을 수 있는 사전 컴파일된 바이너리를 사용하는 것입니다.
간단한 접근법은 인기 있는 `curl` CLI 도구를 사용하여 실행 파일을 다운로드하는 것입니다:

```sh
mkdir bin
curl -sSL https://github.com/rust-lang/mdBook/releases/download/{{ mdbook-version }}/mdbook-{{ mdbook-version }}-x86_64-unknown-linux-gnu.tar.gz | tar -xz --directory=bin
bin/mdbook build
```

이 접근법에 대한 고려사항:

* 상대적으로 빠르며, 반드시 캐싱을 다룰 필요가 없습니다.
* Rust 설치가 필요하지 않습니다.
* 특정 URL을 지정하면 새 버전을 얻기 위해 스크립트를 수동으로 업데이트해야 합니다.
  특정 버전에 고정하려는 경우 이것이 장점일 수 있습니다.
  하지만 일부 사용자는 새 버전이 게시될 때 자동으로 받는 것을 선호합니다.
* GitHub CDN이 사용 가능해야 합니다.

[releases]: https://github.com/rust-lang/mdBook/releases

### 소스에서 빌드하기

소스에서 빌드하려면 Rust가 설치되어 있어야 합니다.
일부 서비스에는 Rust가 사전 설치되어 있지만, 그렇지 않은 경우 설치 단계를 추가해야 합니다.

Rust를 설치한 후, `cargo install`을 사용하여 mdBook을 빌드하고 설치할 수 있습니다.
mdBook의 최신 **호환성을 깨뜨리지 않는** 버전을 얻을 수 있도록 SemVer 버전 지정자를 사용하는 것을 권장합니다.
예를 들어:

```sh
cargo install mdbook --no-default-features --features search --vers "^0.4" --locked
```

이것은 여러 권장 옵션을 포함합니다:

* `--no-default-features` --- CI에서 필요하지 않을 가능성이 높은 `mdbook serve`에서 사용되는 HTTP 서버와 같은 기능을 비활성화합니다.
  이렇게 하면 빌드 시간이 크게 단축됩니다.
* `--features search` --- 기본 기능을 비활성화하면 내장된 [검색] 기능과 같이 원하는 기능을 수동으로 활성화해야 합니다.
* `--vers "^0.4"` --- 이것은 `0.4` 시리즈의 최신 버전을 설치합니다.
  하지만 `0.5.0`과 같은 이후 버전은 빌드를 깨뜨릴 수 있으므로 설치되지 않습니다.
  이미 설치된 이전 버전이 있다면 Cargo가 자동으로 mdBook을 업그레이드합니다.
* `--locked` --- 이것은 mdBook이 릴리즈될 때 사용된 의존성을 사용합니다.
  `--locked` 없이는 모든 의존성의 최신 버전을 사용하는데, 이는 마지막 릴리즈 이후의 수정 사항을 포함할 수 있지만 (드물게) 빌드 문제를 일으킬 수도 있습니다.

mdBook 빌드가 다소 느릴 수 있으므로 캐싱 옵션을 조사하고 싶을 것입니다.

[검색]: guide/reading.md#search

## 테스트 실행하기

변경 사항을 푸시하거나 풀 리퀘스트를 생성할 때마다 [`mdbook test`]를 사용하여 테스트를 실행하고 싶을 수 있습니다.
이는 책에 있는 Rust 코드 예제를 검증하는 데 사용할 수 있습니다.

이를 위해서는 Rust가 설치되어 있어야 합니다.
일부 서비스에는 Rust가 사전 설치되어 있지만, 그렇지 않은 경우 설치 단계를 추가해야 합니다.

적절한 버전의 Rust가 설치되어 있는지 확인하는 것 외에는, 책 디렉토리에서 `mdbook test`를 실행하는 것 이상으로 할 일이 많지 않습니다.

깨진 링크를 확인하는 [mdbook-linkcheck]와 같은 다른 종류의 테스트 실행도 고려해볼 수 있습니다.
또는 자체적인 스타일 검사, 맞춤법 검사기, 또는 다른 테스트가 있다면 CI에서 실행하는 것이 좋습니다.

[`mdbook test`]: cli/test.md
[mdbook-linkcheck]: https://github.com/Michael-F-Bryan/mdbook-linkcheck#continuous-integration

## 배포하기

책을 자동으로 배포하고 싶을 수 있습니다.
일부는 변경 사항이 푸시될 때마다 이를 수행하기를 원하고, 다른 이들은 특정 릴리즈가 태그될 때만 배포하기를 원할 수 있습니다.

웹 서비스에 변경 사항을 푸시하는 방법의 세부 사항을 이해해야 합니다.
예를 들어, [GitHub Pages]는 특정 git 브랜치에 출력을 커밋하는 것만 요구합니다.
다른 서비스들은 원격 서버에 연결하기 위해 SSH와 같은 것을 사용해야 할 수 있습니다.

기본 개요는 출력을 생성하기 위해 `mdbook build`를 실행하고, 그 다음 파일들(`book` 디렉토리에 있는)을 올바른 위치로 전송하는 것입니다.

그 다음 웹 서비스에서 캐시를 무효화해야 하는지 고려해야 할 수 있습니다.

다양한 서비스의 예제는 [Automated Deployment] 위키 페이지를 참조하세요.

[GitHub Pages]: https://docs.github.com/en/pages

### 404 처리

mdBook은 깨진 링크에 사용할 404 페이지를 자동으로 생성합니다.
기본 출력은 책의 루트에 있는 `404.html`이라는 이름의 파일입니다.
[GitHub Pages]와 같은 일부 서비스는 깨진 링크에 대해 이 페이지를 자동으로 사용합니다.
다른 서비스의 경우, 독자가 책으로 돌아갈 수 있는 네비게이션을 제공하므로 이 페이지를 사용하도록 웹 서버를 구성하는 것을 고려해야 할 수 있습니다.

책이 도메인의 루트에 배포되지 않는 경우, 404 페이지가 올바르게 작동하도록 [`output.html.site-url`] 설정을 해야 합니다.
정적 파일(CSS 등)을 올바르게 로드하기 위해 책이 어디에 배포되는지 알아야 합니다.
예를 들어, 이 가이드는 <https://rust-lang.github.io/mdBook/>에 배포되며, `site-url` 설정은 다음과 같이 구성됩니다:

```toml
# book.toml
[output.html]
site-url = "/mdBook/"
```

책에 `src/404.md`라는 이름의 파일을 만들어 404 페이지의 모양을 사용자 정의할 수 있습니다.
다른 파일명을 사용하려면 [`output.html.input-404`]를 다른 파일명으로 설정할 수 있습니다.

[`output.html.site-url`]: format/configuration/renderers.md#html-renderer-options
[`output.html.input-404`]: format/configuration/renderers.md#html-renderer-options
