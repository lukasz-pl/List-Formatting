# Hide All Buttons on Command Bar

## Podsumowanie
Hide everything that can be hidden on the command bar. My use case was to embed a summary into a SharePoint page using an iFrame and keep things as clean as possible.

SharePoint Lists
![zrzut ekranu próbki](./assets/screenshot.png)

SharePoint Document Library
![SharePoint Document Library](./assets/document-library.png)


## Wymagania widoku
- You'll want this to be it's own list view, so the hidden buttons aren't more difficult to access when you actually need them.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
commandbar-hide-all.json | [gitjego](https://github.com/gitjego) & [Watana](https://github.com/watana2)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|24 grudnia 2024|Wersja początkowa
1.1|3 maja 2025|Added/updated command bar props/images
1.2|28 czerwca 2025|Added `PublishCommand`, `properties`
1.3|13 stycznia 2026|Added `syntexAutofillColumnsCommandPublicKey`

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
The buttons to be hidden must be explicitly named, and it is likely that there will be new buttons that need to be hidden in new releases from Microsoft. This code currently hides everything listed in Microsoft's [Documentation](https://learn.microsoft.com/sharepoint/dev/declarative-customization/view-commandbar-formatting). Refer to this if you are seeing commands not be hidden, and add a line as needed.
If you can find a way to hide the viewSelector, please pull request.  :)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/commandbar-hide-all" />
