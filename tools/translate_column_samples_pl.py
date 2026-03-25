#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/Users/lukasz_preihs/Documents/GitHub/List-Formatting/próbki kolumn")

README_REPLACEMENTS = {
    "## Version History": "## Historia wersji",
    "## Additional Notes": "## Dodatkowe uwagi",
    "## How It Works": "## Jak to działa",
    "## How to Apply": "## Jak zastosować",
    "## References": "## Odnośniki",
    "## Troubleshooting": "## Rozwiązywanie problemów",
    "## Features": "## Funkcje",
    "### Column Types": "### Typy kolumn",
    "**Solution**:": "**Rozwiązanie**:",
    "Field |Type": "Pole |Typ",
    "Title | Single line of text": "Title | Pojedyncza linia tekstu",
    "Create a SharePoint list with the following columns:": "Utwórz listę SharePoint z następującymi kolumnami:",
    "To obtain a Flow's ID:": "Aby uzyskać identyfikator przepływu:",
    "1. Click _Flow_ > _See your flows_ in the SharePoint list where the Flow is configured": "1. Kliknij _Flow_ > _See your flows_ na liście SharePoint, na której skonfigurowano przepływ",
    "2. Click on the Flow you want to run": "2. Kliknij przepływ, który chcesz uruchomić",
    "3. Copy the ID from the end of the URL": "3. Skopiuj identyfikator z końca adresu URL",
    "> Alternatively, this information is available in the Power Automate environment where your flow lives and can be found in flow details": "> Alternatywnie tę informację znajdziesz w środowisku Power Automate, w szczegółach przepływu",
    "> Tip - You can apply this format to a Calculated Column with a formula of `=\"\"`. This prevents this field from being part of your edit/new forms.": "> Wskazówka: możesz zastosować ten format do kolumny obliczeniowej z formułą `=\"\"`. Dzięki temu pole nie będzie częścią formularzy nowego elementu ani edycji.",
    "> Actions are supported in lists and libraries in SharePoint and Microsoft Lists": "> Akcje są obsługiwane na listach i w bibliotekach w SharePoint oraz Microsoft Lists",
    "> Some actions, however, are only supported in document libraries": "> Niektóre akcje są jednak obsługiwane tylko w bibliotekach dokumentów",
    "These samples are all built for column formatting, but these can be easily adapted to work with view formatting.": "Wszystkie te przykłady zostały przygotowane dla formatowania kolumn, ale można je łatwo dostosować do formatowania widoków.",
    "Custom row actions only work when placed inside of `button`, `div`, or `span` elements. However, you can adjust the element's styles/children to customize the look entirely _(you can even wrap your entire format in a button - see the [bulletin-board-format](../../view-samples/bulletin-board-format) for an example)_.": "Niestandardowe akcje wiersza działają tylko wtedy, gdy są umieszczone wewnątrz elementów `button`, `div` lub `span`. Możesz jednak dowolnie zmieniać style i elementy podrzędne, aby całkowicie dostosować wygląd _(możesz nawet opakować cały format w przycisk - przykład znajdziesz w [bulletin-board-format](../../view-samples/bulletin-board-format))_.",
    "This action will open the list item. This is equivalent to double-clicking an item.": "Ta akcja otwiera element listy. To odpowiednik dwukrotnego kliknięcia elementu.",
    "This action will open the list item in edit mode. This is equivalent to double-clicking an item and then pressing `Edit all`.": "Ta akcja otwiera element listy w trybie edycji. To odpowiednik dwukrotnego kliknięcia elementu i wybrania `Edit all`.",
    "This action will launch the Share dialog for an item. This is equivalent to selecting the item and then pressing the `Share` command bar button.": "Ta akcja otwiera okno dialogowe udostępniania dla elementu. To odpowiednik zaznaczenia elementu i kliknięcia przycisku `Share` na pasku poleceń.",
    "This action will launch the Copy Link dialog for an item and copy the link to the clipboard. This is equivalent to selecting the item and then pressing the `Copy link` command bar button.": "Ta akcja otwiera okno dialogowe kopiowania linku dla elementu i kopiuje link do schowka. To odpowiednik zaznaczenia elementu i kliknięcia przycisku `Copy link` na pasku poleceń.",
    "This action will open the list item and place the focus in the comment input box. This is equivalent to double-clicking an item and then clicking in the comment box.": "Ta akcja otwiera element listy i ustawia fokus w polu komentarza. To odpowiednik dwukrotnego kliknięcia elementu, a następnie kliknięcia w pole komentarza.",
    "This action will prompt the user with a Deletion confirmation dialog and delete the item if they choose yes. This is equivalent to selecting the item and then pressing the `Delete` command bar button.": "Ta akcja wyświetla użytkownikowi okno potwierdzenia usunięcia i usuwa element po wybraniu opcji potwierdzającej. To odpowiednik zaznaczenia elementu i kliknięcia przycisku `Delete` na pasku poleceń.",
    "This action will launch a Power Automate flow for the item as the selected item. This action requires additional configuration through the `actionParams` property. The ID is always required, but you can also optionally include `headerText` and/or `runFlowButtonText` properties as well to customize the Flow panel.": "Ta akcja uruchamia przepływ Power Automate dla wybranego elementu. Wymaga dodatkowej konfiguracji poprzez właściwość `actionParams`. Identyfikator jest zawsze wymagany, ale opcjonalnie możesz także podać właściwości `headerText` i/lub `runFlowButtonText`, aby dostosować panel przepływu.",
    ">Note - the `headerText` and `runFlowButtonText` parameters are not available in SharePoint 2019": ">Uwaga: parametry `headerText` i `runFlowButtonText` nie są dostępne w SharePoint 2019",
    "`actionParams` are JSON values but because they are inside a JSON format, they have to be entered as a JSON string value. In order to do that, you have to escape all the double quotes. So the JSON for `actionParams` may look like this:": "`actionParams` to wartości JSON, ale ponieważ znajdują się wewnątrz formatu JSON, muszą zostać zapisane jako tekstowy ciąg JSON. Aby to zrobić, trzeba poprzedzić wszystkie podwójne cudzysłowy znakami ucieczki. JSON dla `actionParams` może więc wyglądać tak:",
    "It has to be put into a single string value for the `actionParams` property so we put a backslash (`\\`) in front of each double quote (`\"`) and put it all on one line:": "Trzeba to umieścić w jednej wartości tekstowej właściwości `actionParams`, więc przed każdym podwójnym cudzysłowem (`\"`) dodajemy ukośnik odwrotny (`\\`) i zapisujemy wszystko w jednym wierszu:",
    "This value can even be written using expressions but you'll need to remember to build it with all the escapes as well.": "Tę wartość można zapisać także za pomocą wyrażeń, ale trzeba pamiętać o dodaniu wszystkich znaków ucieczki.",
    "This action will open the Approval Dialog for the item (at whatever stage of approval it is in). This requires Content Approval to be enabled for the list/library. This is equivalent to selecting an item and pressing the `Request Approval` command bar button.": "Ta akcja otwiera okno zatwierdzania dla elementu, niezależnie od etapu akceptacji. Wymaga włączenia zatwierdzania zawartości dla listy lub biblioteki. To odpowiednik zaznaczenia elementu i kliknięcia przycisku `Request Approval` na pasku poleceń.",
    "This action will open the context menu for an item. This is equivalent to right-clicking (or <kbd>CTRL</kbd>-clicking on Mac) and item.": "Ta akcja otwiera menu kontekstowe elementu. To odpowiednik kliknięcia prawym przyciskiem myszy (lub kliknięcia z klawiszem <kbd>CTRL</kbd> na Macu) na elemencie.",
    "This action will open a callout with content embedded in it. You must specify the `src` value as part of `actionInput` to determine what content is loaded.": "Ta akcja otwiera dymek z osadzoną zawartością. Aby określić, jaka treść ma zostać załadowana, musisz podać wartość `src` jako część `actionInput`.",
    "There are 3 properties that can be set within `actionInput` with `src` being required.": "W `actionInput` można ustawić 3 właściwości, z czego `src` jest wymagane.",
    "- `src`: This is the embeddable URL of the content to load in the callout (via iframe)": "- `src`: adres URL treści, którą można osadzić i załadować w dymku (przez iframe)",
    "- `width`: This is an optional property that determines the width of the callout in pixels. Enter the value as a plain number.": "- `width`: opcjonalna właściwość określająca szerokość dymku w pikselach. Wpisz wartość jako zwykłą liczbę.",
    "- `height`: This is an optional property that determines the height of the callout in pixels. Enter the value as a plain number.": "- `height`: opcjonalna właściwość określająca wysokość dymku w pikselach. Wpisz wartość jako zwykłą liczbę.",
    "#### Getting an embed URL": "#### Jak uzyskać adres URL do osadzenia",
    "The `src` property is the URL of the embeddable content. You can generally find it as the `src` attribute of a generated `iframe` element on a site that provides `embed` options.": "Właściwość `src` to adres URL treści możliwej do osadzenia. Zwykle znajdziesz go jako atrybut `src` wygenerowanego elementu `iframe` w serwisie, który oferuje opcję `embed`.",
    "> Note - SharePoint restricts the domains that can be used for this. This can be adjusted on individual site collections or for the whole tenant. [Allow or restrict the ability to embed content on SharePoint Lists using custom formatters](https://go.microsoft.com/fwlink/p/?linkid=2258033)": "> Uwaga: SharePoint ogranicza domeny, których można do tego używać. Można to dostosować dla poszczególnych kolekcji witryn lub dla całej dzierżawy. [Zezwalanie na osadzanie treści w SharePoint Lists przy użyciu niestandardowych formaterów lub ograniczanie tej możliwości](https://go.microsoft.com/fwlink/p/?linkid=2258033)",
    "For example, you can get an embed URL for a public YouTube video by clicking on **Share** then selecting **Embed** and copying the `src` value and the `width` and `height` values from the generated markup:": "Na przykład możesz uzyskać adres URL do osadzenia publicznego filmu z YouTube, klikając **Share**, następnie wybierając **Embed** i kopiując wartość `src` oraz wartości `width` i `height` z wygenerowanego kodu:",
    "This action allows you to update the values of one or more fields for a given item. You specify the fields and their updated values using `actionInput`.": "Ta akcja pozwala zaktualizować wartości jednego lub wielu pól dla danego elementu. Pola i ich nowe wartości określasz za pomocą `actionInput`.",
    "This action will open the default preview handler for the file directly in the library interface.": "Ta akcja otwiera domyślny podgląd pliku bezpośrednio w interfejsie biblioteki.",
    "This action will send a copy of a file to another library. You specify the destination library and/or sub folder within that library using `actionParams`. This is equivalent to selecting a file and clicking the `Copy to` command bar button with the added benefit of already specifying the destination.": "Ta akcja wysyła kopię pliku do innej biblioteki. Bibliotekę docelową i/lub podfolder określasz za pomocą `actionParams`. To odpowiednik zaznaczenia pliku i kliknięcia przycisku `Copy to` na pasku poleceń, z dodatkową korzyścią w postaci wcześniejszego wskazania miejsca docelowego.",
    "Just like with `executeFlow` the `actionParams` are escaped JSON but there's currently only one property that needs to be specified: `destinationUrl`. This is a full URL (using `@currentWeb` to avoid hard coding your tenant) directly to the library and/or the folder within that library you want the file copied to.": "Podobnie jak w `executeFlow`, `actionParams` to JSON ze znakami ucieczki, ale obecnie trzeba podać tylko jedną właściwość: `destinationUrl`. Jest to pełny adres URL (z użyciem `@currentWeb`, aby uniknąć wpisywania na stałe adresu dzierżawy) prowadzący bezpośrednio do biblioteki i/lub folderu, do którego chcesz skopiować plik.",
    "User's permissions on the destination library/folder are not verified ahead of time and users without permission will receive an error.": "Uprawnienia użytkownika do biblioteki lub folderu docelowego nie są sprawdzane z wyprzedzeniem, więc użytkownicy bez odpowiednich uprawnień otrzymają błąd.",
    "This action will move a file to another library (removing it from the source library). You specify the destination library and/or sub folder within that library using `actionParams`. This is equivalent to selecting a file and clicking the `Move to` command bar button with the added benefit of already specifying the destination.": "Ta akcja przenosi plik do innej biblioteki, usuwając go z biblioteki źródłowej. Bibliotekę docelową i/lub podfolder określasz za pomocą `actionParams`. To odpowiednik zaznaczenia pliku i kliknięcia przycisku `Move to` na pasku poleceń, z dodatkową korzyścią w postaci wcześniejszego wskazania miejsca docelowego.",
    "Just like with `executeFlow` the `actionParams` are escaped JSON but there's currently only one property that needs to be specified: `destinationUrl`. This is a full URL (using `@currentWeb` to avoid hard coding your tenant) directly to the library and/or the folder within that library you want the file moved to.": "Podobnie jak w `executeFlow`, `actionParams` to JSON ze znakami ucieczki, ale obecnie trzeba podać tylko jedną właściwość: `destinationUrl`. Jest to pełny adres URL (z użyciem `@currentWeb`, aby uniknąć wpisywania na stałe adresu dzierżawy) prowadzący bezpośrednio do biblioteki i/lub folderu, do którego chcesz przenieść plik.",
    "- These formats can be applied to any column type (its value is ignored)": "- Te formaty można zastosować do dowolnego typu kolumny, ponieważ jej wartość jest ignorowana",
    "- If using the `executeFlow` action, the list/library is expected to have an associated Flow, the ID of this flow needs to be included in the `actionParams` for the button": "- Jeśli używasz akcji `executeFlow`, lista lub biblioteka musi mieć powiązany przepływ, a jego identyfikator należy umieścić w `actionParams` przycisku",
    "- The `setValue.json` sample expects a number column named `Value`": "- Przykład `setValue.json` zakłada istnienie kolumny liczbowej o nazwie `Value`",
    "- The `previewFileAction.json`, `copyFile.json`, and `moveFile.json` formats can only be used within document libraries": "- Formaty `previewFileAction.json`, `copyFile.json` i `moveFile.json` mogą być używane wyłącznie w bibliotekach dokumentów",
    "> Tip - You can apply these formats to a Calculated Column with a formula of `=\"\"`. This makes it obvious the fields aren't expected to hold values and you can configure the columns of your form to hide them easily.": "> Wskazówka: możesz zastosować te formaty do kolumny obliczeniowej z formułą `=\"\"`. Dzięki temu od razu widać, że pola nie mają przechowywać wartości, a kolumny można łatwo ukryć w formularzu.",
    "- Additional samples of the `executeFlow` action can be found here:": "- Dodatkowe przykłady akcji `executeFlow` znajdziesz tutaj:",
    "A similar wizard is also included in the [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md) webpart that allows full customization.": "Podobny kreator znajduje się także w webparcie [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md), który pozwala na pełne dostosowanie.",
    "This template is included in the [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md) webpart.": "Ten szablon jest dołączony do webpartu [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md).",
    "A similar template is also included in the [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md) webpart.": "Podobny szablon znajduje się także w webparcie [Column Formatter](https://github.com/SharePoint/sp-dev-solutions/blob/master/solutions/ColumnFormatter/README.md).",
    "- This format uses operators only available in SharePoint Online and cannot be used in SharePoint 2019": "- Ten format używa operatorów dostępnych wyłącznie w SharePoint Online i nie może być używany w SharePoint 2019",
    "> Additional versions using Abstract Tree Syntax (AST) are also provided for environments where the Excel-style expressions are not supported.": "> Dodatkowe wersje wykorzystujące Abstract Tree Syntax (AST) są również dostępne dla środowisk, w których wyrażenia w stylu Excela nie są obsługiwane.",
    "> An additional version using Abstract Tree Syntax (AST) is also provided for environments where the Excel-style expressions are not supported.": "> Dodatkowa wersja wykorzystująca Abstract Tree Syntax (AST) jest również dostępna dla środowisk, w których wyrażenia w stylu Excela nie są obsługiwane.",
    "> An additional version using Abstract Tree Syntax (AST) is also provided for environments where the Excel-style expressions are not supported (SP2019).": "> Dodatkowa wersja wykorzystująca Abstract Tree Syntax (AST) jest również dostępna dla środowisk, w których wyrażenia w stylu Excela nie są obsługiwane (SP2019).",
    "Some example values and the result using the function above:": "Kilka przykładowych wartości i wynik działania powyższej funkcji:",
    "Notice that the `indexOf` function is **case-sensitive**. You can do a case-insensitive check by adding the `toLowerCase` function like this:": "Zwróć uwagę, że funkcja `indexOf` **rozróżnia wielkość liter**. Aby wykonać sprawdzenie bez rozróżniania wielkości liter, możesz dodać funkcję `toLowerCase` w taki sposób:",
    "None": "Brak",
    "- None": "- Brak",
    "![Screenshot of the sample](./assets/screenshot.png)": "![Zrzut ekranu próbki](./assets/screenshot.png)",
    "![screenshot of the sample - document library](./assets/screenshot2.png)": "![zrzut ekranu próbki - biblioteka dokumentów](./assets/screenshot2.png)",
    "![screenshot of defaultClick](./assets/defaultClick.png)": "![zrzut ekranu defaultClick](./assets/defaultClick.png)",
    "![screenshot of editProps](./assets/editProps.png)": "![zrzut ekranu editProps](./assets/editProps.png)",
    "![screenshot of share](./assets/share.png)": "![zrzut ekranu share](./assets/share.png)",
    "![screenshot of copyLink](./assets/copyLink.png)": "![zrzut ekranu copyLink](./assets/copyLink.png)",
    "![screenshot of comment](./assets/comment.png)": "![zrzut ekranu comment](./assets/comment.png)",
    "![screenshot of delete](./assets/delete.png)": "![zrzut ekranu delete](./assets/delete.png)",
    "![screenshot of executeFlow](./assets/executeFlow.png)": "![zrzut ekranu executeFlow](./assets/executeFlow.png)",
    "![screenshot of openApprovalDialog](./assets/openApprovalDialog.png)": "![zrzut ekranu openApprovalDialog](./assets/openApprovalDialog.png)",
    "![screenshot of openContextMenu](./assets/openContextMenu.png)": "![zrzut ekranu openContextMenu](./assets/openContextMenu.png)",
    "![screenshot of embed](./assets/embed.png)": "![zrzut ekranu embed](./assets/embed.png)",
    "![screenshot of setValue](./assets/setValue.png)": "![zrzut ekranu setValue](./assets/setValue.png)",
    "![screenshot of previewFileAction](./assets/previewFileAction.png)": "![zrzut ekranu previewFileAction](./assets/previewFileAction.png)",
    "![screenshot of copyFile](./assets/copyFile.png)": "![zrzut ekranu copyFile](./assets/copyFile.png)",
    "![screenshot of moveFile](./assets/moveFile.png)": "![zrzut ekranu moveFile](./assets/moveFile.png)",
    "![embedding from YouTube](./assets/youtubeEmbed.png)": "![osadzanie z YouTube](./assets/youtubeEmbed.png)",
    "If you click on an image in a SharePoint list, the image is displayed as a preview. This formatter changes the standard behavior in which a link from another column is used. In this way, a click on the image has the same behavior as if the link had been clicked directly.": "Jeśli klikniesz obraz na liście SharePoint, zostanie on wyświetlony jako podgląd. Ten formatter zmienia standardowe zachowanie tak, aby używany był link z innej kolumny. Dzięki temu kliknięcie obrazu działa tak samo, jak bezpośrednie kliknięcie linku.",
    "- A column of type image containing this column formatter": "- Kolumna typu obraz zawierająca ten formatter kolumny",
    "- A hyperlink column (Internal Name: Link) that contains the target link.": "- Kolumna hiperłącza (nazwa wewnętrzna: `Link`) zawierająca link docelowy.",
    "1.1|November 21, 2024|Using columns link description instead of title": "1.1|21 listopada 2024|Użycie opisu linku kolumny zamiast tytułu",
    "1.1|21 listopada 2024|Using columns link description instead of title": "1.1|21 listopada 2024|Użycie opisu linku kolumny zamiast tytułu",
    "- Change the Image size on line 21": "- Zmień rozmiar obrazu w linii 21",
    "- To remove rounded corners, remove the image style on line 24-26": "- Aby usunąć zaokrąglone rogi, usuń styl obrazu w liniach 24-26",
    "- Padding between the rows can be tweaked on line 6 & 7": "- Odstępy między wierszami można dostosować w liniach 6 i 7",
    "- Choose how the link opens in the browser on line 14. \"_blank\" for new window/tab, or \"_self\" for the same window.": "- W linii 14 wybierz sposób otwierania linku w przeglądarce: `\"_blank\"` dla nowego okna lub karty albo `\"_self\"` dla tego samego okna.",
    "Możesz również specify width and height of the callout using optional properties.": "Możesz również określić szerokość i wysokość dymku za pomocą opcjonalnych właściwości.",
    "- Format expect the following fields:": "- Format oczekuje następujących pól:",
    "*Note: Additional columns can be added as needed for your specific use case.*": "*Uwaga: dodatkowe kolumny można dodać w zależności od potrzeb konkretnego przypadku użycia.*",
    "- Charts are generated dynamically using the [QuickChart.io API](https://quickchart.io/)": "- Wykresy są generowane dynamicznie przy użyciu [QuickChart.io API](https://quickchart.io/)",
    "- The layout displays charts at 400x250 pixels with rounded corners": "- Układ wyświetla wykresy w rozmiarze 400x250 pikseli z zaokrąglonymi rogami",
    "- The chart automatically updates when column values change": "- Wykres aktualizuje się automatycznie po zmianie wartości w kolumnach",
    "**CRITICAL**: Before the charts will display, you must configure SharePoint security settings:": "**KRYTYCZNE**: zanim wykresy zaczną się wyświetlać, musisz skonfigurować ustawienia zabezpieczeń SharePoint:",
    "4. Add `quickchart.io` to the **allowed domains** list": "4. Dodaj `quickchart.io` do listy **dozwolonych domen**",
    "- Requires internet connectivity for chart generation": "- Wymaga połączenia z internetem do generowania wykresów",
    "- Performance may vary with large lists due to multiple API calls": "- Wydajność może się różnić przy dużych listach ze względu na wiele wywołań API",
    "The `indexOf` function returns the index where a given value is found within a string (indexes start at 0). If the value is not found in the text, the result is -1.": "Funkcja `indexOf` zwraca indeks, pod którym dana wartość została znaleziona w ciągu znaków (indeksy zaczynają się od 0). Jeśli wartość nie zostanie znaleziona w tekście, wynikiem jest -1.",
    "`@currentField`|result": "`@currentField`|wynik",
    "A dog | Yes": "A dog | Tak",
    "### User Profile Picture sizes": "### Rozmiary obrazów profilowych użytkownika",
    "> Note: `@currentField.picture` can be used to retrieve a profile picture directly from a person column. However, size options are not available using that approach.": "> Uwaga: `@currentField.picture` może zostać użyte do pobrania zdjęcia profilowego bezpośrednio z kolumny osoby. W tym podejściu opcje rozmiaru nie są jednak dostępne.",
    "2.0|31 lipca 2025|Additional actions": "2.0|31 lipca 2025|Dodatkowe akcje",
    "1.1|20 sierpnia 2018|Switched to Excel-style expressions": "1.1|20 sierpnia 2018|Przełączono na wyrażenia w stylu Excela",
    "1.1|20 sierpnia 2018|Updated to use Excel-style expressions": "1.1|20 sierpnia 2018|Zaktualizowano do użycia wyrażeń w stylu Excela",
    "1.2|20 sierpnia 2018|Switched to Excel-style expression": "1.2|20 sierpnia 2018|Przełączono na wyrażenie w stylu Excela",
    "1.1|22 marca 2018|Simplified logic": "1.1|22 marca 2018|Uproszczono logikę",
}

