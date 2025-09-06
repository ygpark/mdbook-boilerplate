# index.hbs

`index.hbs`는 책을 렌더링하는 데 사용되는 handlebars 템플릿입니다. 
마크다운 파일들이 HTML로 처리된 후 이 템플릿에 주입됩니다.

책의 레이아웃이나 스타일을 변경하고 싶다면, 이 템플릿을 조금 수정해야 할 
가능성이 높습니다. 여기서 알아야 할 사항들을 소개합니다.

## 데이터

많은 데이터가 "컨텍스트"를 통해 handlebars 템플릿에 노출됩니다. handlebars 
템플릿에서 다음과 같이 이 정보에 액세스할 수 있습니다:

```handlebars
{{name_of_property}}
```

노출되는 속성들의 목록은 다음과 같습니다:

- ***language*** `book.toml`에서 지정된 `en` 형태의 책 언어 (지정되지 않으면 기본값은 `en`). 예를 들어 <code class="language-html">\<html lang=\"{{ language }}\"></code>처럼 사용할 수 있습니다.
- ***title*** 현재 페이지에 사용되는 제목. `book_title`이 설정되지 않은 경우 `chapter_title`로 기본 설정되는 것을 제외하고는 `{{ chapter_title }} - {{ book_title }}`와 동일합니다.
- ***book_title*** `book.toml`에서 지정된 책의 제목
- ***chapter_title*** `SUMMARY.md`에 나열된 현재 챕터의 제목

- ***path*** 소스 디렉토리에서 원본 마크다운 파일까지의 상대 경로
- ***content*** 렌더링된 마크다운 내용입니다.
- ***path_to_root*** 현재 파일에서 책의 루트로 가리키는 `../`만으로 구성된 경로입니다. 원본 디렉토리 구조가 유지되므로, 상대 링크 앞에 이 `path_to_root`를 추가하는 것이 유용합니다.
- ***previous*** 및 ***next*** 이전 및 다음 챕터로 링크하는 데 사용되는 객체들입니다. 해당 챕터의 `title` 및 `link` 속성을 포함합니다.
- ***chapters*** 다음 형태의 딕셔너리 배열입니다:
  ```json
  {"section": "1.2.1", "name": "name of this chapter", "path": "dir/markdown.md"}
  ```
  책의 모든 챕터를 포함합니다. 예를 들어 목차(사이드바)를 구성하는 데 사용됩니다.

## Handlebars 헬퍼

액세스할 수 있는 속성 외에도 사용할 수 있는 handlebars 헬퍼들이 있습니다.

### toc

toc 헬퍼는 다음과 같이 사용됩니다:

```handlebars
{{#toc}}{{/toc}}
```

그리고 책의 구조에 따라 다음과 같은 출력을 생성합니다:

```html
<ul class="chapter">
    <li><a href="link/to/file.html">Some chapter</a></li>
    <li>
        <ul class="section">
            <li><a href="link/to/other_file.html">Some other Chapter</a></li>
        </ul>
    </li>
</ul>
```

다른 구조의 목차를 만들고 싶다면, 모든 데이터를 포함하는 chapters 속성에 
액세스할 수 있습니다. 현재로서는 handlebars 헬퍼 대신 JavaScript로 해야 
한다는 제한이 있습니다.

```html
<script>
var chapters = {{chapters}};
// 여기서 처리
</script>
```

### resource

정적 파일의 경로입니다.
`path_to_root`를 암시적으로 포함하며, 
파일명에 해시가 추가되어 이름이 변경된 파일들을 처리합니다.

```handlebars
<link rel="stylesheet" href="{{ resource "css/chrome.css" }}">
```

### fa

mdBook은 [Font Awesome Free의](https://fontawesome.com) MIT 라이선스 SVG 파일들의 
복사본을 포함합니다. 세 개의 위치 인수를 받습니다:

1. Type: "solid", "regular", "brands" 중 하나 (현재 light와 duotone은 지원되지 않음)
2. Icon: [무료 아이콘 세트](https://fontawesome.com/icons?d=gallery&m=free)에서 선택한 것
3. ID (선택사항): 포함된 경우, 아이콘을 감싸는 `<span>` 태그에 HTML ID 속성이 추가됩니다

예를 들어, 다음 handlebars 구문은 이 HTML이 됩니다:

```handlebars
{{fa "solid" "print" "print-button"}}
```

```html
<span class=fa-svg id="print-button"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M448 192V77.25c0-8.49-3.37-16.62-9.37-22.63L393.37 9.37c-6-6-14.14-9.37-22.63-9.37H96C78.33 0 64 14.33 64 32v160c-35.35 0-64 28.65-64 64v112c0 8.84 7.16 16 16 16h48v96c0 17.67 14.33 32 32 32h320c17.67 0 32-14.33 32-32v-96h48c8.84 0 16-7.16 16-16V256c0-35.35-28.65-64-64-64zm-64 256H128v-96h256v96zm0-224H128V64h192v48c0 8.84 7.16 16 16 16h48v96zm48 72c-13.25 0-24-10.75-24-24 0-13.26 10.75-24 24-24s24 10.74 24 24c0 13.25-10.75 24-24 24z"/></svg></span>
```
