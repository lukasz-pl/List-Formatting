# Gauge Aggregate Footer

## Podsumowanie

This sample shows a gauge in the list footer (when aggregates are enabled).

![Zrzut ekranu the sample](./assets/screenshot.png)


## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Liczba|any|Tak|

This format can be applied to any list where a column has an aggregate function (ie sum, average, etc.).

The format assumes a value between 0 and 10 (and is converting to a percentage). To change the total, you can do a find and replace to change the expression. For instance you can find all instances of `(@columnAggregate.value)/10` and replace with `(@columnAggregate.value)/100` if the range is 0-100. If using a number stored as a percent you can simply replace the `(@columnAggregate.value)/10` with `@columnAggregate.value`.

> By default, this format will be applied to ALL aggregate columns. To filter only to a specific field, add a check for the `@columnAggregate.columnDisplayName` and hide accordingly.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
gauge-aggregate-footer.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|4 kwietnia 2022|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/gauge-aggregate-footer" />