JSON_LITERAL_REPLACEMENTS = {
    "Register": "Zarejestruj",
    "Unregister": "Wyrejestruj",
    "Registered": "Zarejestrowano",
    "Course is full": "Brak miejsc na kursie",
    "Registration has ended": "Rejestracja została zakończona",
    "Open in App": "Otwórz w aplikacji",
    "Details": "Szczegóły",
    "Approval Details": "Szczegóły zatwierdzenia",
    "Approval Status details": "Szczegóły statusu zatwierdzenia",
    "Do": "Zrób",
    "Decide": "Zdecyduj",
    "Delegate": "Deleguj",
    "Delete": "Usuń",
    "Open": "Otwórz",
    "Edit": "Edytuj",
    "Download": "Pobierz",
    "Send Email": "Wyślij e-mail",
    "Chat in Teams": "Czat w Teams",
    "Select image": "Wybierz obraz",
    "Delete image": "Usuń obraz",
    "Approve": "Zatwierdź",
    "Reject": "Odrzuć",
    "Request": "Wniosek",
    "Request approval": "Poproś o zatwierdzenie",
    "Assign to Me": "Przypisz do mnie",
    "+ Assign to Me": "+ Przypisz do mnie",
    "Open context menu": "Otwórz menu kontekstowe",
    "Comment": "Komentarz",
    "Share Item": "Udostępnij element",
    "Share to Teams": "Udostępnij w Teams",
    "Share to teams": "Udostępnij w Teams",
    "Close window": "Zamknij okno",
    "Click to expand": "Kliknij, aby rozwinąć",
    "Click to Show Actions": "Kliknij, aby pokazać akcje",
    "Click to open callout with embedded content.": "Kliknij, aby otworzyć dymek z osadzoną zawartością.",
    "Open Item": "Otwórz element",
    "Edit Item": "Edytuj element",
    "Delete Item": "Usuń element",
    "Preview file": "Podgląd pliku",
    "Copy link": "Kopiuj link",
    "Open in New Window": "Otwórz w nowym oknie",
    "Now": "Teraz",
    "Off": "Wył.",
    "On": "Wł.",
    "YES": "TAK",
    "NO": "NIE",
    "Favorite": "Ulubione",
    "Remove Favorite": "Usuń z ulubionych",
    "Ask a Question": "Zadaj pytanie",
    "Escalate": "Eskaluj",
    "Resolve": "Rozwiąż",
    "Increase value": "Zwiększ wartość",
    "Decrease value": "Zmniejsz wartość",
    "Delivered": "Dostarczono",
    "In transit": "W transporcie",
    "Packed": "Spakowano",
    "Ready to be packed": "Gotowe do spakowania",
    "Shipped": "Wysłano",
    "Flow Status": "Status przepływu",
    "Flow Name": "Nazwa przepływu",
    "Flow run details": "Szczegóły uruchomienia przepływu",
    "Requires flow ownership rights to access": "Wymaga uprawnień właściciela przepływu",
    "Version history": "Historia wersji",
    "Step 1": "Krok 1",
    "Step 2": "Krok 2",
    "Step 3": "Krok 3",
    "Step 4": "Krok 4",
    "Step 5": "Krok 5",
    "World Time": "Czas na świecie",
    "Conditional Text Formatting (Severity)": "Warunkowe formatowanie tekstu (ważność)",
    "Launch Power App Button": "Przycisk uruchamiania Power App",
    "Multi-Person Mail To Link": "Link MailTo dla wielu osób",
    "Number Battery": "Bateria liczbowa",
    "Course Registration": "Rejestracja na kurs",
    "Progress bar using text or emoji": "Pasek postępu z użyciem tekstu lub emoji",
    "Linking to a Local Resource": "Link do zasobu lokalnego",
    "Display icons by repeating": "Wyświetlanie ikon przez powtarzanie",
    "Volume option": "Opcja głośności",
    "Date Update Format": "Format aktualizacji daty",
    "Reference a Local Image": "Odwołanie do lokalnego obrazu",
    "Decimal to Binary Conversion": "Konwersja z dziesiętnego na binarny",
    "Multi person favorite": "Ulubione dla wielu osób",
    "Display Count Up and Count Down Buttons": "Wyświetlanie przycisków zliczania w górę i w dół",
    "Rounded Fill Checkbox": "Zaokrąglone pole wyboru z wypełnieniem",
    "Teams Message Format": "Format wiadomości Teams",
    "Changing Image Hyperlink Standard Behavior": "Zmiana standardowego zachowania hiperłącza obrazu",
    "Identicon Column Formatting": "Formatowanie kolumny identikony",
    "Launch a Flow for a Selected Item": "Uruchamianie przepływu dla wybranego elementu",
    "Row Actions": "Akcje wiersza",
    "Person Localization": "Lokalizacja osoby",
}

