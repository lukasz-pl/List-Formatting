# Menu Style List

## Podsumowanie  
This sample transforms SharePoint list items into a styled menu layout using list view formatting. Each row is automatically formatted to visually separate the item name and price, mimicking a clean, restaurant-style pricing table - perfect for food menus, service lists, or product offerings.

![zrzut ekranu próbki](./assets/screenshot.png)  

![zrzut ekranu the sample displayed on the page](./assets/FormattedMenuList_Page.png)

**Note:** To customise group icons (e.g. for `MainCategory`), edit the `iconName` attribute in the JSON (around line 42).  

```json
"attributes": {
  "iconName": "=if(@group.fieldData.displayValue == 'Appetizers', 'EatDrink', if(@group.fieldData.displayValue == 'Drinks', 'CoffeeScript', if(@group.fieldData.displayValue == 'Desserts', 'Cake', if(@group.fieldData.displayValue == 'Main Courses', 'Chopsticks', ''))))"
}
```

## Wymagania widoku
|Type               |Internal Name|Wymagane|
|-------------------|-------------|:------:|
|Pojedyncza linia tekstu|Title        |Yes     |
|Liczba             |Price       |Yes     |
|Choice |MainCategory   |Yes        |

- Make sure to use the List View and include all the specified fields in the view.
- To customize the menu order, add a sorting column (e.g., `OrderLiczba`) and use it as the sort field in the view.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
menu-style-list.json | [Tanel Vahk](https://github.com/tvahk)

## Historia wersji

Version |Data             |Uwagi
--------|-----------------|--------------------------------
1.0     |czerwca 3, 2025 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/menu-style-list" />