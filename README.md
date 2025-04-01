# Ohjelmistotekniikka, harjoitustyö

Tähän repositorioon syntyy yksinkertainen versio Tetris-videopelistä. Peliä ei vielä
nykyisessä muodossaan voi todellisuudessa pelata.

## Dokumentaatio
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Changelog](dokumentaatio/changelog.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)

### Suorittaminen
Asenna pelin vaatimat riippuvuudet:
```
poetry install
```
Suorita sovellus:
```
poetry run invoke start
```

### Muita komentorivitoimintoja
Pelin testit voi suorittaa seuraavalla komennolla:
```
poetry run invoke test
```
Testikattavuusraportin saa HTML-muodossa komennolla:
```
poetry run invoke coverage-report
```