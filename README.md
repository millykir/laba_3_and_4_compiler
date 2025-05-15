# 📐 Форматирование числа в научную нотацию на Python

## 📌 Постановка задачи

В данной работе рассматривается форматирование числа с плавающей точкой в **научную (экспоненциальную) нотацию** на языке **Python**. Пример использования:

```python
scientific_format = "{:.3e}".format(512349000.000000)
```

🔹 Где `"{:.3e}"` — форматная строка, указывающая, что число нужно представить в научной форме с **тремя знаками после запятой**.
🔹 `.format(512349000.000000)` — передаваемое число, которое будет отформатировано.

---

## 🧬 Разработка грамматики

Грамматика **G\[Z]** определяет синтаксис выражения форматирования. Ниже представлены правила продукций:

```
1) <START>                → indicator_symb <VARREM>
2) <VARREM>               → symb <VARREM>
3) <VARREM>               → '=' <QUOTE1>
4) <QUOTE1>               → '"' <LBRACE>
5) <LBRACE>               → '{' <COLON>
6) <COLON>                → ':' <DOT>
7) <DOT>                  → '.' <DIGITBEFOREEXP>
8) <DIGITBEFOREEXP>       → digit <DIGITBEFOREEXPREM>
9) <DIGITBEFOREEXPREM>    → digit <DIGITBEFOREEXPREM>
10) <DIGITBEFOREEXPREM>   → 'e' <RBRACE>
11) <RBRACE>              → '}' <QUOTE2>
12) <QUOTE2>              → '"' <DOT2>
13) <DOT2>                → '.' <FORMAT>
14) <FORMAT>              → 'format' <OPEN_PAREN>
15) <OPEN_PAREN>          → '(' <SIGN>
16) <OPEN_PAREN>          → digit <INTREM>
17) <SIGN>                → ‘-’ <INT>
18) <SIGN>                → ‘+’ <INT>
19) <INT>                 → digit <INTREM>
20) <INTREM>              → digit <INTREM>
21) <INTREM>              → ')' <SEMICOLON>
22) <INTREM>              → '.' <DECIMAL>
23) <DECIMAL>             → digit <DECIMALREM>
24) <DECIMALREM>          → digit <DECIMALREM>
25) <DECIMALREM>          → ')' <SEMICOLON>
26) <SEMICOLON>           → ';'
```

### 🔠 Терминальные и нетерминальные символы:

* `digit → 0|1|2|...|9`
* `indicator_symb → a|...|z | A|...|Z | '_'`
* `symb → a|...|z | A|...|Z | '_' | 0–9`

**Нетерминальные символы (V<sub>n</sub>)**:

```
<START>, <VARREM>, <QUOTE1>, <LBRACE>, <COLON>, <DOT>,
<DIGITBEFOREEXP>, <DIGITBEFOREEXPREM>, <RBRACE>, <QUOTE2>,
<DOT2>, <FORMAT>, <OPEN_PAREN>, <SIGN>, <INT>, <INTREM>,
<DECIMAL>, <DECIMALREM>, <SEMICOLON>
```

**Терминальные символы (V<sub>t</sub>)**:

```
a–z, A–Z, 0–9, '_', '=', '"', '{', ':', '.', 'e', '}', 
'(', ')', ';', 'format', '+', '-'
```

---

## 🧮 Метод анализа

Грамматика `G[Z]` является **автоматной** и может быть представлена в виде графа.
На графе:

* **Сплошные стрелки** обозначают синтаксически верные переходы.
* **Пунктирные стрелки** — состояния ошибок (`ERROR`).
* **Лямбда-дуги** (λ) и непомеченные дуги — любой терминал, отличный от ожидаемого в узле.



📌 *См. рисунок 1: граф переходов (вставьте изображение схемы).*

---

## 🧪 Тестовые примеры



---
