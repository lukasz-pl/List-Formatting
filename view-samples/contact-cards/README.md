# Contact Cards

## Podsumowanie
This is a sample of a complex format that customizes the entire display of a row. The goal is to illustrate several key principals including:
- Responsive layout through flexbox
- Conditionally showing elements based on fields having values
- Providing placeholders when fields are blank
- Row Actions
  - Opening the information panel (`defaultClick`)
  - Editing the list item (`editProps`)
  - Deleting the list item (`delete`)
  - Sharing the list item (`share`)
- Use of theme color classes to ensure the format displays as intended regardless of theme (light, dark, custom, etc.)
- Use of font size and weight classes to match O365 styles
- Integration of maps
- Disabling of selection (`hideSelection`)
- Removal of the list header (`hideListHeader`)

![zrzut ekranu próbki](./assets/screenshot.png)

### Klucz API map

Klucz podany w szablonie (ten mało estetyczny tekst po `&key`) należy zmienić na własny, BEZPŁATNY klucz API. Dzięki temu unikniesz błędów wynikających z nadmiernego użycia współdzielonego klucza. Uzyskanie klucza zajmuje 2 minuty i jest BEZPŁATNE: [Pobierz klucz API](https://developers.google.com/maps/documentation/static-maps/get-api-key)

>Uwaga: pozostawienie tego klucza bez zmiany na własny może w przyszłości powodować problemy, gdy inni użytkownicy będą go używać albo gdy zostanie unieważniony.

## Podgląd mapy się nie wyświetla?
Najprawdopodobniej musisz włączyć zabezpieczenia pól HTML w swojej witrynie. Szczegóły znajdziesz tutaj: [Zezwalanie lub ograniczanie możliwości osadzania zawartości na stronach SharePoint](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b)

## Wymagania widoku

Wszystkie poniższe pola powinny być częścią widoku, ale tylko te oznaczone jako Wymagane muszą mieć wartości:

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Pojedyncza linia tekstu|JobTitle||
|Pojedyncza linia tekstu|Company||
|Pojedyncza linia tekstu|Email||
|Pojedyncza linia tekstu|Phone||
|Pojedyncza linia tekstu|StreetAddress||
|Pojedyncza linia tekstu|City||
|Pojedyncza linia tekstu|State||
|Pojedyncza linia tekstu|ZipCode||
|Hiperłącze|Picture||
|Wiele linii tekstu|Notes||

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
contact-cards.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|22 sierpnia 2018|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

Ten format wykorzystuje CSS Flexbox, aby lepiej działał responsywnie:

![Responsive Screenshot](./assets/screenshotResponsive.png)


<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/contact-cards" />
