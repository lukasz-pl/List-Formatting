# Dwukolumnowy nagłówek z logo

## Podsumowanie

Ta próbka wyświetla `Icon` i `Title` w dwukolumnowym nagłówku, z ikoną po lewej i `Title` po prawej. Dodatkowa `Icon` oraz `RequestStatus` są wyświetlane pod `Title`.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania formularza

|Typ                    |Nazwa wewnętrzna|Wymagane|
|-----------------------|----------------|:------:|
|Pojedyncza linia tekstu|Title           |Tak     |
|Wybór                  |RequestStatus   |Tak     |

### Wartości RequestStatus

|Wartość         |
|----------------|
|Approved|
|Pending|
|Rejected|
|Withdrawn|

Na podstawie wartości `RequestStatus` zmieniany jest kolor kolumny oraz ikona.

- RequestStatus: Domyślny (nie wybrano)

    ![zrzut ekranu próbki, gdy RequestStatus jest puste](./assets/screenshot_two_column_Default.png)

- RequestStatus: Approved

    ![zrzut ekranu próbki, gdy RequestStatus to Approved](./assets/screenshot_two_column_Approved.png)

- RequestStatus: Pending

    ![zrzut ekranu próbki, gdy RequestStatus to Pending](./assets/screenshot_two_column_Pending.png)

- RequestStatus: Rejected

    ![zrzut ekranu próbki, gdy RequestStatus to Rejected](./assets/screenshot_two_column_Rejected.png)

- RequestStatus: Withdrawn

    ![zrzut ekranu próbki, gdy RequestStatus to Withdrawn](./assets/screenshot_two_column_Withdrawn.png)

## Logo

Logo w tej próbce korzysta z `CRMCustomerInsightsApp` z [Fluent UI Icons](https://developer.microsoft.com/en-us/fluentui#/styles/web/icons).

## Przykład

Rozwiązanie|Autor(zy)
-----------|---------
two-column-logo-header.json | [Andrew Burns](https://github.com/GeorgiaGit)

## Historia wersji

Wersja |Data              |Uwagi
-------|------------------|-----
1.0     |July 14, 2024  |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/form-samples/two-column-logo-header" />
