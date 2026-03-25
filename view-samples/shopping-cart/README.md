# Shopping Cart

## Podsumowanie

The JSON template is designed for an online shopping cart. It displays items within the cart, including product details, pricing, shipping information, and user interactions like adding or removing items.

Clicking on 'Add to Cart' updates the 'AddedToCart' field to true and changes the display text to 'Remove from Cart'

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

Column Name               | Type
--------------------------|----------------------------------------
Title                     | Pojedyncza linia tekstu
Description               | Wiele linii tekstu
Price                     | Currency (Liczba of decimal places=2)
OldPrice                  | Currency
ImageUrl                  | Pojedyncza linia tekstu
Offer                     | Pojedyncza linia tekstu
CalculatedPrice           | Calculated (calculation based on other columns)(Formula = `=ROUND(Price,2)`) (Type = 'Pojedyncza linia tekstu')
PriceDifference           | Calculated (calculation based on other columns)(Formula = `=OldPrice-Price`) (Type = 'Pojedyncza linia tekstu')
Rating                    | Liczba
DollarValue               | Calculated (calculation based on other columns)(Formula = `=INT(Price)`) (Type = 'Pojedyncza linia tekstu')
CentsValue                | Calculated (calculation based on other columns)(Formula = `=TEXT(ROUND((Price-INT(Price))*100,0),"00")`)(Type = 'Pojedyncza linia tekstu')
QuantitySold              | Liczba
AddedToCart               | Yes/No
Shipping                  | Currency

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
shopping-cart.json | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|11 września 2024|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/shopping-cart" />