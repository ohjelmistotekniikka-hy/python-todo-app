# TodoApp

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa tekemättömistään töistä eli todoista. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen tehtävälistansa.

Sovellus toimii myös Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikan menetelmät referenssisovelluksena. Sovelluksen tarkoituksena on demonstroida erästä tapaa tehdä suurin piirtein täysiin pisteisiin riittävä dokumentaatio sekä testaus projektillesi. Itse ohjelma on sen verran suppea, että saadaksesi kurssilta arvosanan 5 joudut tekemään hieman laajemman sovelluksen.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla `3.6.0`. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuut komennolla:

```bash
python3 -m poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
python3 -m poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
python3 -m poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
python3 -m poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
python3 -m poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
python3 -m poetry run invoke coveragereport
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
python3 -m poetry run invoke lint
```
