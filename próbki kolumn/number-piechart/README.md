# Pie Chart

## Podsumowanie
This example renders whole pie in neutralLight with radius 50 and the number% (column value) as a slice of the pie in blue using `<svg>` with `<path>` tags. The number% displayed at the bottom of the pie in neutralPrimary.

The background and text colors are set using theme values by applying classes from the [Office UI Fabric](https://developer.microsoft.com/en-us/fabric#/styles/colors). Unfortunately, there is not a theme class for `fill` and so the pie is set to a specific value that will not update through theme switches and so should be chosen carefully. Both a light and dark theme are shown in the screenshot below.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
- Ten format można zastosować do a Number column

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
number-piechart.json | [Aaron Miao](https://github.com/aaronmi), [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|Dec 13, 2017|Wersja początkowa
1.1|March 20, 2018|Dodano min & max values and fixed skewed drawing issue
1.2|August 20, 2018|Switched to Excel-style expressions and use of theme classes

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

A similar wizard is also included in the [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md) webpart that allows full customization.

> An additional version using Abstract Tree Syntax (AST) is also provided for environments where the Excel-style expressions are not supported.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/number-piechart" />
