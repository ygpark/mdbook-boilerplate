# MathJax 지원

mdBook은 [MathJax](https://www.mathjax.org/)를 통한 수학 방정식에 대한 
선택적 지원을 제공합니다.

MathJax를 활성화하려면, `book.toml`의 `output.html` 섹션에 
`mathjax-support` 키를 추가해야 합니다.

```toml
[output.html]
mathjax-support = true
```

>**참고:** MathJax가 일반적으로 사용하는 구분자는 아직 지원되지 않습니다. 
현재 `$$ ... $$`를 구분자로 사용할 수 없으며, `\[ ... \]` 구분자는 
작동하려면 추가 백슬래시가 필요합니다. 이 제한사항이 곧 해제되기를 바랍니다.

>**참고:** MathJax 블록에서 이중 백슬래시를 사용할 때 (예: 
> `\begin{cases} \frac 1 2 \\ \frac 3 4 \end{cases}` 같은 명령어에서) 
> _두 개의 추가_ 백슬래시를 추가해야 합니다 (예: `\begin{cases} \frac 1 2 \\\\ \frac 3 4 
> \end{cases}`).


### 인라인 방정식
인라인 방정식은 `\\(`와 `\\)`로 구분됩니다. 예를 들어, 다음 인라인 방정식 
\\( \int x dx = \frac{x^2}{2} + C \\)을 렌더링하려면 다음과 같이 작성합니다:
```
\\( \int x dx = \frac{x^2}{2} + C \\)
```

### 블록 방정식
블록 방정식은 `\\[`와 `\\]`로 구분됩니다. 다음 방정식을 렌더링하려면

\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]


다음과 같이 작성합니다:

```bash
\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]
```
