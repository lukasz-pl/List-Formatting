# Uruchamianie przepływu dla wybranego elementu

## Podsumowanie
Możesz użyć formatowania kolumn, aby create buttons that, when clicked, run Flows on the corresponding list item. The Flow Launch Panel will be displayed after clicking the button allowing the user to specify any required data and then run the flow.

To use the sample, you must substitute the ID of the Flow you want to run. This ID is contained within the `customRowAction` attribute inside the `button` element.

Aby uzyskać identyfikator przepływu:

1. Kliknij _Flow_ > _See your flows_ na liście SharePoint, na której skonfigurowano przepływ
2. Kliknij przepływ, który chcesz uruchomić
3. Skopiuj identyfikator z końca adresu URL

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
- Ten format można zastosować do any column type (its value is ignored)
- The list is expected to have an associated Flow, the ID of this flow needs to be included in the `actionParams` for the button

> Wskazówka: możesz zastosować ten format do kolumny obliczeniowej z formułą `=""`. Dzięki temu pole nie będzie częścią formularzy nowego elementu ani edycji.

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-start-flow.json | [Yannick Borghmans](https://github.com/yborghmans)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|25 listopada 2017|Wersja początkowa
1.1|22 stycznia 2018|Adjusted actionParams markup
1.2|18 sierpnia 2018|Icon is now included in button and theme colors are used

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
Ta próbka jest również opisana w głównej dokumentacji dotyczącej formatowania kolumn

Podobny kreator znajduje się także w webparcie [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md), który pozwala na pełne dostosowanie.

- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-start-flow" />
