# Column Graph format

## Podsumowanie

This sample shows how to format a list to show the data as a column graph. In this instance we are showing number of views per blog.

![zrzut ekranu próbki](./assets/screenshot.png)

The sample features the following:
- Conditionally showing a crown icon if the item is marked as MostRead
- Conditionally showing elements (chart labels) based on `@rowIndex`
- Conditionally showing a trending icon if the item has more than 700 views
- Conditionally changing the colour of the bar if the item has more than 700 views
- Use of theme color classes to ensure the format displays as intended regardless of theme (light, dark, custom, etc.)

### Item Hover view
![Column Graph with Title Screenshot](./assets/columngraph_with_title.png)

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Liczba|Views||
|Yes/No|MostRead||

### Konfiguracja

The sample needs the following setup:
- Only one item needs to have `MostRead` as yes

The idea is that this data gets populated via some code so that it can represented as a graph.

In the sample, the height of the parent div is set to 800px and the child div calculates heights. The heights are calcuated considering 1000 as the max number of views. If this number needs changed, please update the formulas in lines 89 and 112 accordingly.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
column-graph.json | [Anoop Tatti](https://github.com/anoopt)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|sierpnia 15, 2019 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/column-graph" />
