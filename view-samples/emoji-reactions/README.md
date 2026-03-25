# Emoji Reactions

## Podsumowanie

This sample demonstrates reacting with an emoji. Who reacted and the total counts per reaction are stored with the list item.

Two versions are provided. The first, emoji-reactions.json, displays the reactions of the current user and allows them to react. The section, emoji-reactions-count.json, displays reactions from all users and the count of each reaction type.

![zrzut ekranu próbki](./assets/screenshot.png)

### emoji-reactions-count.json

![emotions format](./assets/screenshotCount.png)

  - Below provides how the counting board is organized by users.

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
Emotion | Multiple line of text - Stores reactions for users
EmotionCount | Pojedyncza linia tekstu  - Stores count of reactions

Here's how the storage looks behind the scenes:

![storage](./assets/UnformattedColumns.png)

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
emoji-reactions.json | [André Lage](https://github.com/aaclage)
emoji-reactions-count.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|12 stycznia 2022|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/emoji-reactions" />
