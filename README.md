# TodoApp

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa tekemättömistään töistä eli todoista. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen tehtävälistansa.

Sovellus toimii myös Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikan menetelmät referenssisovelluksena. Sovelluksen tarkoituksena on demonstroida erästä tapaa tehdä suurin piirtein täysiin pisteisiin riittävä dokumentaatio sekä testaus projektillesi. Itse ohjelma on sen verran suppea, että saadaksesi kurssilta arvosanan 5 joudut tekemään hieman laajemman sovelluksen.

## Vaatimukset

- Sovelluksen toiminta on testattu Python versiolla `3.9.0`. Etenkin vanhempien Python versioiden kanssa saattaa ilmentyä ongelmia. Voit tarkistaa Python versiosi komennolla:

```bash
python --version
```

Jos käytössäsi on eri versio, uuden version asennus onnistuu vaivattomasti [pyenv](https://github.com/pyenv/pyenv)-työkalun avulla

- Sovelluksen riippuvuuksien hallinnassa käytetään [pipenv](https://github.com/pypa/pipenv)-kirjastoa, jonka asentaminen on välttämätöntä sovelluksen käytön kannalta

## Asennus

1. Asenna riippuvuut komennolla:

```bash
pipenv install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
pipenv run build
```

3. Käynnistä sovellus komennolla:

```bash
pipenv run start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
pipenv run start
```

### Testaus

Testit suoritetaan komennolla:

```bash
pipenv run test
```

### Testikattavuus

Testikattavuus kerätään kommenolla:

```bash
pipenv run coverage
```

Tämän jälkeen raportin voi katsoa komennolla:

```bash
pipenv run coverage-report
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset suoritetaan komennolla:

```bash
pipenv run lint
```
