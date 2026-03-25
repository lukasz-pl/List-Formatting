# Photo Gallery with Likes

## Podsumowanie

This sample demonstrates formatting a document library gallery view into a photo gallery showing title and likes.

![zrzut ekranu próbki](./assets/screenshot.gif)

There is also a version that has no title and shows only likes.

![zrzut ekranu próbki](./assets/screenshot-no-title.png)

## Wymagania widoku

The view must be set to gallery.  
This format expects the following columns to be part of the view:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|No
|Liczba|LikesTotal|No
|Multi-Person|LikedBy|No

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
photo-gallery-with-likes.json | [Lou-i3](https://github.com/Lou-i3)
photo-gallery-no-title.json | [Lou-i3](https://github.com/Lou-i3)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|21 października 2022|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

The file name can also be displayed by setting the `txtContent` property as follows.

```
"txtContent": "=substring('[$FileLeafRef]',0,lastIndexOf([$FileLeafRef],'.'))"
```

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/photo-gallery-with-likes" />