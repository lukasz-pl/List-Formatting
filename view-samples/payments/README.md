# Payments

## Podsumowanie
This sample provides a payment list format to register daily expenses, currency, status, rate option, Locations, copy file link, comments and categorization of payment.
Solution has 4 formats Desktop, Mobile, Group by Category and Timeline.

Format includes icon for type of payment, capability to choose currency, expand collapse to view details, payment status and payment date.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
Description | Multiple Line of Text
Category | Choice - Include the following options **"PaymentCard,Bank,Savings,Money,AllCurrency,EatDrink,AirTickets,ShoppingCart,Shop,Home,Health"**
Payment | Liczba  - define number of decimal places to 2
OtherCosts | Liczba - this field will be used order the clipboards
Currency | Choice - Include the following options **"CHF(CHF),€(EUR)£(GBP),$(USD),¥(JPY)"**
PaymentDay | Data & Time
Paid | Yes/No - default value **"No"**
Expand | Yes/No - default value **"No"**
Categorize | Choice - "Red, Blue, Green, Orange, Purple, Yellow"
OtherCostDescription | Pojedyncza linia tekstu 
Rate | Choice - Values from 1 to 5
Location | Location - place where is made the payment
Invoice | Pojedyncza linia tekstu - Save copy link from file

- Replace `[replaceUrlPathtoLibrary]` with path to SharePoint Library, sample: '/SiteAssets/'

### Edit View requirements

- Edit View where format will be included:
   - Access to "**Sort**" Area and select column "**PaymentDay**" and check as **ascending order**, this option order the images based on changed.
   - Include in View the following additional fields "**Created**", "**Modified**" and "**Modified By**".

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
payments.json | [André Lage](https://github.com/aaclage)
payments-mobile.json | [André Lage](https://github.com/aaclage)
payments-grouped.json | [André Lage](https://github.com/aaclage)
payments-format.json | [André Lage](https://github.com/aaclage)
payments-mobile-format.json | [André Lage](https://github.com/aaclage)
payments-timeline-format.json | [André Lage](https://github.com/aaclage)
payments-groupby-format.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
2.0|04 czerwca 2022|New features
1.0|10 stycznia 2022|Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/payments" />
