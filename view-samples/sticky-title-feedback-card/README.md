# Sticky Title Feedback Card

This sample uses **SharePoint List Formatting** to display feedback items as **card-style layouts** with a prominent title header and scrollable feedback content.  
Each row is rendered as a visually appealing card with a yellow header for the title and a scrollable area for longer feedback text.

![zrzut ekranu próbki](assets/screenshot.png)

## View Requirements

Create a list with the following columns:

| Internal Name   | Type               |
|-----------------|--------------------|
| **Title**       | Pojedyncza linia tekstu|
| **Feedback**    | Wiele linii tekstu |

## How it Works

- Each feedback item is displayed as a **card** with rounded corners and subtle shadow.
- The **Title** appears in a yellow header bar at the top of each card.
- The **Feedback** content is displayed below in a scrollable area (max height: 180px).
- Cards have consistent spacing and borders for a clean, organized appearance.
- Long feedback text will scroll independently within each card while the title remains visible at the top.

## Próbka

Solution|Author
--------|---------
sticky-title-feedback-card.json | [Sai Bandaru](https://github.com/saiiiiiii) ([LinkedIn](https://www.linkedin.com/in/sai-bandaru-97a946153/))

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|26 października 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Additional Notes

- The title header uses a yellow background (`#fff78a`) with a darker yellow border for visual emphasis.
- The feedback area supports scrolling for content longer than 180px.
- You can adjust the `max-height` value in the JSON to show more or less content before scrolling.
- Works in both **light** and **dark** SharePoint themes.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/sticky-title-feedback-card" />