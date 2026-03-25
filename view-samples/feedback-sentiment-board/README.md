# Feedback Sentiment Board

This sample uses **SharePoint List Formatting** to visualize feedback sentiment (Positive, Neutral, Negative) with **keyword-based detection** in a color-coded and emoji-enhanced card view.  
Each feedback item is automatically analyzed for sentiment keywords and displayed as a beautiful card showing the sentiment icon, feedback text, author details, and submission date.

![zrzut ekranu próbki](assets/screenshot.png)

## Podsumowanie

- **Automatic sentiment detection** based on keywords in feedback text
- **Color-coded cards** with gradient backgrounds (Green for positive, Red for negative, Yellow for neutral)
- **Emoji indicators** (😊 😞 😐) displayed in circular badges
- **Status** showing POSITIVE/NEGATIVE/NEUTRAL
- **Author avatars** with initials in gradient circles
- **Modern card layout** with shadows and rounded corners
- Perfect for **HR feedback forms**, customer surveys, and employee pulse checks

## View Requirements

Create a list with the following columns:

| Internal Name   | Type                        | Description                           |
|-----------------|-----------------------------|---------------------------------------|
| **Title**       | Pojedyncza linia tekstu         | Feedback title or category            |
| **Feedback**    | Wiele linii tekstu      | The actual feedback content           |
| **Author**      | Person or Group             | Person who submitted the feedback     |
| **Created**     | Data i godzina               | Submission date (auto-generated)      |

**Note:** If your Author column has a different internal name, update `[$Author0]` in the JSON to match your column name (e.g., `[$Author]`).

## Sentiment Keywords

### Positive Keywords (😊 Green):
excellent, great, amazing, love, fantastic, wonderful, outstanding, perfect, impressed, exceptional

### Negative Keywords (😞 Red):
poor, bad, terrible, worst, hate, awful, horrible, frustrated, disappointing

### Neutral (😐 Yellow):
Any feedback without the above keywords

## Próbka Data

| Title                    | Feedback                                                                                      | Author             | Created              |
|--------------------------|-----------------------------------------------------------------------------------------------|--------------------|----------------------|
| Employee Onboarding      | The onboarding process was excellent! Everything was well organized and the team was welcoming. | Sai Bandaru         | 2025-10-24T06:17:08Z |
| Need faster approvals      | The document approval process is slow sometimes.           | Budvik B      | 2025-10-25T08:30:00Z |
| Poor cafeteria service       | Food quality has bad in recent days.          | Sai Bandaru       | 2025-10-25T14:45:00Z |

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
feedback-sentiment-board.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|25 października 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Additional Notes

- **Keyword detection is case-insensitive** - works with any capitalization
- You can easily add more keywords by extending the `indexOf()` conditions in the JSON
- The sentiment is determined by the **first matching keyword** found in the feedback text

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/feedback-sentiment-board" />