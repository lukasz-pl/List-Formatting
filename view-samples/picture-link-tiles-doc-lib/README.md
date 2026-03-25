# Picture Link Tiles Doc Lib

## Podsumowanie
This sample turns each item into a card-style tile view in a SharePoint Document Library.

## picture-link-tiles-doc-lib.json
Key features:
* Shows a file preview thumbnail. If a URL exists, clicking the preview opens the URL, otherwise, it opens the current file.
* Displays a Category | Topic badge on the top left, inline editable.
* Shows a Rank badge on the top right with background color based on value: >89 dark red, >79 dark blue, >49 dark green, else gray. Also inline editable.
* Displays the Title as an overlay, hidden if HideTitle is true or Title is empty. Also inline editable.
* Includes a footer with a delete button, source, published date, and an edit button.
* Changes the footer’s background color based on the category: Sample purple, News red, Blog orange, else dark blue.
> [!NOTE]
> All columns must be included in the gallery view and an additional internal column name `Type` for checking folder.

![Zrzut ekranu the sample](./assets/screenshot.png)

## picture-link-tiles-doc-lib-minimal.json
This sample displays card-style tiles grouped by category, with a basic click-to-open feature.

> [!NOTE]
> `Title` and `URL` columns must be included in the gallery view and an additional internal column name `Type`.

![sample screenshot](./assets/minimal.png)

## Wymagania widoku
Column Name         | Type                   | Setting
--------------------|------------------------|-
Title               | Pojedyncza linia tekstu    |
URL                 | Hiperłącze              |
PublishedData       | Data i godzina          | Data only
Source              | Choice                 | Allow multiple selections = Yes
Category            | Choice                 | Sample, News, Blog,...
Topic               | Choice                 |
Rank                | Liczba                 | Liczba of decimal places = 0
HideTitle           | Yes/No                 | Default value = No

![field mapping screenshot](./assets/field-mapping.png)


## Próbka
Rozwiązanie|Autor(zy)
--------|---------
picture-link-tiles-doc-lib.json | [Watana](https://github.com/watana2)
picture-link-tiles-doc-lib-minimal.json | [Watana](https://github.com/watana2)


## Historia wersji
Wersja|Data|Uwagi
-------|----|-
1.0    | września 24, 2025 | Wersja początkowa.
1.1    |   października 25, 2025 | Added folder handling functionality.

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/picture-link-tiles-doc-lib"/>