# Risk Score Indicator

## Podsumowanie
A number column is evaluated against tiers of values to provide colors corresponding to score ranges. 

![zrzut ekranu próbki](./assets/screenshot.png)

A number column is evaluated against tiers of values to provide colors corresponding to score ranges. This format provides 4 ranges:

|Range|Color|
|---|---|
|value >= 16|Red|
|16 > value >= 12|OrangeLighter|
|12 > value >= 8|Yellow|
|value < 8|Green|

You can easily adjust the values/colors to provide your own ranges. You can also add or remove nested conditions to increase or decrease the number of ranges needed.

## Wymagania widoku
The format expects the following fields:

Field |Type
--------|---------
Score | Liczba

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
risk-score-rowclass.json | [S Merchant](https://github.com/sohailmerchant)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|Septmeber 9, 2018|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/risk-score-rowclass" />
