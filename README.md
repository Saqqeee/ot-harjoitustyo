# Ohjelmistotekniikka, harjoitustyö

Tähän repositorioon syntyy yksinkertainen versio Tetris-videopelistä. Viimeisin julkaisu löytyy [täältä](https://github.com/Saqqeee/ot-harjoitustyo/releases/latest).

## Dokumentaatio
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

### Suorittaminen
Asenna pelin vaatimat riippuvuudet:
```
poetry install
```
Suorita sovellus:
```
poetry run invoke start
```

### Pelaaminen
Tällä hetkellä pelistä löytyvät seuraavat toiminnot:

 - `A` / `←`: Vasen
 - `D` / `→`: Oikea
 - `S` / `↓`: Alas hitaasti ("soft drop")
 - `W` / `↑`: Alas nopeasti ("hard drop")

### Muita komentorivitoimintoja
Pelin testit voi suorittaa seuraavalla komennolla:
```
poetry run invoke test
```
Testikattavuusraportin saa HTML-muodossa komennolla:
```
poetry run invoke coverage-report
```
Pylint-raportin saa tulostettua komennolla:
```
poetry run invoke lint
```
