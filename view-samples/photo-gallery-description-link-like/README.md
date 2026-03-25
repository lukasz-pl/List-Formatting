# Photo Gallery with Description, Link and Likes

## Podsumowanie

This sample demonstrates formatting a document library gallery view into a photo gallery showing title, description, hyperlink and likes.

![zrzut ekranu próbki](./assets/screenshot.png)

Credit to original author [Lou-i3](https://github.com/Lou-i3), I have copied and modified [photo-gallery-with-likes.json](https://github.com/pnp/List-Formatting/tree/master/view-samples/photo-gallery-with-likes) to give another variant option.

## Wymagania widoku

The view must be set to gallery. Use a category column to filter your view so the list can house multiple categories for display purposes.  
This format expects the following columns to be part of the view:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|No
|Wiele linii tekstu|Description|No
|Hiperłącze or Picture|Image|No
|Hiperłącze or Picture|Link|No
|Choice|Category|No
|Liczba|LikesTotal|No
|Multi-Person|LikedBy|No

> [!NOTE]
> When using an external image URL in the `Image` column, the image might not appear if it's retrieved from a domain that isn't allowed. Please make sure to configure the HTML Field Security settings when using external images. For more information, see [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b).

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
photo-gallery-description-link-like.json | [AngelaTS](https://github.com/AngelaTS)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|4 listopada 2025|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/photo-gallery-with-likes-and-description" />
