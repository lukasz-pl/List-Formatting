# Picture Quick Links

## Podsumowanie
This sample shows custom quick links for adding to a vertical section in a SharePoint page.

Images are stored in a central location, so updating an image automatically updates it everywhere it's used. This is especially useful for large companies with many divisions and departments.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

- The view must be set to gallery.
- This format expects the following columns to be part of the view:

    Field Name | Wymagane | Type
    ---------- | -------- | ----
    Link | Yes | Hiperłącze or Picture (Format URL as: Hiperłącze)
    Picture | Yes | Hiperłącze or Picture (Format URL as: Picture)

> [!NOTE]
> - The hyperlink column format cannot be set to Picture in the modern column create or edit pane.  
>     ![zrzut ekranu the create column pane](./assets/create-column-pane.png)
> 
>     To set the hyperlink column format to Picture, you must do so from the classic create or edit column screen.  
>     ![steps to open the edit column screen](./assets/edit-column-screen.png)
> 
> - When setting an external site's image URL in the `Picture` column, the image may not be displayed. This happens when attempting to retrieve images from a domain that is not allowed. To enable image display, you'll need to configure the HTML Field Security settings. For more details, refer to [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b).

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
picture-quick-links.json | [Watana](https://github.com/watana2)
picture-quick-links-compact.json | [Watana](https://github.com/watana2)
picture-quick-links-compact-purple.json | [Watana](https://github.com/watana2)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|16 września 2024|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

If you create a list view and apply [hyperlink-display-url](/column-samples/hyperlink-display-url) to format the `Link` or `Picture` columns, you can display the URLs set in the hyperlink column on the view, making it easier to check the link destinations and manage maintenance.

![zrzut ekranu the list with hyperlink-display-url applied](./assets/hyperlink-display-url.png)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/picture-quick-links" />
