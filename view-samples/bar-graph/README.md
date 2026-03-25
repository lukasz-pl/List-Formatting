# Bar Graph

## Podsumowanie

This sample shows how to format a list to show the data as a bar graph. In this instance we are showing number of votes per fruit.

![zrzut ekranu próbki](./assets/screenshot.png)

The sample features the following:
- Conditionally showing a crown icon if the item is marked as MostVoted
- Conditionally showing elements (trending limit) based on `@rowIndex`
- Conditionally showing a trending icon if the item has more than 700 votes
- Conditionally changing the colour of the bar if the item has more than 700 votes
- Use of theme color classes to ensure the format displays as intended regardless of theme (light, dark, custom, etc.)
- If [inject css application customiser](https://github.com/SharePoint/sp-dev-fx-extensions/tree/master/samples/react-application-injectcss) with [animate.css](https://daneden.github.io/animate.css/) is deployed then, this sample adds animation to bars.

## View with animate.css application customiser
![Bar Graph Screenshot with animate.css app customiser](./assets/bargraph.gif)


## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Liczba|Votes||
|Yes/No|IsLastItem||
|Yes/No|IsHighest||
|Pojedyncza linia tekstu|Icon||

## Konfiguracja

The sample needs the following setup:
- Only one item needs to have `IsHighest` as yes
- Only the last item needs to have `IsLastItem` as yes

The idea is that this data gets populated via some code so that it can represented as a graph.

In the sample, the height of the parent div is set to 800px and the child div calculates heights. The heights are calcuated considering 1000 as the max number of votes. If this number needs changed, please update the formulas in lines 50 and 103 accordingly.

### Inject CSS applcation customiser
The [inject css application customiser](https://github.com/SharePoint/sp-dev-fx-extensions/tree/master/samples/react-application-injectcss) by [Hugo Bernier](http://tahoeninjas.blog/) shows how we can inject css on to pages. Please follow the instructions in readme.md of that sample and use [animate.min.css](https://raw.githubusercontent.com/daneden/animate.css/master/animate.min.css) instead of custom.css .

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
bar-graph.json | [Anoop Tatti](https://github.com/anoopt)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|września 02, 2019 |Wersja początkowa

## Improvements
Need to check if a gradient css can also be added to the bars, with an application customiser.

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/bar-graph" />
