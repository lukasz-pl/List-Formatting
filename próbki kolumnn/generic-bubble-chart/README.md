# Bubble Chart

Ta próbka pokazuje how to use **SharePoint Column Formatting** to create a dynamic **bubble chart** in a list view. The size and color of each bubble are automatically determined by the length of the text in its corresponding column, providing a quick visual representation of your data.

![zrzut ekranu próbki](./assets/screenshot.png)

### Podsumowanie

  * The bubble size and color are dynamically generated.
  * A wider range of sizes and colors is supported for a more vibrant appearance.
  * The bubbles are arranged into a multi-line layout to prevent horizontal crowding.
  * The text within each bubble is horizontally and vertically centered, even when it wraps to multiple lines.

### Wymagania widoku

Utwórz listę SharePoint z następującymi kolumnami:

| Column Name | Type |
|-------------|-------------|
| Title     | Pojedyncza linia tekstu |
| LABEL1    | Pojedyncza linia tekstu |
| LABEL2    | Pojedyncza linia tekstu |
| LABEL3    | Pojedyncza linia tekstu |
| LABEL4    | Pojedyncza linia tekstu |
| LABEL5    | Pojedyncza linia tekstu |
| LABEL6    | Pojedyncza linia tekstu |
| LABEL7    | Pojedyncza linia tekstu |
| LABEL8    | Pojedyncza linia tekstu |
| LABEL9    | Pojedyncza linia tekstu |
| LABEL10   | Pojedyncza linia tekstu |
| LABEL11   | Pojedyncza linia tekstu |
| LABEL12   | Pojedyncza linia tekstu |
| LABEL13   | Pojedyncza linia tekstu |
| LABEL14   | Pojedyncza linia tekstu |
| LABEL15   | Pojedyncza linia tekstu |
| LABEL16   | Pojedyncza linia tekstu |
| LABEL17   | Pojedyncza linia tekstu |
| LABEL18   | Pojedyncza linia tekstu |
| LABEL19   | Pojedyncza linia tekstu |
| LABEL20   | Pojedyncza linia tekstu |

Formatting code will apply to the column containing the JSON and reference these other columns to create the complete visual.

## Jak zastosować

1. Open your **SharePoint list**.
2. Click the column header you want to format → **Column settings → Format this column**.
3. Switch to **Advanced mode**.
4. Paste the JSON provided in this project into the formatting editor.
5. Click **Save**. The column will render as a word cloud automatically.

### Jak to działa

The bubble chart is created using a single JSON file that applies to a column in your SharePoint list. The key parts of the code are:

  * **Dynamic Sizing:** The `width` and `height` of each bubble are set using nested `if` statements that evaluate the length of the text in the corresponding `LABEL` column. This creates a range of sizes, from a small 30px bubble to a large 120px bubble.
  * **Conditional Coloring:** The `background-color` property is also controlled by the text length, with a different color assigned to each size range.
  * **Multi-line Layout:** The bubbles are grouped into separate `div` elements to force them to wrap onto multiple lines, creating a clean, organized layout.

### Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-bubble-chart.json | [Sai Bandaru](https://github.com/saiiiiiii)

### Historia wersji

| Version | Data            | Uwagi       |
|---------|-----------------|----------------|
| 1.0     | września 2, 2025 | Wersja początkowa |

### Zastrzeżenie

**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

-----

### Dodatkowe uwagi

  * You can easily customize the bubble sizes, colors, and the number of rows by editing the JSON code.

## Odnośniki

- [SharePoint Column Formatting Documentation](https://learn.microsoft.com/sharepoint/dev/declarative-customization/column-formatting)
- [JSON Schema for SharePoint Column Formatting](https://developer.microsoft.com/json-schemas/sp/v2/column-formatting.schema.json)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-bubble-chart" />
