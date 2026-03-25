# Staff Rota Shifts with CSS Table

## Podsumowanie
This sample demonstrates creating a Rota Shifts table using CSS Table layout by using `rowFormatter` to customise the entire display of a row. The aim is to demonstrate the following concepts:
- using a CSS table layout (`"display": "table"`, `"display": "table-row"`, `"display": "table-cell"`)
- using Fluent UI classes for font sizing, font color and background color
  - specifically the theme color class to ensure display matches the theme of the site (`ms-bgColor-themePrimary`)
- disabling selection (`hideSelection`)
- hiding column headers (`hideColumnHeader`)
- using `join` and `\n` to join choice column values on separate lines

![zrzut ekranu próbki](./assets/screenshot.png)

## View Requirements

Included in the sample is a site script that will create the list as needed. However if you prefer to create the list yourself here are the fields needed:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Nie|
|Multi-Choice|Shift1|Nie|
|Multi-Choice|Shift2|Nie|
|Multi-Choice|Shift3|Nie|
|Pojedyncza linia tekstu|Data|Nie|

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
rota-css-table.json | [Ariel Kropp](https://github.com/arielkropp)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|07 marca 2019|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/rota-css-table" />
