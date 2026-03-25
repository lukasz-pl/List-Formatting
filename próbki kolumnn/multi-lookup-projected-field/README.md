# Multi-lookup fields and projected fields

## Podsumowanie
Lookup columns that support multiple values can be formatted using the advanced `forEach` property. 
Since the inclusion of the split operation, projected fields (additional columns associated to your lookup column) can now also be formatted using the same method. Ta próbka przedstawia two formats illustrating the difference in how these columns are formatted.

![zrzut ekranu próbki](./assets/screenshot.png)

### Multi-Lookup Columns vs Projected Fields

A lookup column becomes a multi-lookup column when you check the _Allow multiple values_ box under the primary column selection in the classic Column Settings screen for the Lookup column. If you check the box for any additional columns, these values become [projected fields](https://docs.microsoft.com/en-us/sharepoint/dev/schema/projectedfields-element-view).

![List Settings for Lookup Field](./assets/ListSettings-Multi-Lookup.png)

### Formatting Multi-Lookup Columns

The `multi-lookup.json` format should be applied to your primary lookup column. This format uses the [`forEach`](https://docs.microsoft.com/sharepoint/dev/declarative-customization/column-formatting?#foreach) property to act as a template elment for each selected lookup value for an item. This format puts each value in its own box.

We are accessing the value portion of the lookup item by using the `lookupValue` syntax (alternatively, we could access the lookup list's item id for the item with `lookupId`).

### Formatting Multi-Lookup Projected Fields

Unfortunately, multi-lookup projected fields don't come back as nice. Instead of being an array of objects, the values are all joined into a single line of text with multiple values separated by a space and a semi-colon (as seen in the Standard Display above).

We can now use the `split` operation to separate the string into an array which can then be used with the `forEach` property, with the `$itemIterator` value for the `txtContent`.

It's ideal to match the formatting properties of the projected fields with the primary lookup column to ensure the values line up correctly.

## Wymagania widoku
- The `multi-lookup.json` format can be applied to any multi-value lookup column
- The `multi-lookup-projected-field.json` format can be applied to any projected field

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
multi-lookup-projected-field.json | [Chris Kent](https://github.com/thechriskent), [Tim Hunt](https://github.com/timberrr)
multi-lookup.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|22 kwietnia 2021|Wersja początkowa
1.1|14 sierpnia 2023|Updated projected field to use split and forEach

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting#me)


<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/multi-lookup-projected-field" />
