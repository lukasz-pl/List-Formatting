# Glossary View Formatters (connected list WebParts)

## Podsumowanie
View formatters to buid a glossary page using connected list WebParts.
![zrzut ekranu próbki](./assets/screenshot.gif)

Two lists are needed on this sample, so two separate JSON files are used:

File Name|View type for formatting|Details
---------|---------|--------
[glossary-filter.json](./glossary-filter.json)|Gallery|Used to format the filter list.
[glossary-filter-background.json](./glossary-filter-background.json)|Gallery|Used to format the filter list with letter on a background.
[glossary-dynamicfilter-view.json](./glossary-dynamicfilter-view.json)|List|Used to format the main list.

## Wymagania widoku

### List 1: Glossary Filter

Typ|Nazwa wewnętrzna|Wymagane|Details
-----|----------|--------|--------
Pojedyncza linia tekstu|Title|Tak|Used to store a character to be used as a filter


In this list we need to store all the alphabet letters from A to Z (or your country language variation of the alphabet if preferred) to be used later as filters.
Apply either the [glossary-filter.json](./glossary-filter.json) or [glossary-filter-background.json](./glossary-filter-background.json) view formatter in a view in this list.

---
### List 2: Glossary Terms
This is the list used to store all terms and descriptions. This list will consist of 3 fields:

Typ|Nazwa wewnętrzna|Wymagane|Details
-----|----------|--------|--------
Pojedyncza linia tekstu|Title|Tak|Used to store the glossary term
Wiele linii tekstu| Description|Tak|Used to store the term description, no rich text enabled
Calculated|FirstChar| |Used to show the first character of the term. This is the key to the whole functionality. Set it to use an output of 'Pojedyncza linia tekstu' and use as the formula: =LEFT(Title,1). This will extract only the first character from the Title field and use it as the value.

Apply the [glossary-view.json](./glossary-dynamicfilter-view.json) view formatter in a view in this list.

## Setting up the glossary page

Create a new blank page and add a single column section.
On this section, add a first List WebPart for the Glossary Filter list and use the following settings for the WebPart (hide the command bar so only the view content is shown):

![Filtered Glossary](./assets/gFilterWPSetup.png)

Add another list WebPart below it, but now select the Glossary Terms list, with the following settings (remember to hide the command bar so only the custom view will be shown):

![Filtered Glossary](./assets/gTermsWPSetup.png)

Rename the webparts as desired, save and publish your page to get the correct settings applied.

To be more user friendly, in the example shown above they were renamed from:

-Glossary Terms to Terms

-Glossary Filters to Glossary


## Próbka

Rozwiązanie|Autor(zy)
--------|---------
glossary-dynamicfilter-view.json | [Michel Mendes](https://github.com/michelcarlo) - Tweaked FAQ template from [Chris Kent](https://github.com/theChrisKent)
glossary-filter.json | [Michel Mendes](https://github.com/michelcarlo)
glossary-filter-background.json | [Watana](https://github.com/watana2)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|04 kwietnia 2021|Wersja początkowa
1.1|13 grudnia 2024|Added `glossary-filter-background.json`

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

References:

Glossary content was built using Microsoft Terminology Collection:
https://www.microsoft.com/en-us/language/Terminology

JSON for Glossary view was adapted from the FAQ Sample from PnP GitHub Samples:
https://github.com/pnp/List-Formatting/tree/master/view-samples/faqs


<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/glossary-dynamicfilter-view" />
