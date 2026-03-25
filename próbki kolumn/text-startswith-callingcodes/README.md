# Text StartsWith Calling Codes

## Podsumowanie
Ta próbka pokazuje using the `indexOf` function (O365 only) to test if text starts with a given value. Using the international calling code at the start of a phone number, the correct country's flag is shown next to the phone number. The same nested conditionals are also used for the tooltip.

![zrzut ekranu próbki](./assets/screenshot.png)

The `indexOf` function returns the index where a given value is found within a string (indexes start at 0). If the value is not found in the text, the result is -1.

To evaluate if text "startsWith" a given value, we want to know if the index of the value within the string is 0 (at the beginning). So we can use the function like this:

`"=if(indexOf(@currentField,'A')==0, 'Yes', 'No')"`

Some example values and the result using the function above:
`@currentField`|result
---|---
A dog | Yes
a dog | No
Pet A dog | No

Notice that the `indexOf` function is **case-sensitive**. You can do a case-insensitive check by adding the `toLowerCase` function like this:

`=if(indexOf(toLowerCase(@currentField),'a')==0, 'Yes', 'No')`

## Wymagania wstępne

[External image sources are blocked](https://learn.microsoft.com/sharepoint/dev/declarative-customization/formatting-syntax-reference#img-src-security) by default in the custom formatter. To allow external images, you must [add the domain to HTML Field Security](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b). The domain that needs to be added in this sample is `flagcdn.com`.

![screenshot of HTML Field Security](./assets/html-field-security.png)

## Wymagania widoku
- Ten format można zastosować do a Text or Choice column
- This format uses operators only available in SharePoint Online and cannot be used in SharePoint 2019

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
text-startswith-callingcodes.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|February 5, 2019|Wersja początkowa
1.1|September 29, 2023|Dodano note about HTML Field Security and [changed domain from flags.fmcdn.net to flagcdn.com](https://flags.fmcdn.net/)

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
- [Użyj formatowania kolumn do dostosowania SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)

The `indexOf` function is not available in SharePoint 2019

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/text-startswith-callingcodes" />
