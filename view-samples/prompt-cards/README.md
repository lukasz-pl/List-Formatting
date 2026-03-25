# Prompt Cards

## Podsumowanie
This sample demonstrates how to format list items as prompt cards. The design is inspired from the [Copilot Lab](https://copilot.cloud.microsoft/prompts/all) prompt library. It features the following:
- **Responsive tile layout:** Items are displayed in a card-based layout that adjusts to different screen sizes.
- **Conditional Icons:** Icons change dynamically based on the value of the **PromptCategory** column.
- **Theme Color Classes:** Uses theme color classes to ensure the format displays as intended regardless of the site's theme (light, dark, custom, etc.).
- **Gallery View:** The formatting is designed to work with the Gallery view style.

![zrzut ekranu próbki](./assets/screenshot.png)


## Wymagania widoku

**Important:** This formatting depends on the Gallery view style. Make sure to set your view to Gallery before applying the formatting.

|Typ|Nazwa wewnętrzna|Wymagane|
|---|---|:---:|
|Pojedyncza linia tekstu|Title|Tak|
|Wiele linii tekstu|Prompt|Tak|
|Choice|PromptCategory|Tak|
|Choice (allow multiple)|Worksin|Tak|
|Calculated (Pojedyncza linia tekstu)|Icon|Tak|

### Column Details

- **Title (Pojedyncza linia tekstu):** A concise name for the prompt.
- **Prompt (Wiele linii tekstu):** The full text of the prompt.
- **PromptCategory (Choice):** Categorize prompts for easy filtering. Choices include:
  - Understand
  - Create
  - Catch up
  - Ask
  - Edit
  - Learn
  - Design
  - Code
  - Analyze
  - Manage
- **Worksin (Choice - allow multiple selections):** Specify applications or contexts where the prompt is effective. Choices include:
  - Business Chat (work)
  - Copilot chat (web)
  - ChatGPT
  - GitHub Copilot
  - Teams
  - Outlook
  - Word
  - Excel
  - PowerPoint
  - OneNote
  - Loop
  - Whiteboard
  - SharePoint
  - OneDrive
  - Planner
  - Stream
  - Forms
  - Viva Engage
- **Icon (Calculated - Pojedyncza linia tekstu):** This column calculates the appropriate icon based on the **PromptCategory**.
  You need the **Icon** calculated column to display the icon associated with the **PromptCategory** column. Use the following formula for this calculated column:

  `
  =IF(ISBLANK([PromptCategory]),"PageEdit",IF([PromptCategory]="Understand","Lightbulb",IF([PromptCategory]="Create","TextDocumentEdit",IF([PromptCategory]="Catch up","PageList",IF([PromptCategory]="Ask","Feedback",IF([PromptCategory]="Edit","Edit",IF([PromptCategory]="Learn","LearningTools",IF([PromptCategory]="Design","EditCreate",IF([PromptCategory]="Code","CodeEdit",IF([PromptCategory]="Analyze","ComplianceAudit",IF([PromptCategory]="Manage","DataTime","PageEdit")))))))))))
  `

> [!NOTE]
> The separator character in the Calculated column is either `,` (comma) or `;` (semicolon), depending on your locale. If your locale uses `;` as a separator, replace `,` with `;` in the formula provided above.

If you'd like to require approval before the prompt is shown in the prompt library list, you can use Microsoft Power Automate to request approval when a SharePoint item is created and use the "Stop sharing an item or a file" action until the item is approved.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
prompt-cards.json | [Pat McGown](https://github.com/pmcgown) ([@pmcgown](https://x.com/pmcgown))

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|października 11, 2024 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

- Be sure to check your locale’s separator setting when creating Calculated columns. Refer to the [Calculated column documentation](https://learn.microsoft.com/previous-versions/office/developer/sharepoint-2010/bb862071(v=office.14)) for more details.

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/prompt-cards" />
