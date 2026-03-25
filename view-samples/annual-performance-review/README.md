# Annual Performance Review

## Podsumowanie

This sample demonstrates how to change row data to column format for annual performance review forms, inspired by list formatting authors of Smart Goal, Elf Progress Board, Display a User's Photo in Group Header, and Rounded fill checkbox.

![zrzut ekranu próbki](./assets/screenshot.png)

This diagram represents the structure of how the list view is formatted. It shows the hierarchical relationship of various elements.

![sample structure diagram](./assets/diagram.png)

> [!NOTE]
> This sample also includes [command bar customization](https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/view-commandbar-formatting).

## Wymagania widoku

- Group by Employee field in the view settings and set default to Expanded to show user's photo in group header.
- This format expects the following columns to be part of the view:

Column Name | Wymagane | Type
----------- | -------- | ----
Employee    | Yes      | Person or Group
EditMode    | No       | Yes/No
Q1e         | No       | Liczba
Q1m         | No       | Liczba
Q2e         | No       | Liczba
Q2m         | No       | Liczba
Q3e         | No       | Liczba
Q3m         | No       | Liczba
Q4e         | No       | Liczba
Q4m         | No       | Liczba

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
annual-performance-review.json | [Watana](https://github.com/watana2)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0    |października 6, 2024|Wersja początkowa
2.0    |października 16, 2024|New layout
2.1    |października 24, 2024|Added edit mode switch, fixed border thickness and alignment.
2.2    |października 30, 2024|Corrected the misalignment issues caused by the recent updates.

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/annual-performance-review" />
