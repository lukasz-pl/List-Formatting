# Image Card Tiles

## Podsumowanie
This sample displays images in a visually appealing tile layout with modern styling using SharePoint's Gallery view. Each image tile is clickable and navigates to a URL specified in another column. The tiles feature rounded corners, shadow effects, and a clean design that works well for image galleries, catalogs, or showcase layouts.

**Note**: This is a view formatter (tile formatter) that should be applied to a Gallery view, not a column formatter.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
- Create a view based on `Gallery` layout
- Apply this formatter to the tile view

|Typ|Nazwa wewnętrzna|Wymagane|Purpose|
|----|-------------|--------|-------|
|Pojedyncza linia tekstu|Title|Tak|Accessibility alt text|
|Hiperłącze or Picture|ImageURL|Tak|Image URL|
|Hiperłącze or Picture|URL|Nie|Contains the target link|

> [!NOTE]  
> If images from external sites are specified for `ImageURL`, HTML field security must be set. For more information see: [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b).

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
image-card-tiles.json | [Nanddeep Nachan](https://github.com/nanddeepn), [Smita Nachan](https://github.com/smitanachan)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|11 sierpnia 2025|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## How it works

This formatter creates a modern tile-based layout for displaying images in a SharePoint list or library gallery view with the following features:

### Structure:
1. **Container**: A flex container with rounded corners and shadow effect
2. **Clickable Link**: The entire tile is wrapped in an anchor tag that links to the URL column
3. **Image Display**: Images are displayed using `object-fit: contain` to maintain aspect ratio
4. **Responsive Design**: The tiles maintain consistent dimensions while adapting to different screen sizes

### Key Features:
- **Modern Styling**: Clean design with rounded corners, shadows, and proper spacing
- **Accessibility**: Includes proper alt text from the Title column
- **Link Integration**: Seamlessly integrates with URL columns for navigation
- **Consistent Layout**: Fixed tile dimensions ensure uniform appearance
- **Visual Feedback**: Hover and focus states provide user interaction feedback

## Browser Compatibility:
This formatter uses modern CSS properties including flexbox, object-fit, and box-shadow, which are supported in all modern browsers.

## Dodatkowe uwagi

### Customization Options:
- **Tile dimensions**: Adjust the height and width properties at the top level (currently set to 100px height and 180px width)
- **Border radius**: Modify the `border-radius` value on line 11 to change the rounded corner effect (currently 12px)
- **Shadow effect**: Customize the `box-shadow` on line 12 for different shadow styles
- **Spacing**: Adjust the `margin` property on line 16 to change spacing between tiles (currently 10px)
- **Link behavior**: Change the `target` attribute on line 24 to control how links open:
  - `"_blank"` - Opens in a new window/tab (current setting)
  - `"_self"` - Opens in the same window
- **Image fit**: Modify the `object-fit` property on line 46 to control how images are displayed within the tile:
  - `"contain"` - Shows the entire image (current setting)
  - `"cover"` - Fills the tile, may crop image
  - `"fill"` - Stretches image to fill tile

### Column References:
- `[$URL]`: References the URL column containing the target link
- `[$ImageURL]`: References the image URL from the image column
- `[$Title]`: References the title column for accessibility alt text

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/image-card-tiles" />