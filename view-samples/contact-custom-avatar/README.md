# SharePoint View Formatting – Contact Custom Avatar Card

## Podsumowanie

This SharePoint view formatting sample provides a modern, interactive **Contact custom avatar card** for list items using JSON formatting. It enhances the display of user information and enables **quick actions** directly from the list. The column supports **Person or Group type fields for Email**, making it fully compatible with SharePoint user data.

![zrzut ekranu próbki](./assets/screenshot.png)

## View Requirements

This formatting works for lists with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| Email | Person or Group column | User’s email (must be of Person/Group type) |

## Key Features

### Custom Avatar
- Displays the **first letter of the user’s name** inside a circular avatar.
- **Dynamic background color**:
  - **Red (`#e81123`)** if the user has an email.
  - **Blue (`#1078D4`)** if no email is provided.
- Rounded circle with shadow and uppercase initials for visibility.

### Person/Email Integration
- Works with **Person or Group column type** to extract the user's email and display name.

### Quick Actions
- **Email icons** opens the default mail client with the user's email.
- **Teams icons** opens Microsoft Teams for direct conversation.

## Użycie Instructions
1. Navigate to your **SharePoint list**.
2. Click All items → **Add view**.
3. Select **Gallery** as the layout and give it a name of your choice.
4. Open the new view → click **Format current view**.
3. Choose **Advanced mode** and paste the JSON sample into the formatting editor.
4. Save the formatting.

Your list will now display in a **Gallery (card-style) layout** with custom avatars and action buttons.

## Wymagania
- **SharePoint Online (Modern Experience)**
- **Person or Group column type** for Email
- Modern browser for full functionality

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
contact-custom-avatar.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

| Wersja | Data | Uwagi |
|---------|------|---------|
| 1.0 | sierpnia 25, 2025 | Wersja początkowa |


## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/contact-custom-avatar" />