# Announcements

## Podsumowanie

This sample formats your view to look like a Announcements card with a similiar style to Viva Connection Cards when on a SharePoint Page. In Microsoft Lists it will also show an image that you can connect with the Announcement.

![zrzut ekranu próbki](./assets/screenshot.png)

![zrzut ekranu the sample on a Modern page](./assets/screenshot2.png)

## Wymagania widoku

| Column Name         | Type                                   | Internal Column Name |
| ------------------- | -------------------------------------- | -------------------- |
| Title               | Single Line Text                       | Title                |
| Description         | Single Line Text                       | Description          |
| TypeAnn             | Choice (Error, Success, Info, Warning) | TypeAnn              |
| RemoveData         | Data i godzina                          | RemoveData          |
| (optional) ImgHover | Image                                | ImgHover             |

## Próbka

Rozwiązanie|Autor(zy)
--------|---------
announcements.json | [David Ramalho](https://github.com/DRamalho92)

## Historia wersji

| Version | Data               | Uwagi        |
| ------- | ------------------ | --------------- |
| 1.0     | grudnia 1, 2021   | Wersja początkowa |
| 1.1     | września 17, 2023 | The new Image column can now be created, and the use of the Image column is now common when using images. Therefore, changed the type of ImgHover column from Picture column to Image column. |
| 1.2     | listopada 1, 2024   | Fixed image path and black text for dark theme. |

## Zastrzeżenie

**THIS CODE IS PROVIDED _AS IS_ WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/view-samples/announcements" />
