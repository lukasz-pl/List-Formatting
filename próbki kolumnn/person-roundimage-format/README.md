# Display a Person's Profile Picture in a Circle

## Podsumowanie
Ta próbka stosuje styles to a parent `div` element and a child `img` element to show a person's profile picture in a circle.

The size can be easily adjusted by changing the default value of `32px` for both the `width` and `height` style attributes on the parent div.

Możesz również adjust the `border-radius` value of the parent div to change it from a full circle (_50%_) to a rounded rectangle (_< 50%_). To get larger profile pictures you can change the `size=S` portion of the URL to use either `size=M` or `size=L`. See the table below for details on image size.

For best results, images should be square (S & M user profile pictures always are).

![zrzut ekranu próbki](./assets/screenshot.png)

### Rozmiary obrazów profilowych użytkownika

|Key|Size|
|:---:|:---:|
|S|48x48|
|M|72x72|
|L|300x?*|

The L size profile pictures maintain the ratio of the original photo which means they are not guaranteed to be square. Neither are they guaranteed to be 300px wide. The maximum width will be 300px but if the original image was smaller than that, then it will be the original size. Even the placeholder image for the L size is only 250x150.

Overall, however, the L size shouldn't be used inside columns not only because the ratio is not guaranteed, but because the default column width won't allow you to take up that much space.

> Uwaga: `@currentField.picture` może zostać użyte do pobrania zdjęcia profilowego bezpośrednio z kolumny osoby. W tym podejściu opcje rozmiaru nie są jednak dostępne.

## Wymagania widoku
- Ten format można zastosować do a Person column

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
person-roundimage-format.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|21 marca 2018|Wersja początkowa
1.1|20 sierpnia 2018|Switched to Excel-style expression

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
Ten szablon jest dołączony do webpartu [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md).

- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

> Dodatkowa wersja wykorzystująca Abstract Tree Syntax (AST) jest również dostępna dla środowisk, w których wyrażenia w stylu Excela nie są obsługiwane.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/person-roundimage-format" />
