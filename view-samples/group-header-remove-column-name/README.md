# Remove column name from group header

## Podsumowanie

This view formatting sample can be used to customize the group header to remove column name from group header.

![zrzut ekranu próbki](./assets/screenshot.png)

This sample contains two JSON files, one in which the group header is clickable (`group-header-remove-column-name-clickable.json`) and one in which it is not (`group-header-remove-column-name.json`). If you apply `group-header-remove-column-name-clickable.json` and click on a group header, you will see the view filtered by the value of the group header you clicked on.

## Wymagania widoku

List view with Group by applied on any column in the view.

> [!NOTE]
> If grouping by Person or Lookup column and applying this sample JSON, **[object Object]** will appear in the group header. If you group by Person or Lookup columns, please refer to the following table to make the necessary changes in the JSON.
> 
> | Type of column to group | Part of the JSON to be changed | After the change |
> | --- | --- | --- |
> | Person | @group.fieldData.displayValue | @group.fieldData.title |
> | Lookup | @group.fieldData.displayValue | @group.fieldData.lookupValue |

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
group-header-remove-column-name.json | [Ganesh Sanap](https://github.com/ganesh-sanap)
group-header-remove-column-name-clickable.json | [Ganesh Sanap](https://github.com/ganesh-sanap) & [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Version |Data          |Uwagi
--------|--------------|--------------------------------
1.0     |listopada 10, 2021 |Wersja początkowa
1.1     |października 17, 2023 |Added group-header-remove-column-name-clickable.json
1.2     |listopada 10, 2023 |Added note for grouping by Person and Lookup columns

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- [Group customization syntax reference](https://learn.microsoft.com/sharepoint/dev/declarative-customization/view-group-formatting)
- [Formatting syntax reference - Special string values](https://learn.microsoft.com/sharepoint/dev/declarative-customization/formatting-syntax-reference#special-string-values)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/group-header-remove-column-name" />
