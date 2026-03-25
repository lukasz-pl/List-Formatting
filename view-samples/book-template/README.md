# Book Template Table Formatter

## Podsumowanie

Ten szablon formatuje widok Microsoft Lists / SharePoint tak, aby kazdy rekord ksiazki byl pokazany jako elegancka karta z tabela danych po polsku. Widok eksponuje okladke, tytul, autora, kategorie, cene, date wydania, status bestsellera, opis oraz akcje dla uzytkownika.

![zrzut ekranu probki](./assets/screenshot.png)

## Co zostalo zmienione

- Etykiety i teksty interfejsu sa po polsku.
- Glowna czesc rekordu ma uklad tabelaryczny.
- Przyciski akcji sa opisane po polsku.
- Widok jest przygotowany do uzycia w Microsoft Lists.

## Wymagane kolumny

Utworz w liscie ponizsze kolumny. Nazwy wewnetrzne musza odpowiadac polom uzytym w JSON.

| Nazwa wyswietlana | Nazwa wewnetrzna | Typ kolumny | Opis |
|---|---|---|---|
| Tytul | `Title` | Pojedyncza linia tekstu | Tytul ksiazki |
| Autor | `BookAuthor` | Pojedyncza linia tekstu | Autor ksiazki |
| Opis | `BookAbstract` | Wiele linii tekstu | Krotki opis ksiazki |
| Kategoria | `Category` | Pojedyncza linia tekstu | Np. Fantasy, Biznes, Klasyka |
| Cena | `Price` | Pojedyncza linia tekstu | Cena, np. `49.90` |
| Okladka URL | `BookCoverUrl` | Pojedyncza linia tekstu | Link do obrazu okladki |
| Bestseller | `IsBestSeller` | Tak/Nie | Czy ksiazka jest bestsellerem |
| Data wydania | `ReleaseDate` | Data i godzina | Data publikacji |
| Link do sklepu | `FindInStoreUrl` | Pojedyncza linia tekstu | Link do sklepu lub lokalizacji |
| W koszyku | `AddToCart` | Tak/Nie | Flaga przelaczana przyciskiem |

## Jak wdrozyc w Microsoft Lists

1. Otworz swoja liste w Microsoft Lists.
2. Dodaj kolumny wymienione w sekcji "Wymagane kolumny".
3. Wejdz w widok listy, ktory chcesz sformatowac.
4. Kliknij `View options` / `Opcje widoku`.
5. Wybierz `Format current view` / `Formatuj biezacy widok`.
6. Kliknij `Advanced mode` / `Tryb zaawansowany`.
7. Otworz plik [book-template.json](/Users/lukasz_preihs/Documents/GitHub/List-Formatting/view-samples/book-template/book-template.json).
8. Skopiuj cala zawartosc pliku JSON i wklej do okna formatowania.
9. Zapisz zmiany przyciskiem `Save`.

## Jak przetestowac

1. Dodaj kilka rekordow ksiazek z uzupelnionymi polami.
2. Upewnij sie, ze `BookCoverUrl` wskazuje na publicznie dostepny obraz.
3. Kliknij `Dodaj do koszyka`, aby sprawdzic, czy pole `AddToCart` zmienia wartosc.
4. Kliknij `Znajdz w sklepie`, aby sprawdzic, czy link otwiera sie poprawnie.

## Uwagi

- Jezeli obrazy z `BookCoverUrl` nie wyswietlaja sie, przyczyna moze byc blokada zewnetrznej domeny przez SharePoint HTML Field Security.
- Do szybkiego przygotowania listy mozesz wykorzystac skrypt [Create List.ps1](/Users/lukasz_preihs/Documents/GitHub/List-Formatting/view-samples/book-template/assets/Create%20List.ps1), ale przed uruchomieniem warto dopasowac adres witryny i dane probne.
- W JSON pole daty to `ReleaseDate`. Upewnij sie, ze w liscie kolumna ma dokladnie taka nazwe wewnetrzna.

## Probka

Rozwiazanie | Autor(zy)
---|---
`book-template.json` | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja | Data | Uwagi
---|---|---
1.1 | 2026-03-25 | Widok zmieniony na polski uklad tabelaryczny oraz dodana instrukcja wdrozenia do Microsoft Lists
1.0 | 2025-08-31 | Wersja poczatkowa

## Zastrzezenie

**TEN KOD JEST DOSTARCZANY W STANIE TAKIM, W JAKIM JEST, BEZ JAKIEJKOLWIEK GWARANCJI.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/book-template" />
