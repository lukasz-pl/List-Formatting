# Diet Plan Card Formatter

## Podsumowanie

This SharePoint JSON view formatting sample transforms your list items into rich, visually appealing diet plan cards. Each card highlights a meal or plan with a banner image, author details, key nutritional values, and a prominent call-to-action button.
This layout is ideal for health & wellness portals, employee fitness programs, or meal planning lists.

![zrzut ekranu próbki](./assets/screenshot.png)
![zrzut ekranu próbki](./assets/sample2.png)

## Wymagania widoku

### 📝 Recommended SharePoint List Columns

| Column Name           | Type                   | Description                               |
| --------------------- | ---------------------- | ----------------------------------------- |
| Title                 | Pojedyncza linia tekstu    | Name of the meal or plan                  |
| BannerImageUrl        | Pojedyncza linia tekstu    | URL to the header image                   |
| Author                | Person or Group        | Creator of the plan                       |
| Benefits              | Wiele linii tekstu | Key benefits of the plan                  |
| DietType              | Choice                 | Type of diet (e.g., Keto, Vegan)          |
| Duration              | Liczba                 | Duration in days or weeks                 |
| Calories              | Liczba                 | Caloric value                             |
| PlanLink              | Hiperłącze or Picture   | Link to full plan details                 |
| BackgroundColor       | Pojedyncza linia tekstu    | Background color for the card             |
| ButtonBackgroundColor | Pojedyncza linia tekstu    | Background color for the metric buttons   |
| ForegroundColor       | Pojedyncza linia tekstu    | Text/icon color inside the metric buttons |


A PowerShell Script (Create List.ps1) has been provided in the assets folder to provision the list for you.

**Note:** This script uses [PnP PowerShell](https://pnp.github.io/powershell/) and requires an environment ready for PnP PowerShell.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
diet-plan-card.json | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|03 maja 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- This sample also includes command bar customization, and the "Add new item" button will be hidden.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/diet-plan-card" />
