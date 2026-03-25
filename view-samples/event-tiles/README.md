# Modern Event Tiles

## Podsumowanie
This sample demonstrates applying view formatting to an Events list to imitate the modern events webpart. The format is implemented using the Tiles view and there is a format included that only includes this portion to make customization easier ([event-tiles-only](./event-tiles-only.json)). The primary sample demonstrates using a single format to provide both a list and tile view as well as demonstrating implementing a custom hover card with default person hover cards as well.

![zrzut ekranu próbki](./assets/screenshot.png)

### Gallery View:

![zrzut ekranu próbki - tiles](./assets/screenshotTiles.png)

### Links

## Wymagania widoku
Even on modern sites, the Events list shows all views in the classic experience. You will have to follow these instructions to enable the modern experience on normal views (NOT the calendar view):

List Settings > Advanced settings > List Experience: Change to **New experience** and click OK.

This specific format expects the following columns to be part of the view:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Data|Deployed|Tak|
|Yes/No|Active|Tak|

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
event-tiles.json | [Chris Kent](https://github.com/thechriskent)
event-tiles-only.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|25 czerwca 2020|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi


<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/event-tiles" />
