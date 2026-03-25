# Interactive Content Card with Explore Button

## Podsumowanie

This sample uses **SharePoint List Formatting** to display list items as **modern card tiles** with a prominent image header, icon overlay, and call-to-action button.  
Each card features a fixed 365x400px layout with an image background, branded icon badge, title/description content area, and an "Explore Section" button that opens external links.

![zrzut ekranu próbki](./assets/screenshot.png)

## View Requirements

Create a list with the following columns:

| Internal Name   | Type               | Description |
|-----------------|--------------------|-------------|
| **Title**       | Pojedyncza linia tekstu| Card title/heading |
| **Description** | Wiele linii tekstu | Card description/summary |
| **Image**       | Single of text          | Main card background image (upload image siteassets) |
| **IconUrl**     | Pojedyncza linia tekstu | Small icon for the overlay badge (upload image/url siteassets) |
| **Url**         | Hiperłącze          | Target URL for the "Explore Section" button |


## How it Works

- **Image Header**: The main image (`Image` column) serves as a 220px tall background header
- **Icon Overlay**: A circular white badge in the top-left displays the icon from `IconUrl`
- **Content Area**: White content section displays the `Title` in red (#dc3545) and `Description` in gray
- **Action Button**: "Explore Section" button links to the URL specified in the `Url` column
- **Fixed Dimensions**: Each card maintains consistent 365x400px sizing with 20px right margin
- **External Links**: All URLs open in new tabs/windows for better user experience

## Design Features

- **Modern Card Design**: Clean, professional appearance with rounded corners
- **Responsive Layout**: Fixed-width cards that work well in grid arrangements
- **Brand Colors**: Red accent color (#dc3545) for titles and button borders
- **Accessibility**: Proper contrast ratios and semantic HTML structure
- **Interactive Elements**: Hover-friendly button styling

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
interactive-content-card.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|16 września 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Additional Notes

- **Image Requirements**: Use high-quality images (minimum 365px wide) for best results
- **Icon Format**: PNG or SVG icons work best for the overlay badge (24x24px display size)
- **URL Validation**: Ensure all URLs are properly formatted and accessible
- **Performance**: Consider image optimization for faster loading times
- **Customization**: Modify colors, spacing, and button text in the JSON as needed
- **Mobile Friendly**: Fixed-width design works well on desktop and tablet devices

## Customization Options

You can easily customize this formatter by modifying:
- **Colors**: Change the red accent color (#dc3545) to match your brand
- **Button Text**: Update "Explore Section" to your preferred call-to-action
- **Dimensions**: Adjust card width/height and image header size
- **Border Radius**: Modify the 8px border-radius for different corner styles
- **Spacing**: Adjust padding and margins for tighter or looser layouts

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/interactive-content-card" />
