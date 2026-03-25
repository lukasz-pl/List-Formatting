# To-do List

## Podsumowanie
This sample formats your SharePoint list view to look like Microsoft To Do.

![zrzut ekranu próbki](./assets/screenshot.png)


## Wymagania widoku

Column Name   |Type
--------------|--------------
Title         | Single Line Text
Description   | Multi Line Text
Category   | Choice
Due date   | Data and time
Important   | Yes/No, with default value set to No
Status   | Yes/No, with default value set to No
Data   | Calculated, as a single line of text using the formula: =CONCATENATE(TEXT(WEEKDAY([Due date]),"ddd"),", ",TEXT([Due date],"mmmm dd, yyyy"))



## More info and details

This sample and all the options and decisions made to implement it, is explained in detail in a serie of articles:    

1️⃣ [List Definition](https://lists.handsontek.net/create-list-using-sharepoint-microsoft-lists-view-formatting-part-1/)  
2️⃣ [List view customization](https://lists.handsontek.net/create-list-using-sharepoint-microsoft-lists-view-formatting-part-2/)  
3️⃣ [To Do list template](https://lists.handsontek.net/create-list-using-sharepoint-microsoft-lists-view-formatting-part-3/)   

A resumed version of the articles is also available in video format

🎥 [Creating a To Do list for Microsoft Lists and SharePoint using View Formatting](https://www.youtube.com/watch?v=Ic5ZdBso3iI)   


## Próbka

Rozwiązanie|Autor(zy)
--------|---------
to-do.json | [João Ferreira](https://github.com/joaoferreira)



## Historia wersji

Version |Data              |Uwagi
--------|------------------|--------------------------------
1.0     |marca 4, 2022  |Wersja początkowa


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/to-do" />
