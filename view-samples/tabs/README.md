# Tabs

## Podsumowanie
This sample creates tabs with associated content. Users can then navigate between tabs. This sample is intended to display content within a SharePoint page (using the lists webpart) to provide a more interactive and user friendly approach.

You can include the tab header, icon (or URL to an image), content, and link redirection for more information. By using views, you can filter to only display specific list items to allow the list to power multiple tabs on different pages.

![zrzut ekranu próbki](./assets/screenshot.gif)

> Note - the active tab is stored with the list item meaning that changes on the active tab position will affect ALL users.

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
TabHead1 | Pojedyncza linia tekstu  - Tab name
Tab1Desc | Wiele linii tekstu - Description of Tab content
Tab1Icon | Pojedyncza linia tekstu - Icon name or url to image
TabUrl1 | Pojedyncza linia tekstu  - url to "more info" button
TabHead2 | Pojedyncza linia tekstu 
Tab2Desc | Wiele linii tekstu
Tab2Icon | Pojedyncza linia tekstu 
TabUrl2 | Pojedyncza linia tekstu 
TabHead3 | Pojedyncza linia tekstu 
Tab3Desc | Wiele linii tekstu
Tab3Icon | Pojedyncza linia tekstu 
TabUrl3 | Pojedyncza linia tekstu 
TabHead4 | Pojedyncza linia tekstu 
Tab4Desc | Wiele linii tekstu
Tab4Icon | Pojedyncza linia tekstu 
TabUrl4 | Pojedyncza linia tekstu 
TabHead5 | Pojedyncza linia tekstu 
Tab5Desc | Wiele linii tekstu
Tab5Icon | Pojedyncza linia tekstu 
TabUrl5 | Pojedyncza linia tekstu 
Position | Liczba - Tab position selected

## Filter Tab to display content

Since is possible to create multiple tabs, using the view capabilties can filter each view to only display associated tab and then include in associated SharePoint page.

Access to View edit option and access to "**Filter**" area, check "**Show items only when the following is true:**" and select column and content to be filter to only display associated tabs.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
tabs.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|17 lutego 2022|Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/tabs" />
