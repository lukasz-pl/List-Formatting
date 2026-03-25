# SharePoint View Formatting – Course Training Tile Cards

## Podsumowanie
Modern tile card layout for displaying training courses with images, badges, and hover previews in SharePoint Gallery view.

![zrzut ekranu próbki](./assets/screenshot.png)

## Fields Wymagane

| Column | Type | Wymagane |
|--------|------|----------|
| Title | Pojedyncza linia tekstu | Yes |
| Image | Image | No |
| Visual | Choice | No |
| Sponsor | Pojedyncza linia tekstu | No |
| Description | Wiele linii tekstu | No |
| Hours | Liczba | No |
| Flag | Choice | No |
| URL | Hiperłącze or Picture | Yes |

> [!NOTE]
> If no image is provided in the `Image` column, this sample displays the image located in the “SiteAssets” library > “Images” folder > “tile-default.png” within the site (line 108).
> Update the image file or path as needed.

## Funkcje

- **280×350px tile cards** with course thumbnails
- **Hover popup** showing title and description
- **Duration badge** (auto-converts to hours/minutes)
- **Flag badge** for highlighting courses
- **Responsive image** with fallback to default
- **Direct link** to course content

## Próbka

| Rozwiązanie | Autor(zy) |
|----------|-----------|
| course-training-tiles.json | [Sai Bandaru](https://github.com/saiiiiiii) |

## Version History

| Wersja | Data | Uwagi |
|---------|------|----------|
| 1.0 | lutego 13, 2026 | Wersja początkowa |

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/course-training-tiles" />