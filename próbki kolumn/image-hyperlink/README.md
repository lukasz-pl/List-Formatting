# Zmiana standardowego zachowania hiperłącza obrazu

## Podsumowanie
Jeśli klikniesz obraz na liście SharePoint, zostanie on wyświetlony jako podgląd. Ten formatter zmienia standardowe zachowanie tak, aby używany był link z innej kolumny. Dzięki temu kliknięcie obrazu działa tak samo, jak bezpośrednie kliknięcie linku.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku
- Kolumna typu obraz zawierająca ten formatter kolumny
- Kolumna hiperłącza (nazwa wewnętrzna: `Link`) zawierająca link docelowy.

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
image-hyperlink.json | [Hagen Deike](https://github.com/samurai-ka) ([@samurai@sueden.social](https://sueden.social/@samurai))

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|21 listopada 2024|Wersja początkowa
1.1|21 listopada 2024|Użycie opisu linku kolumny zamiast tytułu

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- Zmień rozmiar obrazu w linii 21
- Aby usunąć zaokrąglone rogi, usuń styl obrazu w liniach 24-26
- Odstępy między wierszami można dostosować w liniach 6 i 7
- W linii 14 wybierz sposób otwierania linku w przeglądarce: `"_blank"` dla nowego okna lub karty albo `"_self"` dla tego samego okna.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/image-hyperlink" />