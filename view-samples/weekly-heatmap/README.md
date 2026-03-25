# Weekly Heatmap

This sample uses **SharePoint List Formatting** to display weekly data as a **heatmap calendar view**.  
Each row represents a week, and daily values are visualized with conditional background colors, making it easy to spot trends and high/low activity days.

![zrzut ekranu próbki](./assets/screenshot.png)

## Podsumowanie

- Each day (Monday–Sunday) is displayed in a horizontal weekly row.
- Cell background colors are based on the **numeric values** (higher values = darker shade).
- Values 0 or less are shown in gray, while values greater than 11 are displayed with the darkest green.
- The `WeekStartData` column ensures proper ordering of weekly records.
- The `Team` column can be used to filter heatmaps by department.

## View Requirements

Create a list with the following columns:

| Internal Name   | Type               |
|-----------------|--------------------|
| **Title**       | Pojedyncza linia tekstu|
| **WeekStartData** | Data i godzina (Data only) |
| **Monday**      | Liczba             |
| **Tuesday**     | Liczba             |
| **Wednesday**   | Liczba             |
| **Thursday**    | Liczba             |
| **Friday**      | Liczba             |
| **Saturday**    | Liczba             |
| **Sunday**      | Liczba             |
| **Team**        | Choice (e.g., Development, QA, Design, etc.) |

## Próbka Data

| Title   | WeekStartData        | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | Team        |
|---------|----------------------|--------|---------|-----------|----------|--------|----------|--------|-------------|
| Week 1  | 2025-08-01T04:00:00Z | 0      | 0       | 0         | 0        | 10     | 0        | 0      | Development |
| Week 2  | 2025-08-04T04:00:00Z | 10     | 20      | 8         | 9        | 7      | 0        | 0      | Development |
| Week 4  | 2025-08-11T04:00:00Z | 12     | 11      | 8         | 3        | 10     | 0        | 0      | Development |

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
weekly-heatmap.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|19 sierpnia 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Additional Notes

- You can adjust the **color scale thresholds** in the JSON to match your data distribution.
- Supports both **light** and **dark** SharePoint themes.
- Works best in **List view** with `WeekStartData` sorted ascending.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/weekly-heatmap" />
