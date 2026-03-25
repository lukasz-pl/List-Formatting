# Certificate Card Formatting

This sample uses **SharePoint List View Formatting** to display a **certificate-style card** for each employee.  
Each row in the list is transformed into a visually rich certificate layout, including logos, employee details, certification information, and program authority.

![zrzut ekranu próbki](./assets/screenshot.png)

## View Requirements

Create a list with the following columns:

| Internal Name         | Type                     |
|-----------------------|--------------------------|
| **Title**             | Pojedyncza linia tekstu      |
| **EmployeeName**      | Pojedyncza linia tekstu      |
| **CertificationName** | Pojedyncza linia tekstu      |
| **CertificateID**     | Pojedyncza linia tekstu      |
| **IssueData**         | Data i godzina            |
| **ExpiryData**        | Data i godzina            |
| **HRManager**         | Pojedyncza linia tekstu      |


## Próbka Data

| Title   | EmployeeName | CertificationName            | CertificateID | IssueData           | ExpiryData          | HRManager    |
|---------|--------------|-----------------------------|---------------|-------------------|-------------------|-------------|-------|
| Cert 1  | Sai Bandaru     | Microsoft Learn Fundamentals | CERT7884w6     | 2025-08-01T04:00:00Z | 2026-08-01T04:00:00Z | Budvik B  |

## Podsumowanie

- Each row is displayed as a **certificate card** with a logo, employee name, certification name, and details.
- **Employee Name** is highlighted with gradient text and uppercase letters.
- **Credential Information** (Certificate ID, Issue Data, Expiry Data) is shown on the bottom left.
- **Program Authority** (HR Manager) is shown on the bottom right with a signature line.
- Optional **watermark image** appears at the bottom-left of the certificate.
- A **checkmark badge** indicates successful completion.

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
certificate-card.json | [Sai Bandaru](https://github.com/saiiiiiii)

## Historia wersji

Wersja|Data|Uwagi
-------|----|--------
1.0|26 sierpnia 2025|Wersja początkowa

## Zastrzeżenie

**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Additional Notes

- Change the Logo in the json code because SharePoint blocks images from other domains if they don’t allow CORS (cross-origin requests). Best fix → store images in SharePoint (same domain) or ensure the external server sets Access-Control-Allow-Origin: *. 
- Works best in **List view** with `EmployeeName` sorted ascending.
- You can adjust **logo, colors, and shadows** in the JSON to match your corporate branding.
- Compatible with **SharePoint Online Modern Lists**.  

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/certificate-card" />