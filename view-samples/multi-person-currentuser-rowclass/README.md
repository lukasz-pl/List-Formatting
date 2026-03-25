# Current User's Rows (Using a Multi-Person Column)

## Podsumowanie
Highlights the entire row for any list items where one of the assigned to users is the current user (the user viewing the list view, not the author of the format). You can easily adjust this to use a different person column by changing the `[$AssignedTo]` portion of the expression.

By using the Office UI Fabric color classes for themes, we can ensure our format looks good in all themes including both light and dark as well as custom themes.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
- This format expects a person column with an internal name of `AssignedTo` to be part of the view. This column can be single or multi-select.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
multi-person-currentuser-rowclass.json | [Chris Kent](https://github.com/thechriskent)
## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|29 stycznia 2019|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

This sample works for **both** single and multi-select person fields.However, an additional sample is available intended for use with single-select person fields: [person-currentuser-rowclass](../person-currentuser-rowclass). It is a simpler sample intended to show how to use the `@me` operator.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/multi-person-currentuser-rowclass" />
