# Project Gantt Chart

## Podsumowanie
This project Gantt Chart sample demonstrates how to show a list of high level tasks in a Gantt chart. It is mainly useful for top-level views.

So this

![list view](./assets/unformattedlistview.png)  

Turns into this

![zrzut ekranu próbki](./assets/screenshot.png)  

## Wymagania widoku
This format expects the following columns to be part of the view:

|Typ|Nazwa wewnętrzna|Wymagane|Values\
|---|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak||
|Data|ProjectStart|Tak||
|Data|ProjectDue|Tak||
|Data|TaskStart|Tak||
|Data|TaskDue|Tak||
|Liczba|Progress|Tak||
|Choice|TaskType|Nie|Task, Milestone|
|People (single select)|AssignedToUser|Tak||
|Multilines of text (no format)|TaskDescription|Tak||

The view should be sorted by `TaskStart`, ascending

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
project-gantt-chart.json | [Geert de Kooter](https://github.com/gdk-max)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|1 listopada 2020|Wersja początkowa
2.0|10 lutego 2021| Added status Progress indicator, current date indicator, and width fixes
3.0|12 sierpnia 2023|Added Milestones, Progressbar, Clicks to update the progress, Task description, Task assignment, Labels that mover from right to left based on the amount of space.

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/project-gantt-chart" />
