# Color Picker

## Podsumowanie

This sample contains pre defined palettes of color as listed here: [color enumeration in Power Apps](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/functions/function-colors). These palettes are then made available as a color picker setting the value on selection. 2 additional color palettes, **"12 sections"** and **"Basic"**, are also provided as separate formats.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Main sample (color-picker.json)

This format allow users to select up to 140 colors existing in Power Apps, it's also possible to select what colors can be displayed using the field `ColorF` as filter and include only the names of the colors you wish to include. Fot instance: `red,azure,gold`.

![color picker format](./assets/ColorPickerFilter.PNG)

> If `ColorF` is empty then all 140 colors are displayed. 

## Wymagania widoku
- The format expect the following fields:

Field |Type
--------|---------
Title | Pojedyncza linia tekstu 
ColorP | Single lines of text
ColorF | Single lines of text

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
color-picker.json | [André Lage](https://github.com/aaclage)
color-picker-12Sections-palette.json | [André Lage](https://github.com/aaclage)
color-picker-basic-palette.json | [André Lage](https://github.com/aaclage)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|17 stycznia 2022|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi
None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/color-picker" />