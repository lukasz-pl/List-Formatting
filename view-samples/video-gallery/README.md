# Video Gallery

## Podsumowanie
A gallery view of video stored in SharePoint with a card layout showing rich metadata such as title, description, people, tools topics covered, social sharing options like yammer, share and like.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

Column Name   |Type
--------------|--------------
Title         | Single Line Text
Description   | Multi Line Text
Track         | Choice
Session       | Single Line Text
About         | Multi Line Text
Responsible   | Person or Group
Image         | Image
Learning      | Hiperłącze
Yammer        | Hiperłącze
User          | Person or Group
Age           | Calculated (=DATEDIF(Created,TODAY(),"d"))
Tool          | Choice

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
video-gallery.json | [Anand Ragav](https://github.com/anandragav)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|23 listopada 2021|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/video-gallery" />
