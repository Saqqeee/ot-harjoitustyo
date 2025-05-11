# Käyttöohje

Lataa sovelluksen viimeisin [release](https://github.com/Saqqeee/ot-harjoitustyo/releases/latest)
ja pura lähdekoodi haluamaasi kansioon.

## Ohjelman asentaminen ja suorittaminen

Käynnistääksesi pelin sinun täytyy ensin asentaa sen tarvitsemat riippuvuudet,
mikä onnistuu näppärästi kirjoittamalla komentoriviin komento:

```
poetry install
```

Kun riippuvuudet on asennettu, peli on suoraan käynnistettävissä komennolla:

```
poetry run invoke start
```

## Pelaaminen

Pelin tarkoitus on ohjata putoava Tetromino suotuisaan paikkaan,
jotta kukin rivi täyttyisi neliöistä. Pelin ohjaus näyttää seuraavalta:

 - `A` / `←`: Vasen
 - `D` / `→`: Oikea
 - `W` / `↑`: Kääntö myötäpäivään
 - `S` / `↓`: Alas hitaasti ("soft drop")
 - Välilyönti: Alas nopeasti ("hard drop")

Nämä nappulat näkyvät myös itse peli-ikkunassa.