# Planner Inspired Task Cards

## Podsumowanie
Formats Task List Items in a Planner Inspired Card View. Uses Fluent UI Icons to designate "In Progress", "Completed" and "Delayed" Statuses. Automatically strikes out text for "Completed" items.  

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

Wszystkie poniższe pola powinny być częścią widoku, ale tylko te oznaczone jako Wymagane muszą mieć wartości:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Person|AssignedTo|Tak|
|Choice|Status|Nie|
|DataTime|DueData|Nie|

The `Status` column expects the following choice values:
- In Progress
- Delayed
- Completed

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
planner-inspired-task-card.json | [kwietnia Dunnam](https://github.com/aprildunnam)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|26 lipca 2019|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

This format takes advantage of `CustomRowActions` to enable the `defaultClick` and `delete` actions from icon buttons:

![Custom Actions in Action](./assets/screenshot.gif)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/planner-inspired-task-card" />
