# Demote News to Site Page | Promote Site Page to News

## Podsumowanie
In the Site Pages library, there is a Promoted State column. Depending on the value stored in this column, you can identify whether it is a site page or a news page. The correspondence between the value and page type is as follows.

Promoted State |Page Type
---------------|---------------------------
0              |Site page
1              |News page not yet published
2              |News page

Once a page is created as news page, it cannot be demoted to a site page under normal circumstances.

Ta próbka pokazuje how to use the setValue action to update the value of the Promoted State column to 0 and demote the news page to a site page.

![zrzut ekranu próbki](./assets/screenshot.gif)

After demoting it, please republish it. Otherwise, view-only users will not reflect the change and the page will remain displayed as a news page.

![zrzut ekranu how to republish](./assets/republish.png)

## Wymagania wstępne
The Promoted State column needs to be displayed in the view. Poniższe is how to display it.

1. Click any column.
2. Hover **Column Settings**
3. Click **Show/hide Columns**
4. Check **Promoted State**
5. Click **Apply**

![screenshot to show the promoted state](./assets/display_promotedstate.png)

## Wymagania widoku
Ten format można zastosować do a Promoted State column.

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
promotedstate-demote-news.json | [Tetsuya Kawahara](https://github.com/tecchan1107) & [Cory Schwartz](https://github.com/Schwartzyy55)

## Historia wersji

Wersja |Data              |Uwagi
--------|------------------|--------
1.0     |grudnia 11, 2021 |Wersja początkowa
1.1     |stycznia 2, 2024   |Dodano ability to promote back into page
1.2     |stycznia 6, 2024   |Poprawiono the more icon not to wrap

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/promotedstate-demote-news" />
