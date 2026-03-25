# File Thumbnails or Hyperlinks

## Podsumowanie
This example uses a column to generate a hyperlink to the Item Thumbnail for a document library.
* Uses FileRef Variable
* Uses getpreview.ashx

### Before you use generic-hyperlink-thumbnail
* Adjust the resolution=**3** (0-6) value to your NEEDS. _(3: 1024px, 4: 1600px)_

![zrzut ekranu próbki](./assets/screenshot.png)

### generic-image-thumbnail 
basics from: https://github.com/pnp/List-Formatting/tree/master/column-samples/picture-roundimage-format

* Adjust Thumbnail Sizes or Rounded Edges to your NEEDS. 

![zrzut ekranu próbki](./assets/screenshot2.png)


## Wymagania widoku
- Ten format można zastosować do any column type (the value is ignored)
- This format should be used in a Document Library

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-hyperlink-thumbnail.json | [Josef Lahmer](https://github.com/josy1024)
generic-image-thumbnail.json | [Josef Lahmer](https://github.com/josy1024)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|lipca 17, 2018 |Wersja początkowa
1.1|20 sierpnia 2018|Przełączono na wyrażenia w stylu Excela
1.2|9 stycznia 2019|Removed hardcoded url and replaced with @currentWeb token
1.3|9 kwietnia 2019|Bug fix in @currentWeb, + generic-image-thumbnail

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

> Dodatkowa wersja wykorzystująca Abstract Tree Syntax (AST) jest również dostępna dla środowisk, w których wyrażenia w stylu Excela nie są obsługiwane.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-hyperlink-thumbnail" />
