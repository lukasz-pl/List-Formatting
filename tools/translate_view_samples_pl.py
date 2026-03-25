#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/Users/lukasz_preihs/Documents/GitHub/List-Formatting/view-samples")

README_REPLACEMENTS = {
    "# View Formatting samples for SharePoint and Microsoft Lists": "# Próbki formatowania widoków dla SharePoint i Microsoft Lists",
    "Samples for use with View Formatting in SharePoint Online and Microsoft Lists. Samples are organized into dedicated folders with READMEs, screenshots, and everything needed to apply the sample in your own environment.": "Próbki do użycia z formatowaniem widoków w SharePoint Online i Microsoft Lists. Próbki są uporządkowane w osobnych folderach z plikami README, zrzutami ekranu i wszystkim, co potrzebne do zastosowania przykładu we własnym środowisku.",
    "There is a dedicated listing of view samples in our documentation site along with groupings to help find exactly the sample you need:": "Na naszej stronie z dokumentacją znajduje się osobna lista próbek widoków wraz z grupowaniami, które pomagają szybko znaleźć dokładnie ten przykład, którego potrzebujesz:",
    "* [View Samples](https://pnp.github.io/List-Formatting/viewsamples/) - Friendly display of ALL view samples": "* [Próbki widoków](https://pnp.github.io/List-Formatting/viewsamples/) - przyjazny widok WSZYSTKICH próbek widoków",
    "* [Groupings](https://pnp.github.io/List-Formatting/groupings/author/) - Various listings of samples by operators, tokens, author, class usage, etc.": "* [Grupowania](https://pnp.github.io/List-Formatting/groupings/author/) - różne zestawienia próbek według operatorów, tokenów, autora, użycia klas itd.",
    "## Summary": "## Podsumowanie",
    "## View requirements": "## Wymagania widoku",
    "## Requirements": "## Wymagania",
    "## Sample": "## Próbka",
    "## Samples": "## Próbki",
    "## Version history": "## Historia wersji",
    "## Disclaimer": "## Zastrzeżenie",
    "## Additional notes": "## Dodatkowe uwagi",
    "## Configuration": "## Konfiguracja",
    "## Usage": "## Użycie",
    "## Setup": "## Konfiguracja",
    "## How to use": "## Jak używać",
    "## Notes": "## Uwagi",
    "## References": "## Odnośniki",
    "## Instructions": "## Instrukcje",
    "## Customizations": "## Dostosowania",
    "## Features": "## Funkcje",
    "## Examples": "## Przykłady",
    "### Map API key": "### Klucz API map",
    "## Map preview fails to appear?": "## Podgląd mapy się nie wyświetla?",
    "### Column Types": "### Typy kolumn",
    "### Required fields": "### Wymagane pola",
    "### Optional fields": "### Pola opcjonalne",
    "Solution|Author(s)": "Rozwiązanie|Autor(zy)",
    "Solution | Author(s)": "Rozwiązanie | Autor(zy)",
    "Version|Date|Comments": "Wersja|Data|Uwagi",
    "Version | Date | Comments": "Wersja | Data | Uwagi",
    "Version|Date|Comment": "Wersja|Data|Uwagi",
    "Type|Internal Name|Required": "Typ|Nazwa wewnętrzna|Wymagane",
    "|Type|Internal Name|Required|": "|Typ|Nazwa wewnętrzna|Wymagane|",
    "All fields below should be part of the view, but only those marked with Required need to have values:": "Wszystkie poniższe pola powinny być częścią widoku, ale tylko te oznaczone jako Wymagane muszą mieć wartości:",
    "The key provided in the template (the ugly text after `&key`) should be changed to your own FREE API Key. This will ensure you don't receive errors from over usage of a shared key. Getting a key takes 2 minutes and is FREE: [Get API Key](https://developers.google.com/maps/documentation/static-maps/get-api-key)": "Klucz podany w szablonie (ten mało estetyczny tekst po `&key`) należy zmienić na własny, BEZPŁATNY klucz API. Dzięki temu unikniesz błędów wynikających z nadmiernego użycia współdzielonego klucza. Uzyskanie klucza zajmuje 2 minuty i jest BEZPŁATNE: [Pobierz klucz API](https://developers.google.com/maps/documentation/static-maps/get-api-key)",
    ">Note: Failure to switch the key to your own key leaves you open to future issues as other users use this key or if this key were to be revoked.": ">Uwaga: pozostawienie tego klucza bez zmiany na własny może w przyszłości powodować problemy, gdy inni użytkownicy będą go używać albo gdy zostanie unieważniony.",
    "Most likely you need to enable the HTML Field Security on your site. For details, see: [Allow or restrict the ability to embed content on SharePoint pages](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b)": "Najprawdopodobniej musisz włączyć zabezpieczenia pól HTML w swojej witrynie. Szczegóły znajdziesz tutaj: [Zezwalanie lub ograniczanie możliwości osadzania zawartości na stronach SharePoint](https://support.microsoft.com/office/allow-or-restrict-the-ability-to-embed-content-on-sharepoint-pages-e7baf83f-09d0-4bd1-9058-4aa483ee137b)",
    "This format takes advantage of CSS Flexbox to help make it responsive:": "Ten format wykorzystuje CSS Flexbox, aby lepiej działał responsywnie:",
    "**THIS CODE IS PROVIDED *AS IS* WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**": "**TEN KOD JEST DOSTARCZANY *W STANIE, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**",
    "Initial release": "Wersja początkowa",
    "Single line of text": "Pojedyncza linia tekstu",
    "Multiple lines of text": "Wiele linii tekstu",
    "Hyperlink": "Hiperłącze",
    "Number": "Liczba",
    "Date and Time": "Data i godzina",
    "Date": "Data",
    "Required": "Wymagane",
    "Comments": "Uwagi",
    "Friendly display of ALL view samples": "Przyjazny widok WSZYSTKICH próbek widoków",
    "Various listings of samples by operators, tokens, author, class usage, etc.": "Różne zestawienia próbek według operatorów, tokenów, autora, użycia klas itd.",
}

