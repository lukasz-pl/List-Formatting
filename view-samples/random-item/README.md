# Random Item

## Podsumowanie
This sample demonstrates utilizing layering to draw all rows on top of each other and then the z-index is set to a randomized value to determine which row to draw on the very top.

The trick is that the z-index is set using the `@now` parameter with a modulo operator against the total number of items (7). This number should be updated to match the number of items in the list you are trying to display. However, it can also be dynamic by setting this to a relatively high number.

![zrzut ekranu próbki](./assets/screenshot.gif)

In the above use case, this format has been used to display a random turkey fact! This can easily be added to a page using the list web part and will act as a miniature application.

![zrzut ekranu the sample on a page](./assets/screenshotOnPage.png)

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Multiple line of text|Details|Tak|
|Image|Image|Yes

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
random-item.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|15 kwietnia 2022|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/random-item" />
