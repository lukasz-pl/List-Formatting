# Message Chat Bubbles

## Podsumowanie
This sample formats your SharePoint list view to look like message chat bubbles! If the `Author` is the current user, the message will be displayed on the right.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title||
|Multi line of text|Message|Tak|
|Person|Author|Tak|
|DataTime|Created|Tak|

* Show the default column `Author` and `Created` column in the view.
* If you want to display the latest messages at the top, please sort them in descending order by `Created`.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
message-chat-bubbles.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Version |Data              |Uwagi
--------|------------------|--------
1.0     |listopada 19, 2020 |Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/message-chat-bubbles" />
