# Menu Link Tiles

## Podsumowanie
This sample includes a Metro tiles style menu with additional features such us configuration of tiles using **size** and **color**, option to **favorite** a tile using `setValue`, and also includes `customCardProps` to show a custom hover card with the **description** of a tile.

![zrzut ekranu próbki](./assets/screenshot.gif)

> This format uses the icon `AddFavorite` combined with `"action": "setValue"` to update an item and reorganizes Tiles in the view when ordered by `Modified`. 

![Menu Tile configuration](./assets/screenshot2.gif)

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
Description | Multiple line of text 
Color | Pojedyncza linia tekstu - Select one of this pre defined case-sensitive colors - (**empty/null, Green, Red, CyanBlue, Gray, MagentaPink, Orange, OrangeYellow**).
icon | Pojedyncza linia tekstu
URL | Hiperłącze 
NewTab | Yes/No - This field is used to open the link the same tab or new tab
Small | Yes/No - Used to define the size of Tile.
OrderData | Data & Time - this field will be used to update item to order tile.

### Edit View requirements

- Sort by the `Modified` column in descending order

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
menu-link-tiles.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|03 grudnia 2021|Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/menu-link-tiles" />
