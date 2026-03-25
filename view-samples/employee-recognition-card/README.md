# Employee Recognition Card

## Podsumowanie

This sample acts as a digital shout-out board for your team, built right into SharePoint. It gives employees an easy way to recognize and appreciate each other's hard work. Colleagues can show their support by clicking on emojis to cast their votes.

![zrzut ekranu próbki](./assets/screenshot.gif)

## Wymagania widoku

### 📝 Recommended SharePoint List Columns


| Column Name         | Type                 |
|---------------------|----------------------|
| Title               | Pojedyncza linia tekstu  |
| From                | Person or Group      |
| To                  | Person or Group      |
| Message             | Wiele linii tekstu |
| AwardType           | Choice               |
| Reactions_Medal     | Liczba               |
| Reactions_Heart     | Liczba               |
| Reactions_Clap      | Liczba               |
| DataRecognized      | Data i godzina        |


A PowerShell Script (Create List.ps1) has been provided in the assets folder to provision the list for you.

**Note:** This script uses [PnP PowerShell](https://pnp.github.io/powershell/) and requires an environment ready for PnP PowerShell.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
employee-recognition-card.json | [Sudeep Ghatak](https://github.com/sudeepghatak)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|Apr 21, 2024|Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

None

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/employee-recognition-card" />
