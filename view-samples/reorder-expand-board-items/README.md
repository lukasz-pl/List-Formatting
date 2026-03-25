# Reorder and Expand Board Items

## Podsumowanie
This sample allow users to manage card order in Board Views and also enables expanding and collapsing images. This sample has the option "**Move to Top**" that allows users to move cards to the top of the board view as a way to rearrange card positions.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
Category | Choice - Include the following options **"Started,Pending,Completed"**
Order | Pojedyncza linia tekstu   - Manage the order of cards
Image | Pojedyncza linia tekstu   - This field allow to include url to image.
Expand | Yes/No - default value **"No"**

### Create Board View

- Access to View dropdown and select "**Create new view**"
- Add new Name and select option "**Board**"

### Edit List View requirements

- Access to List Settings > access to "**Views**" area and select created view.
- Edit View where format will be included:
   - Access to "**Sort**" Area and select column "**Order**" and check as **descending order**, this option order the cards based on changed.


## Próbka

Rozwiązanie|Autor(zy)
--------|---------
reorder-expand-board-items.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|15 lutego 2022|Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/reorder-expand-board-items" />
