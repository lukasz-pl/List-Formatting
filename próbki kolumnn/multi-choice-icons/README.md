# Multi-Choice Icons

## Podsumowanie
Ta próbka pokazuje using the `indexOf` and `join` functions (O365 only) to test if a multi-select choice field has a selected choice. Providing icons of the known choices and applying themed colors based on if the given choice is selected or not creates an intuitive, easy to understand visualization that doesn't suffer from varying item order or text formatting issues.

![zrzut ekranu próbki](./assets/screenshot.png)

Ta próbka pokazuje również, jak używać podwójnych cudzysłowów wewnątrz wartości. Aby je dodać, musisz je poprzedzić znakiem ucieczki zgodnie ze składnią JSON, umieszczając ukośnik przed cudzysłowem: `"\"Juice\""`

Funkcja `indexOf` zwraca indeks, pod którym dana wartość została znaleziona w ciągu znaków (indeksy zaczynają się od 0). Jeśli wartość nie zostanie znaleziona w tekście, wynikiem jest -1.

To evaluate if text contains a given value, we want to know if the index of the value within the string is anything but -1. So we can use the function like this:

`"=if(indexOf(@currentField,'dog') != -1, 'Yes', 'No')"`

Kilka przykładowych wartości i wynik działania powyższej funkcji:
`@currentField`|wynik
---|---
A dog | Tak
a Dog | No
dog's are nice | Yes
bark dog bark | Yes

Zwróć uwagę, że funkcja `indexOf` **rozróżnia wielkość liter**. Aby wykonać sprawdzenie bez rozróżniania wielkości liter, możesz dodać funkcję `toLowerCase` w taki sposób:

`"=if(indexOf(toLowerCase(@currentField),'dog') != -1, 'Yes', 'No')"`

When it comes to an array of values (such as a multi-select choice or person column) we can't use `indexOf` directly because it expects a string value. Using it directly on multi-select fields will always result in -1.

We can use the `join` or `toString` functions on the value first and then nest those within the `indexOf` call:

`"=if(indexOf(join(@currentField,''),'dog') != -1, 'Yes', 'No')`

## Wymagania widoku
- Ten format można zastosować do a Multi-Select Choice column
- Ten format używa operatorów dostępnych wyłącznie w SharePoint Online i nie może być używany w SharePoint 2019

### Przykład Choice Values
- Water
- Coffee
- Wine
- Beer
- "Juice"

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
multi-choice-icons.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|5 lutego 2019|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

The `indexOf` and `join` functions are not available in SharePoint 2019

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/multi-choice-icons" />
