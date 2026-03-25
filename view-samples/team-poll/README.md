# Team Poll

## Podsumowanie
This sample combines a couple of lists and a few formats to demonstrate creating an application using view formatting. The end result is a configurable poll that end users can submit their choices too and view grouped results.

An optional Power Automate flow is also presented below to ensure that as Team Members are added to the Office 365 Group a response list item is configured automatically for them.

![zrzut ekranu próbki](./assets/screenshot.png)

![zrzut ekranu the poll response](./assets/screenshotPollResponse.png)

## Wymagania widoku

### Poll list

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Pojedyncza linia tekstu|Question|Tak|
|Pojedyncza linia tekstu|Option1|No
|Pojedyncza linia tekstu|Option2|No
|Pojedyncza linia tekstu|Option3|No
|Pojedyncza linia tekstu|Color1|No
|Pojedyncza linia tekstu|Color2|No
|Pojedyncza linia tekstu|Color3|No
|Liczba|Iteration|Yes

### Poll Responses list

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Person|User|Nie|
|Lookup|Poll|Tak|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Option_x0020_1|Nie|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Option_x0020_2|Nie|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Option_x0020_3|Nie|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Color_x0020_1|Nie|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Color_x0020_2|Nie|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Color_x0020_3|Nie|
|Additional Column from Poll Lookup|Poll_x003a__x0020_Iteration|Nie|
|Liczba|ResponseIteration|Nie|
|Pojedyncza linia tekstu|Selection|Nie|
|Pojedyncza linia tekstu|SelectionwithColor|Nie|

> Those ugly names are automatically created when we select the additional columns when configuring the Poll lookup column. Fun!

> [!NOTE]  
> When using `team-poll-results.json`, it is necessary to group by the `SelectionwithColor` column.

## Flow Prompt

"When a Horse is added or removed from an Office 365 Group, look up the user's profile, and then create a list item in SharePoint"

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
team-poll.json | [Chris Kent](https://github.com/thechriskent)
team-poll-configuration.json | [Chris Kent](https://github.com/thechriskent)
team-poll-response.json | [Chris Kent](https://github.com/thechriskent)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|3 sierpnia 2023|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/team-poll" />