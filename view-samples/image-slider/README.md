# Image Slider

## Podsumowanie
This sample display images as a slider with navigation to the next image.

![zrzut ekranu próbki](./assets/screenshot.gif)

> The image to display is determined by the `UpdateState` column where the order to display is stored. This is updated by the format for **All** users.

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
url | Pojedyncza linia tekstu  - url of image
UpdateState | Pojedyncza linia tekstu - this field will be used order the images

### Edit View requirements

   - **Sort**: sort by `UpdateState` in ascending order
   - **Item Limit**: Edit the view and set _"Liczba of items to display"_ to **1** and check option _"Limit the total number of items returned to the specified amount."_

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
image-slider.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|08 grudnia 2021|Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/image-slider" />
