# Out of Office

## Podsumowanie
This sample shows how to format a list to show upcoming employee time away from office. It features the following:
- Responsive layout through flexbox
- Conditionally showing a today icon if the out of office overlaps the current date
- Conditionally changing the text which shows based on if the out of office start date is the current date
- Use of theme color classes to ensure the format displays as intended regardless of theme (light, dark, custom, etc.)

![zrzut ekranu próbki](./assets/screenshot.png)

> This sample is derived from the [birthdays](../birthdays) sample.

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Person|Who|Tak|
|Data Time|Startdate|Tak|
|Data Time|Enddate|Nie|

This sample relies on having a View set up which filters to only show items where either the Start date or the End date is greater than or equal to the current date. Make sure to apply the necessary filters in your view for this to work:

![View Filter](./assets/ViewFilter.png)

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
out-of-office.json | [Tom Resing](https://github.com/tomresing)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|maja 14, 2021 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/out-of-office" />
