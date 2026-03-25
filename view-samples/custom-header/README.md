# Custom Header

## Podsumowanie
Sometimes it is necessary to remove the standard headers. In those cases, you may still want to show a custom header. This sample demonstrates creating a custom header and only showing it on the first row. The key to this technique is setting the `display` style attribute to `none` (hidden) whenever the `@rowIndex` is not 0 (first row).

![zrzut ekranu próbki](./assets/screenshot.png)

Creating a custom header removes the standard features such as menus, sorting, moving, resizing, etc. In addition, the sticky header feature is now gone. So an additional sample, custom-header-repeating-format.json is provided that demonstrates drawing the custom header every 30 rows.

![screenshot repeating](./assets/screenshotRepeating.png)

## Wymagania widoku
The concept can be adjusted for any view, but this specific format expects the following columns to be part of the view:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Data|Deployed|Tak|
|Yes/No|Active|Tak|

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
custom-header.json | [Chris Kent](https://github.com/thechriskent)
custom-header-repeating.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|20 lutego 2020|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi


<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/custom-header" />
