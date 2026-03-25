# Incident Action Buttons

## Podsumowanie

Ta próbka dodaje two context-aware buttons to a SharePoint list for managing incident workflows directly from the list view. It uses column formatting and the `executeFlow` action to provide inline **Escalate** and **Resolve** buttons that trigger Power Automate flows.

![zrzut ekranu próbki](./assets/screenshot.png)

Key points:

- The **Escalate** button is only enabled when `Priority` is set to `high`
- The **Resolve** button is disabled when the `Status` is still `new`
- Both buttons are styled using inline JSON and provide a more app-like interaction in SharePoint
- Uses `executeFlow` actions to launch Power Automate flows for escalation and resolution handling

## Wymagania widoku

|Type|Internal Name|Required|Additional Information|
|---|---|:---:|---|
|Choice|Priority|Yes|Values: `low`, `medium`, `high` (all lowercase)|
|Choice|Status|Yes|Values: `new`, `in progress`, `resolved` (all lowercase)|
|Single line of text|Actions| |Apply [generic-action-buttons.json](./generic-action-buttons.json) to this column|

- Format is best applied to a dedicated Actions column (type: Single line of text) that exists solely for button rendering.

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
generic-action-buttons.json | [Luise Freese](https://github.com/LuiseFreese)

## Historia wersji

Wersja |Data          |Uwagi
--------|--------------|--------
1.0     |July 16, 2025 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/generic-action-buttons" />
