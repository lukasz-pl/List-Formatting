# Text Contains

## Podsumowanie
Ta próbka pokazuje using the `indexOf` function (O365 only) to test if text contains a given value. Próbka also uses the `toLowerCase` function to ensure the contains condition is case-insensitive. In this sample, if the text of the current field contains the word _"dead"_ a class is applied to turn the text red.

![zrzut ekranu próbki](./assets/screenshot.png)

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

## Wymagania widoku
- Ten format można zastosować do a Text or Choice column
- Ten format używa operatorów dostępnych wyłącznie w SharePoint Online i nie może być używany w SharePoint 2019

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
text-contains.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|5 lutego 2019|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

The `indexOf` and `toLowerCase` functions are not available in SharePoint 2019

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/text-contains" />
