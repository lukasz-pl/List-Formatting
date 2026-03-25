# Stat Comparison Chart

## Podsumowanie
These samples format a list view into a chart that shows a comparison between two entities against various attributes. This sample can be used for all sorts of things but is demonstrated below using sports teams for the entities and stats for the teams as individual rows.

![zrzut ekranu próbki](./assets/screenshot.png)

There are 2 versions of the sample included. The difference being that one shows images to represent each entity (team country flags in this case) and icons for individual stats while the other does not.

**Version without Images:**
![zrzut ekranu the sample without images](./assets/screenshot_without_images.png)

> These samples are dervied from the [Butterfly Chart Sample](../butterfly-chart/).

## Wymagania widoku (stat-comparison-chart.json)

|Type                |Internal Name|Wymagane|Details|
|--------------------|-------------|:------:|-------|
|Pojedyncza linia tekstu |Title        |Yes     |The attribute against which the stats are measured|
|Pojedyncza linia tekstu |Icon         |No      |Icon to represent the attribute|
|Liczba              |Entity1      |Yes     |The stat value for the first entity|
|Liczba              |Entity2      |Yes     |The stat value for the second entity|
|Yes/No              |IsPercent    |No      |True when the stat is a percentage|
|Image               |Entity1Image |No      |Image to represent the first entity. Will be only displayed for the first row at the top left. |
|Image               |Entity2Image |No      |Image to represent the second entity. Will be only displayed for the first row at the top right.|


## Wymagania widoku (stat-comparison-chart-without-images.json)

These requirements are the same as above except that icons and images are not needed.

|Type                |Internal Name|Wymagane|
|--------------------|-------------|:------:|
|Pojedyncza linia tekstu |Title        |Yes     |
|Liczba              |Entity1      |Yes     |
|Liczba              |Entity2      |Yes     |
|Yes/No              |IsPercent    |No      |

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
stat-comparison-chart.json | [Anoop Tatti](https://github.com/anoopt)
stat-comparison-chart-without-images.json | [Anoop Tatti](https://github.com/anoopt)

## Historia wersji

Version |Data              |Uwagi
--------|------------------|--------
1.0     |czerwca 23, 2021  |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/stat-comparison-chart" />
