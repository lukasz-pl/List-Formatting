# Flight Card

## Podsumowanie

This sample transforms list items into cards formatted with flight information layouts. To ensure the view functions correctly, make sure all specified columns are included. The icons are referenced from [Fluent UI Icons](https://developer.microsoft.com/en-us/fluentui#/styles/web/icons).

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

Column Name                 | Type
----------------------------|-----------------------------------------
Title                       | Pojedyncza linia tekstu
From                        | Pojedyncza linia tekstu
To                          | Pojedyncza linia tekstu
SourceTime                  | Data i godzina
DestinationTime             | Data i godzina
Source Airport              | Pojedyncza linia tekstu
Destination Airport         | Pojedyncza linia tekstu
SourceTerminal              | Pojedyncza linia tekstu
DestinationTerminal         | Pojedyncza linia tekstu
Airline                     | Pojedyncza linia tekstu
FlightNo                    | Pojedyncza linia tekstu
Carrier                     | Pojedyncza linia tekstu
Class                       | Choice (Economy,Business,Premium Economy)
Currency                    | Pojedyncza linia tekstu
Price                       | Liczba
PriceLabel                  | Pojedyncza linia tekstu
SourceCode                  | Pojedyncza linia tekstu
DestinationCode             | Pojedyncza linia tekstu
SourceTimeOnly              | Calculated (`=TEXT([SourceTime],"HH:mm")`) (Pojedyncza linia tekstu)
DestinationTimeOnly         | Calculated (`=TEXT([DestinationTime],"dd mmm")`) (Pojedyncza linia tekstu)
FormattedSourceData         | Calculated (`=TEXT([SourceTime],"HH:mm")`) (Pojedyncza linia tekstu)
FormattedDestinationData    | Calculated (`=TEXT([DestinationTime],"dd mmm")`) (Pojedyncza linia tekstu)

> [!NOTE]  
> This sample uses a [Calculated column](https://learn.microsoft.com/previous-versions/office/developer/sharepoint-2010/bb862071(v=office.14)). Note that the separator for a Calculated column is either a `,` (comma) or a `;` (semi-colon), depending on the locale. If your locale uses `;` as the separator, please replace `,` with `;` in the formulas above.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
flight-card.json | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|22 lipca 2024|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/flight-card" />
