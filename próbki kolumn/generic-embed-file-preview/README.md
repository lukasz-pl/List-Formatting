# File Preview Callout with the `embed` Action

## Podsumowanie

Ta próbka pokazuje how to display a file preview from a document library or Site Pages inside a callout using the [embed](https://learn.microsoft.com/sharepoint/dev/declarative-customization/formatting-syntax-reference#customrowaction) action. This allows users to view file contents bez opuszczania bieżącej strony.

![zrzut ekranu próbki](./assets/screenshot.png)

Pages can also be previewed in a callout.

![screenshot of a Site Pages page preview in a callout](./assets/screenshot-site-pages.png)

> [!WARNING]
> Support for the `embed` action in Site Pages may not yet be available in some tenants as of October 2, 2025, so page previews might not work in those environments.

## Wymagania wstępne

To embed content, the domain of the SharePoint site (e.g., `contoso.sharepoint.com`) must be allowed for embedding. For guidance on how to allow embedding, please refer to [Allow or restrict the ability to embed content on SharePoint Lists using custom formatters](https://go.microsoft.com/fwlink/p/?linkid=2258033).

![screenshot of HTML field security settings](./assets/html-field-security.png)

If you attempt to embed content from a domain that is not allowed, the following error screen will appear:

![screenshot of the error screen when target site is not allowed to embed](./assets/not-allowed-screen.png)

## Wymagania widoku

- This format is designed for use with document libraries and Site Pages.
- Ten format można zastosować do any column type.

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-embed-file-preview.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Wersja |Data         |Uwagi
--------|-------------|--------
1.0     |June 30, 2025|Wersja początkowa
1.1     |October 2, 2025|Extended to support page (aspx) previews

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- This sample was created with reference to the [generic-file-preview](../generic-file-preview/).
- Not all file extensions have been tested for preview, so some file types may not be supported for display.
- The embedded view uses query strings such as `?env=WebView`. For more details, see [Query String URL Tricks for SharePoint and Microsoft 365](https://learn.microsoft.com/microsoft-365/community/query-string-url-tricks-sharepoint-m365).

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-embed-file-preview" />