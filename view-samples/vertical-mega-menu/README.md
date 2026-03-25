# Vertical Mega Menu

## Podsumowanie

This sample demonstrates the use of multi lines of text column value and the `split` operator to display a vertical mega menu.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

|Type                |Internal Name|Wymagane|
|--------------------|-------------|:------:|
|Pojedyncza linia tekstu |Title        |Yes     |
|Pojedyncza linia tekstu |Icon         |Yes     |
|Multi lines of text |Menu         |Yes     |

- Set the icon name of [Fluent UI Icons](https://developer.microsoft.com/fluentui#/styles/web/icons) in the `Icon` column.
- Set the `Menu` column to a value like the following.
```
@@@[Header]
>[Link Text]|[URL]
>[Link Text]|[URL]
>[Link Text]|[URL]
@@@[Header]
>[Link Text]|[URL]
>[Link Text]|[URL]
>[Link Text]|[URL]
```

> Note: Do not set `>` and `|`, which are used as delimiters, to [Header] and [Link Text].

- The following is an example of the value of the `Menu` column.
```
@@@Samples
>Power Platform Samples|https://pnp.github.io/powerplatform-samples/
>SharePoint Framework Web Parts|https://pnp.github.io/sp-dev-fx-webparts/
>SharePoint Framework Extensions‍|https://pnp.github.io/sp-dev-fx-extensions/
>SharePoint Framework Viva Adaptive Card Extensions|https://github.com/pnp/sp-dev-fx-aces/
>Script Samples|https://pnp.github.io/script-samples/
>Teams Apps Samples|https://pnp.github.io/teams-dev-samples/
>Office Add-ins PnP|https://github.com/OfficeDev/Office-Add-in-samples/
>Microsoft 365 Learning Pathways|https://github.com/pnp/custom-learning-office-365/
>List Formatting Samples|https://pnp.github.io/List-Formatting/
>Library Component Samples & Tutorials|https://github.com/pnp/sp-dev-fx-library-components/
@@@Solutions
>SharePoint Look Book|https://lookbook.microsoft.com/
>Teams App Templates|https://learn.microsoft.com/microsoftteams/platform/samples/app-templates/
>PnP Modern Search|https://microsoft-search.github.io/pnp-modern-search/
>SharePoint Starter Kit‍|https://github.com/pnp/sp-starter-kit/
```

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
vertical-mega-menu.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Version |Data              |Uwagi
--------|------------------|--------------------------------
1.0     |grudnia 13, 2022 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

## Dodatkowe uwagi
- [Fluent UI Icons](https://developer.microsoft.com/fluentui#/styles/web/icons)

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/vertical-mega-menu" />