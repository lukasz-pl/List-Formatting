# Menu Link Button

## Podsumowanie

This sample has been inspired by [menu-link-tiles](https://github.com/pnp/List-Formatting/tree/master/view-samples/menu-link-tiles) by [André Lage](https://github.com/aaclage). It includes a Button style menu similar to Quick Links Button style with additional features such as using **width** , **height**, **color** and **fontColor**, and also includes `customCardProps` to show a custom hover card with the **description** of a tile.

![zrzut ekranu próbki](./assets/screenshot.png)

Also, this sample is responsive.

![Quick Links Button Style ](./assets/screenshot.gif)

## Wymagania widoku

- The format expect the following fields:

|Typ|Nazwa wewnętrzna|Wymagane|Notes|
|---|---|:---:|---|
|Pojedyncza linia tekstu|Title|Tak| |
|Multiple line of text|Description|Nie| |
|Pojedyncza linia tekstu|BackgroundColor|Nie|Select one of this pre defined case-sensitive colors - (**empty/null, Green, Red, Cyan, CyanBlue, Gray, MagentaPink, BlueMagenta, Orange, OrangeYellow, RedOrange**). |
|Pojedyncza linia tekstu|FontColor|Nie|Set the HTML color code or color name (e.g. #CD5C5C, pink). If not set, the color is white.|
|Pojedyncza linia tekstu|Icon|Nie|Set the icon name for [Fluent UI Icons](https://developer.microsoft.com/fluentui#/styles/web/icons).|
|Hiperłącze|URL|Tak| |
|Yes/No|NewTab|Nie|This field is used to open the link the same tab or new tab.|
|Liczba|Width|Nie|If not set, the default width is set to 100px.|
|Liczba|Height|Nie|If not set, the default width is set to 40px.|

### Edit View requirements

- Sort by the `Modified` column in descending order

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
menu-link-button.json | [Reshmee Auckloo](https://github.com/reshmee011)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|03 maja 2023|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/menu-link-button" />
