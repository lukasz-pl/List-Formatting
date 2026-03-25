# Exam Bundle Tracker

## Podsumowanie

Often in certain schools, a system of _corporate marking_ exists where multiple teachers teaching a particular cohort (e.g. Mathematics Extension 1) will mark a section of each student's paper to ensure consistency.

When this occurs, often bundles of papers are divided by class, and each teacher takes a bundle out of a cupboard, but it can be hard to track:
- Who has possession of a particular bundle
- Whether I have marked a particular bundle or not (without having to hunt down and check through every bundle!)

This sample transforms your list into an Exam Bundle Tracker which answers the two questions above.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania widoku
The view format expect the following fields.

Internal Name |Type | Choices | Allow Fill in Choice | Other notes
--------|---------|--------|---------|---------
Title | Pojedyncza linia tekstu | | 
YearOfTask | Choice | `2023`, `2024`, `2025` etc | Yes |  | 
CourseYear | Choice	| `07`, `08`, ..., `11 - Adv`, `11 - Ext 1`, `12 - Adv`, `12 - Ext 1`, `12 - Ext 2` etc | No |  
BundleLiczba | Choice | `1`, `2`, ..., `7` | No | 
TotalBundles | Liczba | | | Min: `0`
TaskLiczba | Choice	| `1`, `2`, `3`, `4 (Yearly/Trial)` | 
InPossession | Person | | 
NotMarked | Multi Person | | 
Marked | Multi Person | | 
UpdateLog | Wiele linii tekstu, append to previous | | 
InCirculation | Yes/No | | 

### Views to make it work
The following views are needed, with the JSON code applied to the following views:

View name | Type | Sorting | Filtering | Group | Other notes | JSON code to paste
--------|---------|--------|---------|---------|---------|---------
Overview | List | None | `InCirculation` equal to `Yes` | `CourseYear` asc | | exam-bundle-tracker-overview.json
Overview - include out of circulation  | List | `YearOfTask` desc, `BundleLiczba` asc |  | `CourseYear` asc | | exam-bundle-tracker-overview.json

All grouping is initially expanded.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
exam-bundle-tracker.json | [Hubert Lam](https://github.com/z3019494)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|14 lipca 2023|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
Use the default **All Items** and **Edit in Grid** view to bulk enter new exam bundles.

## Acknowledgements
The Exam Bundle Tracker was inspired by multiple other samples found here in the PnP community, and the author greatly acknowledges their contributions.
- [Giuliano Del Luca's Video Library view](https://github.com/giuleon/ListViewFormattingVideoLibrary)
- [Tetsuya Kawahara's Assign to Me column formatting](https://github.com/pnp/List-Formatting/tree/master/column-samples/person-assign-to-me)
- [Michel Mendes' Group Header Status Icon and Color group formatting](https://github.com/pnp/list-formatting/tree/master/view-samples/group-header-status-icon-color)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/exam-bundle-tracker" />