# RYG Status

## Podsumowanie

A status column is evaluated to provide colors corresponding to status. This format uses the values Red, Yellow, Green, and Amber but you could easily extend this to fit your own color-coded system by adding or removing nested conditions.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
The format expects the following field:

Field |Type
--------|---------
Status | Pojedyncza linia tekstu / Choice

> To use a lookup column instead, replace all occurences of [$internalfieldname] with  [$internalfieldname.lookupValue].

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
ryg-status-rowclass.json | [S Merchant](https://github.com/sohailmerchant)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|Septmeber 9, 2018|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/ryg-status-rowclass" />
