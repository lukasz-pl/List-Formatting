# Social Media Profile Pics

## Podsumowanie

Using the social media handles supported by https://unavatar.now.sh, social media profile pictures are displayed in a circle and clicking them will open the user's social media page in a new window. The handle is also displayed as a tooltip when hovering over the profile image.

![zrzut ekranu próbki](./assets/screenshot.png)

> Note: https://unavatar.now.sh currently supports a variety of services including Twitter, Facebook, Instagram and GitHub.

### Typy kolumn
Ten format będzie działać z Choice and Text columns without any changes. To use Lookup columns, you'll need to change the 2 occurences of `@currentField` to `@currentField.lookupValue`.

The field values are case insensitve and should be just the user's twitter handle with no @.

## Wymagania widoku
Ten format powinien być zastosowany do a text based column containing the username for a given social network. Widok powinien zawierać następujące pola:

|Type                 |Internal Name  |Wymagane|
|---------------------|---------------|:------:|
|Choice               |SocialNetwork  |Yes     |
|Pojedyncza linia tekstu  |SocialPic      |Yes      |

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-socialpic.json | [David Warner II](https://github.com/PopWarner)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|21 lipca 2018|Wersja początkowa
1.1|20 sierpnia 2018|Zaktualizowano do użycia wyrażeń w stylu Excela
1.2|20 sierpnia 2020|Updated to use the unavatar service for profile picture

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

Podobny kreator znajduje się także w webparcie [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md), który pozwala na pełne dostosowanie.

- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

> Dodatkowa wersja wykorzystująca Abstract Tree Syntax (AST) jest również dostępna dla środowisk, w których wyrażenia w stylu Excela nie są obsługiwane.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-socialpic" />