JSON_LITERAL_REPLACEMENTS = {
    "No picture available": "Brak dostępnego zdjęcia",
    "Class code": "Kod klasy",
    "Topic number": "Numer tematu",
    "Topic name": "Nazwa tematu",
    "Syllabus wording": "Treść podstawy programowej",
    "School developed teaching point": "Punkt dydaktyczny opracowany przez szkołę",
    "Topic ": "Temat ",
    "Dear ": "Dzień dobry ",
    "Register": "Zarejestruj",
    "Unregister": "Wyrejestruj",
    "Registered": "Zarejestrowano",
    "Course is full": "Brak miejsc na kursie",
    "Registration has ended": "Rejestracja została zakończona",
    "Open in App": "Otwórz w aplikacji",
    "Details": "Szczegóły",
    "Delete": "Usuń",
    "Open": "Otwórz",
    "Edit": "Edytuj",
    "Download": "Pobierz",
    "Send Email": "Wyślij e-mail",
    "Chat in Teams": "Czat w Teams",
    "Approve": "Zatwierdź",
    "Reject": "Odrzuć",
    "Comment": "Komentarz",
    "Share Item": "Udostępnij element",
    "Close window": "Zamknij okno",
    "Open Item": "Otwórz element",
    "Edit Item": "Edytuj element",
    "Delete Item": "Usuń element",
    "Preview file": "Podgląd pliku",
    "Copy link": "Kopiuj link",
    "Open in New Window": "Otwórz w nowym oknie",
    "Now": "Teraz",
    "YES": "TAK",
    "NO": "NIE",
    "Favorite": "Ulubione",
    "Remove Favorite": "Usuń z ulubionych",
    "Ask a Question": "Zadaj pytanie",
    "Resolve": "Rozwiąż",
    "Delivered": "Dostarczono",
    "In transit": "W transporcie",
    "Packed": "Spakowano",
    "Ready to be packed": "Gotowe do spakowania",
    "Shipped": "Wysłano",
    "Version history": "Historia wersji",
    "Step 1": "Krok 1",
    "Step 2": "Krok 2",
    "Step 3": "Krok 3",
    "Step 4": "Krok 4",
    "Step 5": "Krok 5",
    "World Time": "Czas na świecie",
    "Row Actions": "Akcje wiersza",
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

TRANSLATABLE_JSON_KEYS = {
    "txtContent",
    "title",
    "description",
    "aria-label",
    "altText",
    "text",
    "headerText",
    "runFlowButtonText",
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
        part = re.sub(r"\bAdditional Information\b", "Dodatkowe informacje", part)
        part = re.sub(r"\bAuthor\(s\)\b", "Autor(zy)", part)
        part = re.sub(r"(?<=\|)Yes(?=\|)", "Tak", part)
        part = re.sub(r"(?<=\|)No(?=\|)", "Nie", part)
        part = translate_date_line(part)
        part = re.sub(
            r"(?P<prefix>\|?\s*\d+\.\d+\|)(?P<month>[a-ząćęłńóśźż]+) (?P<day>\d{1,2}), (?P<year>\d{4})(?P<suffix>\|)",
            lambda m: f"{m.group('prefix')}{m.group('day')} {m.group('month')} {m.group('year')}{m.group('suffix')}",
            part,
        )
        parts[idx] = part
    return "".join(parts)


def should_translate_json_value(key: str, value: str) -> bool:
    if not isinstance(value, str):
        return False
    if key not in TRANSLATABLE_JSON_KEYS:
        return False
    if "http://" in value or "https://" in value:
        return False
    return True


def translate_json_text(value: str) -> str:
    for src, dst in sorted(JSON_LITERAL_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        value = value.replace(src, dst)
    return value


def translate_json_obj(obj):
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            if should_translate_json_value(key, value):
                result[key] = translate_json_text(value)
            else:
                result[key] = translate_json_obj(value)
        return result
    if isinstance(obj, list):
        return [translate_json_obj(item) for item in obj]
    return obj


def main() -> None:
    for path in ROOT.rglob("*.md"):
        original = path.read_text(encoding="utf-8")
        translated = translate_markdown(original)
        if translated != original:
            path.write_text(translated, encoding="utf-8")

    for path in ROOT.rglob("*.json"):
        if "/assets/" in path.as_posix() or "/provisioning/" in path.as_posix():
            continue
        try:
            original_text = path.read_text(encoding="utf-8")
            data = json.loads(original_text)
        except Exception:
            continue
        translated = translate_json_obj(data)
        if translated == data:
            continue
        new_text = json.dumps(translated, ensure_ascii=False, indent=2) + "\n"
        if new_text != original_text:
            path.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
