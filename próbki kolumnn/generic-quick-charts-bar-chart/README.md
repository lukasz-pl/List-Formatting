# Bar Chart Column Formatter

## Podsumowanie

Ta próbka wykorzystuje **SharePoint List Formatting** to automatically generate a bar chart visualization for task status counts in each list item.  
Each row displays a dynamically generated bar chart showing the distribution of tasks across three states: "To Do", "In Progress", and "Done", making it easy to visualize project or task progress at a glance.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

Utwórz listę z następującymi kolumnami:

| Nazwa wewnętrzna | Typ    |
|---------------------|---------|
| **Title**       | Pojedyncza linia tekstu  |
| **ToDoCount**       | Liczba  |
| **InProgressCount** | Liczba  |
| **DoneCount**       | Liczba  |
| **Charts**       | Pojedyncza linia tekstu  |

*Uwaga: dodatkowe kolumny można dodać w zależności od potrzeb konkretnego przypadku użycia.*

## Dane przykładowe

| ToDoCount | InProgressCount | DoneCount |
|-----------|----------------|-----------|
| 5         | 3              | 12        |
| 8         | 2              | 5         |
| 0         | 4              | 16        |

## Jak to działa

- Formatter displays a **bar chart** for each list item based on task status counts
- Wykresy są generowane dynamicznie przy użyciu [QuickChart.io API](https://quickchart.io/)
- Each bar chart visualizes three data segments with unique colors:
  - **To Do** (Red - #FF6384)
  - **In Progress** (Yellow - #FFCE56)
  - **Done** (Blue - #36A2EB)
- Układ wyświetla wykresy w rozmiarze 400x250 pikseli z zaokrąglonymi rogami
- Wykres aktualizuje się automatycznie po zmianie wartości w kolumnach

## Konfiguracja zabezpieczeń

**KRYTYCZNE**: zanim wykresy zaczną się wyświetlać, musisz skonfigurować ustawienia zabezpieczeń SharePoint:

1. Navigate to **SharePoint Admin Center**
2. Przejdź do **Settings** > **Advanced Settings**  
3. Znajdź **"HTML Field Security"** section
4. Dodaj `quickchart.io` do listy **dozwolonych domen**
5. Zapisz konfigurację

**Bez tej konfiguracji zabezpieczeń wykresy nie będą wyświetlane z powodu zasad bezpieczeństwa zawartości w SharePoint.**

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-quick-charts-bar-chart.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|08 października 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

**Change Bar Colors:**
Modify the backgroundColor hex codes in the URL:
- Current: `%23FF6384` (Red), `%23FFCE56` (Yellow), `%2336A2EB` (Blue)
- Replace with your preferred colors (remember to URL-encode the # symbol as %23)

**Adjust Chart Size:**
Modify the dimensions in the style section:
```json
"style": {
  "width": "500px",
  "height": "300px"
}
```

**Change Chart Labels:**
The labels are URL-encoded in the chart URL. To customize labels, modify the `labels` array in the decoded URL:
- Current: `["To Do","In Progress","Done"]`
- Modify as needed for your use case

**Customize Dataset Label:**
Change `label:%22Tasks%22` to any text you prefer (URL-encode the text)

**Border Radius:**
Adjust the `border-radius` value to change corner roundness (use `"0px"` for square corners)

### Przykładowe zastosowania
- **Project Management**: Visualize task completion status across multiple projects
- **Sprint Tracking**: Monitor work items in agile development workflows
- **Resource Allocation**: Display distribution of team members across different work states
- **Quality Assurance**: Track bug status distribution (open, in progress, resolved)
- **Sales Pipeline**: Visualize deals across different pipeline stages
- **Support Tickets**: Monitor ticket distribution by status
- **Inventory Management**: Track stock levels across different categories

### Struktura adresu URL wykresu

Adres URL QuickChart używa formatu konfiguracji Chart.js (zakodowanego w URL):
```
https://quickchart.io/chart?c={
  type: "bar",
  data: {
    labels: ["To Do","In Progress","Done"],
    datasets: [{
      label: "Tasks",
      data: [5,3,12],
      backgroundColor: ["#FF6384","#FFCE56","#36A2EB"]
    }]
  }
}
```

### Color Palette

The default color scheme uses:
- **Red (#FF6384)**: Represents "To Do" tasks - typically indicating pending work
- **Yellow (#FFCE56)**: Represents "In Progress" tasks - showing active work
- **Blue (#36A2EB)**: Represents "Done" tasks - completed work

Możesz dostosować these colors to match your organization's branding or create different visual meanings.

### Ograniczenia
- Wymaga połączenia z internetem do generowania wykresów
- External dependency on QuickChart.io API
- Wydajność może się różnić przy dużych listach ze względu na wiele wywołań API
- Limited customization without modifying the URL-encoded chart configuration
- Chart renders as a static image (not interactive)

### Zaawansowane dostosowanie

For more advanced chart customization (colors, legends, etc.), you can modify the Chart.js configuration in the URL. Refer to the [QuickChart.io documentation](https://quickchart.io/documentation/) for available options.

## Licencja
To rozwiązanie formatowania jest udostępniane w stanie takim, w jakim jest, do celów edukacyjnych i profesjonalnych. Interfejs QuickChart.io API ma własne warunki korzystania.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-quick-charts-bar-chart" />