# Book Template Card Formatter

## Podsumowanie

This SharePoint JSON view formatting sample transforms your list items into visually rich book cards. Each card displays a book cover, title, author, price, category, release date, best seller badge, and more. It is ideal for book catalogues, libraries, or online bookstore lists.

![zrzut ekranu próbki](./assets/screenshot.png)

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

| Column Name      | Type                   | Description                                 |
|------------------|------------------------|---------------------------------------------|
| Tytuł            | Pojedyncza linia tekstu    | Book title                                  |
| Autor            | Pojedyncza linia tekstu    | Author of the book                          |
| Opis     | Wiele linii tekstu | Short extract or summary of the book        |
| Kategoria         | Pojedyncza linia tekstu    | Book category (e.g., Fantasy, Classic)      |
| Cena            | Pojedyncza linia tekstu    | Price of the book                           |
| Okładka     | Pojedyncza linia tekstu    | URL to the book cover image                 |
| Best seller     | Yes/No                 | Indicates if the book is a best seller      |
| Przeczytano      | Data i godzina          | Book release date                           |
| Opis od redakcji   | Pojedyncza linia tekstu    | Link to find the book in a store (e.g., map)|
| Dodaj do kart        | Yes/No                 | Add to cart flag                            |

> [!NOTE]
> - When using an external image URL in the `BookCoverUrl` column, the image may not be displayed. This happens when attempting to retrieve images from a domain that is not allowed. you'll need to configure the HTML Field Security settings. For more details, refer to [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b).
> - A [PowerShell Script](./assets/Create%20List.ps1) is provided in the assets folder to provision the list and add sample data.
> - This script uses [PnP PowerShell](https://pnp.github.io/powershell/) and requires an environment ready for PnP PowerShell.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
book-template.json | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|Aug 31, 2025|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- This sample includes a visually rich card layout for books, with best seller highlighting and store location links.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/book-template" />
