# completions 명령어

completions 명령어는 일반적인 쉘 몇 가지에 대한 자동 완성 기능을 생성하는 데 사용됩니다.
이는 쉘에서 `mdbook`을 입력한 후 쉘의 자동 완성 키(보통 Tab 키)를 누르면 유효한 옵션들이 표시되거나 부분 입력을 완성할 수 있다는 의미입니다.

다음과 같이 쉘에 대해 먼저 완성 기능을 설치해야 합니다:

```bash
# bash
mdbook completions bash > ~/.local/share/bash-completion/completions/mdbook
# oh-my-zsh
mdbook completions zsh > ~/.oh-my-zsh/completions/_mdbook
autoload -U compinit && compinit
```

이 명령어는 주어진 쉘에 대한 완성 스크립트를 출력합니다.
지원되는 쉘 목록을 보려면 `mdbook completions --help`를 실행하세요.

완성 기능을 어디에 배치할지는 사용하는 쉘과 운영 체제에 따라 달라집니다.
스크립트를 어디에 배치할지에 대한 자세한 정보는 사용하는 쉘의 문서를 참조하세요.
