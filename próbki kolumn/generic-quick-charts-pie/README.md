# Pie Chart Column Formatter

## Podsumowanie

Ta próbka wykorzystuje **SharePoint List Formatting** to automatically generate a pie chart visualization for task status counts in each list item.  
Each row displays a dynamically generated pie chart showing the distribution of tasks across three states: "To Do", "In Progress", and "Done", making it easy to visualize project or task progress at a glance.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

Utwórz listę z następującymi kolumnami:

| Nazwa wewnętrzna | Typ    |
|---------------------|---------|
| **Title**       | Single line of text  |
| **ToDoCount**       | Number  |
| **InProgressCount** | Number  |
| **DoneCount**       | Number  |
| **Charts**       | Single line of text  |

*Note: Additional columns can be added as needed for your specific use case.*

## Dane przykładowe

| ToDoCount | InProgressCount | DoneCount |
|-----------|----------------|-----------|
| 5         | 3              | 12        |
| 8         | 2              | 5         |
| 0         | 4              | 16        |

## Jak to działa

- Formatter displays a **pie chart** for each list item based on task status counts
- Charts are generated dynamically using the [QuickChart.io API](https://quickchart.io/)
- Each pie chart visualizes three data segments:
  - **To Do** (first segment)
  - **In Progress** (second segment)
  - **Done** (third segment)
- The layout displays charts at 400x250 pixels with rounded corners
- The chart automatically updates when column values change

## Konfiguracja zabezpieczeń

**CRITICAL**: Before the charts will display, you must configure SharePoint security settings:

1. Navigate to **SharePoint Site**
2. Przejdź do **Site Settings**
3. Znajdź **"HTML Field Security"** section
4. Add `quickchart.io` to the **allowed domains** list
5. Zapisz konfigurację

**Bez tej konfiguracji zabezpieczeń wykresy nie będą wyświetlane z powodu zasad bezpieczeństwa zawartości w SharePoint.**

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-quick-charts-pie.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|October 08, 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

### Przykładowe zastosowania
- **Project Management**: Visualize task completion status across multiple projects
- **Sprint Tracking**: Monitor work items in agile development workflows
- **Resource Allocation**: Display distribution of team members across different work states
- **Quality Assurance**: Track bug status distribution (open, in progress, resolved)
- **Sales Pipeline**: Visualize deals across different pipeline stages
- **Support Tickets**: Monitor ticket distribution by status

### Struktura adresu URL wykresu

Adres URL QuickChart używa formatu konfiguracji Chart.js (zakodowanego w URL):
```
https://quickchart.io/chart?c={
  type: "pie",
  data: {
    labels: ["To Do","In Progress","Done"],
    datasets: [{
      data: [5,3,12]
    }]
  }
}
```

### Ograniczenia
- Requires internet connectivity for chart generation
- External dependency on QuickChart.io API
- Performance may vary with large lists due to multiple API calls
- Chart colors are automatically assigned by QuickChart.io
- Limited customization without modifying the URL-encoded chart configuration

### Zaawansowane dostosowanie

For more advanced chart customization (colors, legends, etc.), you can modify the Chart.js configuration in the URL. Refer to the [QuickChart.io documentation](https://quickchart.io/documentation/) for available options.

## Licencja
To rozwiązanie formatowania jest udostępniane w stanie takim, w jakim jest, do celów edukacyjnych i profesjonalnych. Interfejs QuickChart.io API ma własne warunki korzystania.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-quick-charts-pie" />