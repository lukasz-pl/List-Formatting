# FAQs

## Podsumowanie
This sample creates a theme-aware format to use when displaying FAQs (Frequently Asked Questions).

![zrzut ekranu próbki](./assets/screenshot.png)

### faqs-with-keywords.json

An advanced version of the sample is also included that allows specific keywords within the answer to be turned into links.

The Keyword field is used to match a value in the Answer column, and adds a hyperlink from the KeywordLink field to that value in the Answer column. In the below example, the formatting will change the "information" column in the Answer field, to a hyperlink linking to https://www.microsoft.com

* Title - "What's the difference between 32-bit and 64-bit versions of windows?"
* Answer - "The terms 32-bit and 64-bit refer to the way a computer's processor (also called a CPU) handles information. The 64-bit version of Windows handles large amounts of random access memory (RAM) more effectively than a 32-bit system. Not all devices can run the 64-bit versions of Windows."
* Keyword - "Information"
* KeywordLink - "https://www.microsoft.com"

![zrzut ekranu the sample with keywords](./assets/screenshotWithKeywords.png)

## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Multiple line of text|Answer|Tak|
|Pojedyncza linia tekstu|Keyword||
|Hiperłącze|KeywordLink||

> The last 2 columns are only needed when using the keywords version of the format.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
faqs.json | [Chris Kent](https://github.com/thechriskent)
faqs-with-keywords.json | [Chris Kent](https://github.com/thechriskent)


## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|1 marca 2020|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/faqs" />
