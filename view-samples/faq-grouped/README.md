# Grouped FAQs

## Podsumowanie
This sample uses standard group rendering to provide a list of expandable questions. By default, when grouping by a column the column name and the count of grouped items will be included in the group name. This format provides some small tweaks to the group header to only show the value (question in this case). By also hiding the column header and item selection, this format acts like a mini application and could easily be added to a page using the list web part.

![zrzut ekranu próbki](./assets/screenshot.png)

This sample includes two variations: the original `faq-grouped.json` and `faq-grouped-full-width-answer.json`.
- **faq-grouped.json** – Applies formatting only to the group header. The width of the answer depends on the column width.
- **faq-grouped-full-width-answer.json** – Also includes a `rowFormatter` to style the entire row, allowing the answer to span the full width of the page. However, only the `Answer` column is shown; other columns are not displayed.

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Multiple line of text|Answer|Tak|

In this case, the Title column has been renamed to Question (though it doesn't make any difference to the format). The view is grouped by the Question (Title) column and then the Question column has been removed from display (so that the value doesn't repeat alongside the answer).

> FAQs - Stands for **F**requently **A**sked **Q**uestions

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
faq-grouped.json | [Chris Kent](https://github.com/thechriskent)
faq-grouped-full-width-answer.json | [Steve Corey](https://github.com/stevecorey365)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|15 kwietnia 2022|Wersja początkowa
1.1|11 sierpnia 2025|Added `faq-grouped-full-width-answer.json`

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/faq-grouped" />
