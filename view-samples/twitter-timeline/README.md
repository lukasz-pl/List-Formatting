# Twitter Timeline

## Podsumowanie
This sample formats your SharePoint list view to look like Twitter. If you are using the Microsoft Flow Templates to track tweets in a SharePoint list, this is a great way to format your list so that it looks more like Twitter. For more info on Flow Templates that take Tweets and add them to a SharePoint list check out this template: https://us.flow.microsoft.com/en-us/galleries/public/templates/e78571e5c70e4806a18eeacba5a897c8/save-tweets-that-include-a-specific-hashtag-to-a-sharepoint-list/

This sample features the following:
- Responsive layout through flexbox
- Shows the number of retweets
- Share icon which takes you to the Tweet in Twitter so you can like, retweet, etc
- The Person's name is a hyperlink to their Profile
- Pulls in Twitter Profile Pictures

![zrzut ekranu próbki](./assets/screenshot.png)

Screen Capture of working Links

![Twitter Format Screenshot](./assets/SPTwitter.gif)


## Wymagania widoku

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Pojedyncza linia tekstu|TweetBy|Tak|
|Pojedyncza linia tekstu|TweetByFullName|Tak|
|Data Time|TweetData|Tak|
|Calculated Column|TweetFormattedData|Tak|
|Hiperłącze|TwitterProfilePic|Tak|
|Hiperłącze|ProfileLink|Tak|
|Hiperłącze|LinkToTweet|Tak|
|Multi Line of Text|FullTweet|Tak|
|Liczba|NumbRetweets|Tak|

You need the `TweetFormattedData` Calculated Column so that it only shows the current month name spelled out and date (not the year or time). The formula for this calculated column is below:

`=TEXT(TweetData,"mmm d")`


## Próbka

Rozwiązanie|Autor(zy)
--------|---------
twitter-timeline.json | [kwietnia Dunnam](https://github.com/aprildunnam)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|sierpnia 2, 2019 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/twitter-timeline" />
