# Nagłówek i stopka statusu

## Podsumowanie
Ta próbka pokazuje niestandardowy nagłówek i stopkę formularza z kolumną Status o możliwych wartościach `Thinking about it`, `Working on it`, `Done` oraz `Nevermind`.

Ten format jest przeznaczony do sekcji Header Format i Footer Format treści formularza w panelu Configure Layout. W zależności od wartości kolumny Status używana jest odpowiednia ikona i kolorystyka.

![zrzut ekranu próbki](./assets/screenshot.png)

![zrzut ekranu próbki](./assets/status-workingonit.png)

![zrzut ekranu próbki](./assets/status-done.png)

![zrzut ekranu próbki](./assets/status-nevermind.png)


## Wymagania formularza

Wymagana jest kolumna wyboru o nazwie Status z możliwymi wartościami `Thinking about it`, `Working on it`, `Done` oraz `Nevermind`.

![obraz kolumny listy](./assets/status-column.png)

|Typ                    |Nazwa wewnętrzna|Wymagane|
|-----------------------|----------------|:------:|
|Pojedyncza linia tekstu|Title           |Tak     |
|Wybór                  |Status          |Nie     |


## Przykład

Rozwiązanie|Autor(zy)
-----------|---------
status-footer.json | [Chris Kent](https://github.com/thechriskent)
status-header.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja |Data             |Uwagi
-------|-----------------|-----
1.0     |January 31, 2021 |Wersja początkowa
2.0     |August 20, 2021 |Dodano README i zrzuty ekranu

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/form-samples/status-header-footer" />
