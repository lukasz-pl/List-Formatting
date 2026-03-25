# Bookmarks

## Podsumowanie
This sample shows how to create SharePoint page bookmarks using list items with custom JSON formatting, inspired by [João Ferreira's post](https://sharepoint.handsontek.net/2024/10/14/create-custom-vertical-navigation-sharepoint-pages/).

**Features:**
1. Navigate to specific sections of a SharePoint page using heading styles (H2, H3,...) to generate anchor links
2. Open external links in a new tab (e.g https://google.com)
3. Group and filter content by category

![zrzut ekranu próbki](./assets/bookmarks-list.png)

![zrzut ekranu próbki](./assets/screenshot.png)


## Wymagania widoku
Column Name|Wymagane|Type
-----------|--------|-
Title      | Yes    | Text
Category   | Yes    | Choice
Link       | Yes    | Hiperłącze


> [!NOTE]
> It is necessary to group the view by the `Category` column.


## Próbka

Rozwiązanie|Autor(zy)
--------|---------
bookmarks.json | [Watana](https://github.com/watana2)


## Historia wersji
Wersja|Data|Uwagi
-------|----|-
1.0    | czerwca 22, 2025 | Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/bookmarks" />
