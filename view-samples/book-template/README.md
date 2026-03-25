# Book Template Table Formatter

## Podsumowanie

Ten szablon formatuje widok Microsoft Lists / SharePoint tak, aby kazdy rekord ksiazki byl pokazany jako elegancka karta z tabela danych po polsku. Widok eksponuje okladke, tytul, autora, kategorie, cene, date wydania, status bestsellera, opis oraz akcje dla uzytkownika.

![zrzut ekranu probki](./assets/screenshot.png)

## Wymagania widoku

### SharePoint List Columns

| Column Name      | Type                   | Description                                 |
|------------------|------------------------|---------------------------------------------|
| Title            | Pojedyncza linia tekstu    | Book title                                  |
| BookAuthor       | Pojedyncza linia tekstu    | Author of the book                          |
| BookAbstract     | Wiele linii tekstu | Short extract or summary of the book        |
| Category         | Pojedyncza linia tekstu    | Book category (e.g., Fantasy, Classic)      |
| Price            | Pojedyncza linia tekstu    | Price of the book                           |
| BookCoverUrl     | Pojedyncza linia tekstu    | URL to the book cover image                 |
| IsBestSeller     | Yes/No                 | Indicates if the book is a best seller      |
| ReleaseData      | Data i godzina          | Book release date                           |
| FindInStoreUrl   | Pojedyncza linia tekstu    | Link to find the book in a store (e.g., map)|
| AddToCart        | Yes/No                 | Add to cart flag                            |

> [!NOTE]
> - When using an external image URL in the `BookCoverUrl` column, the image may not be displayed. This happens when attempting to retrieve images from a domain that is not allowed. you'll need to configure the HTML Field Security settings. For more details, refer to [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b).
> - A [PowerShell Script](./assets/Create%20List.ps1) is provided in the assets folder to provision the list and add sample data.
> - This script uses [PnP PowerShell](https://pnp.github.io/powershell/) and requires an environment ready for PnP PowerShell.

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
