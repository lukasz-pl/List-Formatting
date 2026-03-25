# Linear Gauge

## Podsumowanie

Ta próbka pokazuje displaying a linear gauge from a regular string set to the split operator.

![zrzut ekranu próbki](./assets/screenshot.png)

## Wymagania widoku

- Ten format można zastosować do a Liczba column.

## How to apply this sample

Ta próbka wymaga dostosowania do konkretnego zastosowania. Konieczne są dwie zmiany.

### Krok 1: Set the min and max values

1. Znajdź the split operator on line 31 of the JSON.
2. Adjust the min and max values to match your desired range.

    ```
    "forEach": "_overallRange in split('min:MIN_VALUE,max:MAX_VALUE','^')",

    # Example 1
    "forEach": "_overallRange in split('min:0,max:100','^')",

    # Example 2
    "forEach": "_overallRange in split('min:-150,max:250','^')",

    # Example 3
    "forEach": "_overallRange in split('min:0,max:1','^')",
    ```

    ![zrzut ekranu the gauge setting](./assets/gauge-setting.png)

### Krok 2: Set numerical range, background color, and range name

1. Znajdź the split operator on line 50 of the JSON.
2. Adjust the numerical range, background color, and range name for each range according to your use case. Use a comma-separated format.

    ```
    "forEach": "_range in split('RANGE_MIN[<= or <]n[<= or <]RANGE_MAX:BACKGROUND_COLOR:RANGE_NAME',',')",

    # Example 1
    "forEach": "_range in split('0<=n<30:#9ED9D2:C,30<=n<80:#F7D358:B,80<=n<=100:#F4A7B9:A',',')",

    # Example 2
    "forEach": "_range in split('-99999<=n<0:#c190f0:D,0<=n<100:#9ED9D2:C,100<=n<200:#F7D358:B,200<=n<=99999:#F4A7B9:A',',')",

    # Example 3
    "forEach": "_range in split('0<=n<0.4:#9ED9D2:C,0.4<=n<0.8:#F7D358:B,0.8<=n<=1:#F4A7B9:A',',')",
    ```

    - **RANGE_MIN[<= or <]n[<= or <]RANGE_MAX:** Specifies the range of values for each segment of the linear gauge.
        - Example: `0<=n<30`, `0<n<=30`, `0<=n<=30`, `0<n<30`

    - **BACKGROUND_COLOR:** Defines the background color for the respective range.
        - Example: `#9ED9D2`, `Blue`

    - **RANGE_NAME:** Set the text to be displayed in the range.
        - Example: `A`, `Range_B`, `Great`

    ![zrzut ekranu the range setting](./assets/range-setting.png)

> [!NOTE]  
> - Expressions such as `n>=20` or `20<n` are not acceptable for numeric ranges. Please strictly adhere to the specified format `RANGE_MIN[<= or <]n[<= or <]RANGE_MAX`.
> - The value range can exceed the linear gauge's min and max.
> - Make sure that the values do not overlap between ranges.
> - Avoid single-byte spaces in the string to prevent errors. For single-byte spaces in range names, use an underscore (\_) instead. The underscore (\_) will be converted to half-width spaces when displayed. (Related link: [#642](https://github.com/pnp/List-Formatting/issues/642))
> - Do not use `<`, `:`, `=`, and `,` in range names.
> - When configuring percentage values, ensure that they are set as decimals. For example, if you want to represent 50%, set the value as `0.5` instead of `50`.

#### Range setting examples:

- Using HTML color code:
    ```
    80<=n<=100:#F4A7B9:A
    ```

- Using HTML color name:
    ```
    30<=n<80:Yellow:B
    ```

- Range name not set:
    ```
    50<=n<60:#00FF00:
    ```

- Using an underscore (\_) instead of single-byte spaces in the range name:
    ```
    90<=n<=100:#FFD700:Range_D
    ```

## Przykład

Rozwiązanie|Autor(zy)
--------|---------
number-linear-gauge.json | [Tetsuya Kawahara](https://github.com/tecchan1107)

## Historia wersji

Wersja |Data             |Uwagi
--------|-----------------|--------
1.0     |grudnia 1, 2023 |Wersja początkowa

## Zastrzeżenie
**TEN KOD JEST DOSTARCZANY W STANIE *TAKIM, W JAKIM JEST*, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ ANI DOROZUMIANEJ, W TYM TAKŻE DOROZUMIANYCH GWARANCJI PRZYDATNOŚCI DO OKREŚLONEGO CELU, WARTOŚCI HANDLOWEJ ANI NIENARUSZANIA PRAW.**

---

## Dodatkowe uwagi

### About the size of the linear gauge

The linear gauge adjusts based on the column width.

### About formulas in JSON

![zrzut ekranu the explanatory diagram](./assets/explanatory-diagram.png)

The style properties of each range are set to the following values:  

|Style|Value|
|---|---|
|display|<ul><li>**if (Rmax<=Gmin&#124;&#124;Gmax<=Rmin&#124;&#124;Rmin>Rmax):** none</li><li>**Otherwise:** flex</li></ul>|
|width|<ul><li>**if (Rmin<Gmin):** $$\frac{R_{max}-G_{min}}{G_{max}-G_{min}}*100\\%$$</li><li>**Otherwise:** $$\frac{R_{max}-R_{min}}{G_{max}-G_{min}}*100\\%$$</li></ul>|
|max-width|<ul><li>**if (Rmin<Gmin):** $$\frac{G_{max}-G_{min}}{G_{max}-G_{min}}*100\\%$$</li><li>**Otherwise:** $$\frac{G_{max}-R_{min}}{G_{max}-G_{min}}*100\\%$$</li></ul>|
|left|<ul><li>**if (Rmin<Gmin):** $$\frac{0}{G_{max}-G_{min}}*100\\%$$</li><li>**Otherwise:** $$\frac{R_{min}-G_{min}}{G_{max}-G_{min}}*100\\%$$</li></ul>| 

The characters used in the above formula and their meanings are as follows:        

|Character|Meaning|Formula in JSON|
|---|---|---|
|$$G_{max}$$|Max value of linear gauge|Liczba\(substring\(\[$_overallRange\],indexOf\(\[$_overallRange\],'max:'\)+4,indexOf\(\[$_overallRange\]+'^','^'\)\)\)|
|$$G_{min}$$|Min value of linear gauge|Liczba\(substring\(\[$_overallRange\],indexOf\(\[$_overallRange\],'min:'\)+4,indexOf\(\[$_overallRange\],','\)\)\)|
|$$R_{max}$$|Max value of each range|Liczba\(replaceAll\(substring\(\[$_range\],lastIndexOf\(\[$_range\],'<'\)+1,indexOf\(\[$_range\],':'\)\),'=',''\)\)|
|$$R_{min}$$|Min value of each range|Liczba\(substring\(\[$_range\],0,indexOf\(\[$_range\],'<'\)\)\)|

<img src="https://pnptelemetry.azurewebsites.net/list-formatting/column-samples/number-linear-gauge" />
