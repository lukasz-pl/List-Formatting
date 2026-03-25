# Nagłówek planu wydarzenia

## Podsumowanie
Ta próbka pokazuje niestandardowy nagłówek formularza elementu używanego w szablonie listy „Event itinerary”.

![zrzut ekranu próbki](./assets/screenshot.png)

Ten format jest przeznaczony do sekcji Header Format w panelu Configure Layout formularza. Układ treści widoczny na zrzucie ekranu można uzyskać przez skonfigurowanie sekcji w panelu Body, ale nie jest to częścią tego formatu.

## Wymagania formularza

Poniższe pola są dostępne w szablonie „Event itinerary”. Szablon znajdziesz w oknie tworzenia nowej listy:

![obraz szablonu listy](./assets/listtemplates.png)

|Typ                    |Nazwa wewnętrzna|Wymagane|
|-----------------------|----------------|:------:|
|Pojedyncza linia tekstu|Title           |Tak     |
|Wiele linii tekstu     |Description     |Nie     |
|Pojedyncza linia tekstu|SessionCode     |Nie     |
|Wybór                  |SessionType     |Nie     |
|Osoba lub grupa        |Speakers        |Nie     |
|Data i godzina         |StartDateAndTime|Nie     |
|Data i godzina         |EndDateAndTime  |Nie     |
|Obliczeniowe           |Duration        |Nie     |
|Liczba                 |Capacity        |Nie     |
|Wybór                  |Location        |Nie     |
|Wiele linii tekstu     |Notes           |Nie     |

## Przykład

Rozwiązanie|Autor(zy)
-----------|---------
event-itinerary-header.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Wersja |Data             |Uwagi
-------|-----------------|-----
1.0     |January 31, 2021 |Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/form-samples/event-itinerary-header" />
