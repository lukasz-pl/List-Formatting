# Custom Share to Teams

## Podsumowanie
Sometimes you might need a more specialised "Share to Teams" option - this one allows for sharing a short synopsis & URL!

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania widoku
- Sample is applied to a calculated column type (formula `=""`)

Nazwa kolumny|Typ|Notes
--------|---------|--------
ShareMessage|Text|Limit to 200 characters
URL|Wiele linii tekstu|Link will only parse 1 parameter, any more will be assumed to be part of the request to Teams

- Instead of the extra columns, you could hardcode the share url by replacing the `[$ShareMessage]` and `[$URL]` content in the attached format


## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-share-to-teams-with-message.json | [Bianca W](https://github.com/bianca-git)


## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|15 października 2023|Wersja początkowa

## Dodatkowe uwagi

This solution was originally designed to be part of a bigger view, and has been re-designed for sharing with the community.


## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-share-to-teams-with-message" />
