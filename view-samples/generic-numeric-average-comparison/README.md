# Numeric Average Comparison

## Podsumowanie
Provides an example of comparing numeric values across time periods. In this example, we are using grades for students across 4 quarters, though the principle can be applied to any repetitive numeric values.

The View Formatting definition calculates the average of the current and prior quarters numeric grades. The current quarter numeric grade and the average of the previous quarters is displayed. (Example: Quarter 3 calculates the average of quarter 1, 2 & 3)

In addition to the numeric average calculation displayed within each quarter, this example also illustrates how the average value in each quarter can be used to assign additional labels, such as the Student Grade. (Example: A,B,C,D,F)

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Pojedyncza linia tekstu|StudentName|Nie|
|Liczba|Q1NumericGrade|Tak|
|Liczba|Q2NumericGrade|Tak|
|Liczba|Q3NumericGrade|Tak|
|Liczba|Q4NumericGrade|Tak|

![Unformatted View](./assets/screenshotUnformatted.png)

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
generic-numeric-average-comparison.json | [David Warner II](https://github.com/PopWarner)


## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|7 listopada 2018|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

Using the `customRowAction` with an `action` of `defaultClick` creates a great way to make your list into a master view with details easily accessible. This sample wraps the entire row in a button so that you can click anywhere in the row to open the information panel for the item:



<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/generic-numeric-average-comparison" />
