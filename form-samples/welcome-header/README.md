# Powitalny nagłówek

## Podsumowanie
Ta próbka pokazuje, jak wyświetlić komunikat powitalny zależny od pory dnia, obraz profilu użytkownika oraz nazwę użytkownika, jeśli została zapisana w adresie e-mail w formacie podobnym do `user.1@[domain].com`.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania formularza

### Format czasu (12-godzinny lub 24-godzinny)

Sprawdź, jakie ustawienia regionalne są używane w witrynie.
- Zwykle domyślną konfigurację można znaleźć przez ikonę w prawym górnym rogu > Informacje o witrynie > Wyświetl wszystkie ustawienia witryny > Ustawienia regionalne, chyba że format czasu jest zarządzany przez administratora **M365**.

![zrzut ekranu formatu czasu](./assets/time-format.png)

### Jak wdrożyć

Przejdź do listy, do której ma zostać zastosowane dostosowanie, edytuj element, otwórz opcje w prawym górnym rogu i wybierz **"Configure layout"**, a następnie wklej JSON dla sekcji **Header**.

![zrzut ekranu konfiguracji formularza listy](./assets/list-form-configuration.png)

Ta informacja jest ważna przy korzystaniu z próbki, ponieważ `12 hours` używa **12:00:00 AM i 12:00:00 PM**, a `24 hours` używa **0:00:00 do 24:00:00**.
- Na tej podstawie (`12 Hours/24 Hours`) możesz użyć odpowiedniego przykładowego JSON-a do testów.

## Przykład

Rozwiązanie|Autor(zy)
-----------|---------
welcome-header.json | [Andre Lage](https://github.com/aaclage)
welcome-header-24hours.json | [Andre Lage](https://github.com/aaclage)

## Historia wersji

Wersja |Data             |Uwagi
-------|-----------------|-----
1.0     |March 14, 2023 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/form-samples/welcome-header" />
