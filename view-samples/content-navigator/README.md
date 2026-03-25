# Content Navigator

## Podsumowanie
This sample demonstrates the use of the `id` attribute to create linkable anchors. The list is intended to have 2 views (Content and Links) using the 2 view formats supplied. Each view can be added to a page as a separate list webpart. No connections are required. Clicking on an item in the links view webpart will navigate to the item in the content view webpart. Additionally, previous and next buttons are included in the content view for internal navigation.

![zrzut ekranu próbki](./assets/screenshot.gif)

The sample utilizes the `@rowIndex` magic string to generate the anchor links. This means that you can add additional items and the formats will continue to work as expected. The order is determined by the order of the views (which needs to be the same).

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Multiple line of text|Content|Tak|

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
content-navigator.json | [Chris Kent](https://github.com/thechriskent)
content-navigator-links.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|15 kwietnia 2022|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/content-navigator" />
