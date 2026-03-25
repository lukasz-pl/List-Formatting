# IMDb Card

## Podsumowanie

This sample transforms list items into cards formatted with IMDb (Internet Movie Database) Movie listing layout. To ensure the view functions correctly, make sure all specified columns are included. The icons are referenced from [Fluent UI Icons](https://developer.microsoft.com/en-us/fluentui#/styles/web/icons).

![zrzut ekranu próbki](./assets/screenshot.png)

The Director and Actor names are hyperlinks so that you can leverage them to filter other movies where they might have featured. If you set the `href` as follows, the link to the filtered view will be displayed:

```
"href": "=@currentWeb+'/Lists/<<ListName>>'+'/'+'<<ViewName>>.aspx?FilterField1=<<InternalNameOfColumn>>&FilterValue1='+[$<<InternalNameOfColumnToBeUsedForFilter>>]"
```

For example:

```
"href": "=@currentWeb+'/Lists/MovieCast'+'/'+'AllItems.aspx?FilterField1=Title&FilterValue1='+[$Actor1]"
```

![zrzut ekranu the filtered view](./assets/filtered-view.png)

You can achieve that by using query strings as described in [this blog](https://sudeepghatak.com/using-hyperlinks-in-list-view-json-to-apply-filters/).

## Wymagania widoku

Column Name                 | Type
----------------------------|-----------------------------------------
Title                       | Pojedyncza linia tekstu
Year                        | Pojedyncza linia tekstu
Duration                    | Pojedyncza linia tekstu
Rating                      | Choice (PG,R,A)
VoteCount                   | Liczba
Metascore                   | Liczba
Director                    | Pojedyncza linia tekstu
Actor1                      | Pojedyncza linia tekstu
Actor2                      | Pojedyncza linia tekstu
Actor3                      | Pojedyncza linia tekstu
MovieImage                  | Hiperłącze or Picture

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
imdb-card.json | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|22 lipca 2024|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- Query string is also described in the following document:

    [Query String URL Tricks for SharePoint and Microsoft 365 - Filtering and sorting modern SharePoint and Microsoft Lists views](https://learn.microsoft.com/microsoft-365/community/query-string-url-tricks-sharepoint-m365#filtering-and-sorting-modern-sharepoint-and-microsoft-lists-views)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/imdb-card" />