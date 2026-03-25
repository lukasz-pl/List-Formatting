# Event Registration

## Podsumowanie

This sample provides Event registration with different capabilities such us Start and End dates, Category, Attendees, All Day option, Location, Team URL, and favoriting.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania widoku
This sample is not intended to be used with the standard Events list but rather a custom list with the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
Description | Wiele linii tekstu
StartData | Data i godzina
EndData | Data i godzina
Category | Choice - include option "Meeting, Work hours, Business, Holiday, Get-together, Gifts, Birthday"
Categorize | Choice - "Red, Blue, Green, Orange, Purple, Yellow"
Attendees | Person - Allow multiple selections
AllDay | Yes/No - Default **"No"**
Location | Pojedyncza linia tekstu 
TeamUrl | Pojedyncza linia tekstu 
Favorite | Yes/No - Default **"No"**
Difference | Calculated - include formula "=INT((EndData-StartData)*1440)" to retrieve minutes from event

Edit View requirements
- Include `Modified by` and `Modified` columns in View
- Sort View by `StartData` descending.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
event-registration.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|12 stycznia 2022|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/event-registration" />
