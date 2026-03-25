# Links to Search Page

## Podsumowanie

This sample demonstrates displaying links to the search page. When you open the search page, it displays the search results where the query registered in the `Query` column of the item has been executed. Also, there are two types of links, each with a different search scope. One is for the entire tenant, and the other is for within the site.

![zrzut ekranu próbki](./assets/screenshot.png)

You can also add search keywords on the search page to further refine your search results.

![zrzut ekranu the search result](./assets/search-result.png)

In addition, there is a favorite feature using the `setValue` action.

![zrzut ekranu the favorite feature](./assets/favorite.png)

In addition to a view that shows all items, it is useful to create a view that displays only the items you have added to your favorites.

![zrzut ekranu the my favorites view](./assets/my-favorites-view.png)

## Wymagania widoku

|Type                         |Internal Name|Wymagane|
|-----------------------------|-------------|:------:|
|Pojedyncza linia tekstu          |Title        |Yes     |
|Pojedyncza linia tekstu          |Query        |Yes     |
|Pojedyncza linia tekstu or Choice|Category     |Yes     |
|Pojedyncza linia tekstu          |Icon         |Yes     |
|Multi-Select Person          |Favorites    |        |

- Set the icon name of [Fluent UI Icons](https://developer.microsoft.com/fluentui#/styles/web/icons) in the `Icon` column.
- You need to use Gallery view grouped by `Category` column

### Próbka Data

- You can view [sample data (CSV file)](./assets/sample-data.csv).
- When using the Excel import and CSV import functions, the internal names of the columns are "field_" + "sequential number" like field_1, field_2. And these internal names of columns are not used in the sample JSON. Therefore, please note that the sample JSON cannot be used as it is when using the Excel import and CSV import functions.
    ![zrzut ekranu internal name of column when Excel import and CSV imported](./assets/excel-csv-import.png)
- As of sierpnia 15, 2023, the gallery view is not available when [exporting from Excel to SharePoint](https://support.microsoft.com/office/export-an-excel-table-to-sharepoint-974544f9-94bc-4aa8-9159-97282d256dab). Please note this as well.  
Related Link: [Export an Excel table to SharePoint: gallery view layout not available · Issue #8811 · SharePoint/sp-dev-docs](https://github.com/SharePoint/sp-dev-docs/issues/8811)
- If you want to import the sample data into your list, I recommend downloading the CSV file of the sample data, opening it in Excel, copying a range of all the data, and pasting it in using Edit Grid View.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
search-page-link-tiles.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Version |Data            |Uwagi
--------|----------------|--------------------------------
1.0     |sierpnia 15, 2023 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- This sample was inspired by [Ai Hirano's post](https://x.com/ai_yamasaki/status/1545353487533232130).
- The following documents describe the managed property and the search query.
  - [Manage the search schema in SharePoint | Microsoft Learn](https://learn.microsoft.com/sharepoint/manage-search-schema)
  - [Keyword Query Language (KQL) syntax reference | Microsoft Learn](https://learn.microsoft.com/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference)
- [SharePoint Search Query Tool](https://github.com/pnp/PnP-Tools/tree/master/Solutions/SharePoint.Search.QueryTool) allows you to see what values are set for which managed properties, which is very helpful when building a query.
- Using [PnP Modern Search](https://microsoft-search.github.io/pnp-modern-search/), you can place search-related web parts on the page.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/search-page-link-tiles" />
