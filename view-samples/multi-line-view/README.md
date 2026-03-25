# Multi-line View

## Podsumowanie

This example uses the `rowFormatter` element, which totally overrides the rendering of a list view row. The `rowFormatter` in this example creates a bounding `<div />` box for every list view row.  Inside this bounding box, the `$Title` and `$Feedback` fields are displayed on separate lines.  Under those fields, a `button` element is displayed that, when clicked, does the same thing as clicking the list row in an uncustomized view, which is opening the property form for the item.  This `button` is displayed conditionally, when the value of the `$Assigned_x0020_To` field (assumed to be a person/group field) matches the current signed-in user.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
- The format expects the `Title` field
- The format expects a text column with an internal name of `Feedback`
- The format expects a person column with an internal name of `Assigned_x0020_To`

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
multi-line-view.json | [Lincoln DeMaris](https://github.com/ldemaris)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|10 sierpnia 2018|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/multi-line-view" />
