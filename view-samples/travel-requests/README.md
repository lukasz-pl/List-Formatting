# Travel Requests

## Podsumowanie
This sample formats the SharePoint list template Travel requests.

![zrzut ekranu próbki](./assets/screenshot.png)

The approve button will set the value of the Approved column to Yes (true).

## Wymagania widoku

### SharePoint List

The following fields are all included in the "Travel requests" template. You can find this template in the new List dialog:

![image on the list template](./assets/listtemplates.png)

|Type                |Internal Name     |Wymagane|
|--------------------|------------------|:------:|
|Pojedyncza linia tekstu |Title             |Yes     |
|Person or Group     |Requester         |No      |
|Location            |Destination       |No      |
|Data i godzina       |TravelStartData   |No      |
|Data i godzina       |TravelEndData     |No      |
|Calculated          |TravelDuration    |No      |
|Choice              |Airline           |No      |
|Liczba              |EstimatedAirfare  |No      |
|Location            |Hotel             |No      |
|Liczba              |EstimatedHotelCost|No      |
|Yes/No              |Approved          |No      |

The items above are not required, but highly recommended. Furthermore, You could filter the view on the Approved column (Approved? is equal to No) to create an action list. You can then copy that view and adjust the filtering to yes and name the view approved, to only indicate approved items.

### Bing maps key

The view shows a static map image of the Destination column. You need to enter a Bing Map key to make it work. You can create an account at the [Bing maps Dev Center](https://www.bingmapsportal.com/). Once registered, you can create a key. Copy that key and put it in the json file where indicated.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
travel-requests.json | [Miguel Verweij](https://github.com/miguelverweij)

## Historia wersji

Version |Data              |Uwagi
--------|------------------|--------
1.0     |sierpnia 20, 2022   |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/travel-requests" />