MONTHS = {
    "January": "stycznia",
    "February": "lutego",
    "March": "marca",
    "April": "kwietnia",
    "May": "maja",
    "June": "czerwca",
    "July": "lipca",
    "August": "sierpnia",
    "September": "września",
    "October": "października",
    "November": "listopada",
    "December": "grudnia",
}


def translate_date_line(text: str) -> str:
    for en, pl in MONTHS.items():
        text = re.sub(rf"\b{en}\b", pl, text)
    return text


def translate_markdown(text: str) -> str:
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    for idx, part in enumerate(parts):
        if part.startswith("```"):
            continue
        for src, dst in README_REPLACEMENTS.items():
            part = part.replace(src, dst)
        part = re.sub(r"!\[screenshot of the sample\]", "![zrzut ekranu próbki]", part)
        part = re.sub(r"!\[screenshot of the sample - ([^\]]+)\]", r"![zrzut ekranu próbki - \1]", part)
        part = re.sub(r"!\[screenshot of ([^\]]+)\]", r"![zrzut ekranu \1]", part)
        part = re.sub(r"!\[Screenshot of ([^\]]+)\]", r"![Zrzut ekranu \1]", part)
        part = re.sub(r"\bSingle line of text\b", "Pojedyncza linia tekstu", part)
        part = re.sub(r"\bNumber\b", "Liczba", part)
        part = re.sub(r"\bRequired\b", "Wymagane", part)
        part = re.sub(r"\bAdditional Information\b", "Dodatkowe informacje", part)
        part = re.sub(r"\bDate\b", "Data", part)
        part = re.sub(r"\bComments\b", "Uwagi", part)
        part = translate_date_line(part)
        for src, dst in JSON_LITERAL_REPLACEMENTS.items():
            part = re.sub(rf"(?m)^(#+)\s+{re.escape(src)}\s*$", rf"\1 {dst}", part)
        part = re.sub(
            r"(?P<prefix>\|?\s*\d+\.\d+\|)(?P<month>[a-ząćęłńóśźż]+) (?P<day>\d{1,2}), (?P<year>\d{4})(?P<suffix>\|)",
            lambda m: f"{m.group('prefix')}{m.group('day')} {m.group('month')} {m.group('year')}{m.group('suffix')}",
            part,
        )
        part = part.replace("## Zróbdatkowe uwagi", "## Dodatkowe uwagi")
        parts[idx] = part
    return "".join(parts)


