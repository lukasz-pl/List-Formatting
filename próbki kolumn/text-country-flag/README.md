# Country Flag

## Podsumowanie

Ta próbka pokazuje displaying the flag of the country selected in the single selection SharePoint choice column.

![zrzut ekranu próbki](./assets/screenshot.png)

The country flag is shown using the [FlagCDN - CDN & API of flags](https://flagcdn.com/) web site API. So, allow `flagcdn.com` domain in HTML Field Security settings of your SharePoint site by following this Microsoft official documentation: [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/en-us/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b).

Możesz znaleźć the list of countries used in this JSON sample at: [Countries](./assets/countries.xlsx)

Add list of countries in the choice column settings like:

![screenshot of the edit column](./assets/edit-column.png)

## Wymagania widoku

- Ten format można zastosować do any text based column but a single selection choice column is the intent

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
text-country-flag.json | [Ganesh Sanap](https://github.com/ganesh-sanap)

## Historia wersji

Wersja |Data          |Uwagi
--------|--------------|--------
1.0     |August 28, 2023 |Wersja początkowa
1.1     |October 19, 2025 |Renamed from `choice-country-flag` to `text-country-flag`

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/text-country-flag" />