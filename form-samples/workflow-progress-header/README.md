# Nagłówek postępu workflow

## Podsumowanie
Ta próbka pokazuje znacznik wyboru dla każdego pola daty, które ma wartość, aby ułatwić zobaczenie osiągniętych etapów.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania formularza

|Typ            |Nazwa wewnętrzna|Wymagane|
|---------------|----------------|:------:|
|Data i godzina |Date1           |Nie     |
|Data i godzina |Date2           |Nie     |
|Data i godzina |Date3           |Nie     |

## Przykład

Rozwiązanie|Autor(zy)
-----------|---------
workflow-progress-header.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Wersja |Data             |Uwagi
-------|-----------------|-----
1.0     |February 1, 2021 |Wersja początkowa
1.1     |April 19, 2024 |Poprawiono użycie `[$ColumnName.displayValue]` zamiast operatora `toLocaleDateString`, aby rozwiązać problem z niewyświetlaniem daty przy niektórych formatach daty.


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/form-samples/workflow-progress-header" />