def should_translate_json_value(key: str, value: str) -> bool:
    if not isinstance(value, str):
        return False
    if value.startswith("@") or value.startswith("="):
        return False
    if "http://" in value or "https://" in value:
        return False
    if key not in {"txtContent", "title", "description", "aria-label", "altText", "text"}:
        return False
    return True


def translate_json_obj(obj):
    if isinstance(obj, dict):
        return {k: translate_json_obj(v) if not should_translate_json_value(k, v) else JSON_LITERAL_REPLACEMENTS.get(v, v.replace(
            "Możesz użyć formatowania kolumn, aby customize how fields in SharePoint lists and libraries are displayed. To do this, you construct a JSON object that describes the elements that are displayed when a field is included in a list view, and the styles to be applied to those elements. The column formatting does not change the data in the list item or file; it only changes how its displayed to users who browse the list.",
            "Możesz użyć formatowania kolumn, aby dostosować sposób wyświetlania pól na listach i w bibliotekach SharePoint. W tym celu tworzysz obiekt JSON opisujący elementy wyświetlane wtedy, gdy pole jest uwzględnione w widoku listy, oraz style stosowane do tych elementów. Formatowanie kolumn nie zmienia danych elementu listy ani pliku; zmienia jedynie sposób ich wyświetlania użytkownikom przeglądającym listę."
        ).replace(
            "Możesz użyć formatowania kolumn, aby customize how items in SharePoint lists and libraries are displayed. To do this, you construct a JSON object that describes the elements that are displayed when an item is loaded in a column and any styles to be applied to those elements.",
            "Możesz użyć formatowania kolumn, aby dostosować sposób wyświetlania elementów na listach i w bibliotekach SharePoint. W tym celu tworzysz obiekt JSON opisujący elementy wyświetlane wtedy, gdy element jest ładowany w kolumnie, oraz style stosowane do tych elementów."
        ).replace(
            "Możesz użyć formatowania kolumn, aby customize how fields in SharePoint lists and libraries are displayed. To do this, you construct a JSON object that describes the elements that are displayed when a field is included in a list view, and the styles to be applied to those elements.",
            "Możesz użyć formatowania kolumn, aby dostosować sposób wyświetlania pól na listach i w bibliotekach SharePoint. W tym celu tworzysz obiekt JSON opisujący elementy wyświetlane wtedy, gdy pole jest uwzględnione w widoku listy, oraz style stosowane do tych elementów."
        )) for k, v in obj.items()}
    if isinstance(obj, list):
        return [translate_json_obj(x) for x in obj]
    return obj


def main() -> None:
    for path in ROOT.rglob("README.md"):
        original = path.read_text(encoding="utf-8")
        translated = translate_markdown(original)
        if translated != original:
            path.write_text(translated, encoding="utf-8")

    for path in ROOT.rglob("*.json"):
        try:
            original_text = path.read_text(encoding="utf-8")
            data = json.loads(original_text)
        except Exception:
            continue
        translated = translate_json_obj(data)
        new_text = json.dumps(translated, ensure_ascii=False, indent=2) + "\n"
        if new_text != original_text:
            path.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
