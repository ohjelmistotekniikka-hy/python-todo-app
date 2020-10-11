# TodoApp

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa tekemättömistään töistä eli todoista. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen tehtävälistansa.

Sovellus toimii myös Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikan menetelmät referenssisovelluksena. Sovelluksen tarkoituksena on demonstroida erästä tapaa tehdä suurin piirtein täysiin pisteisiin riittävä dokumentaatio sekä testaus projektillesi. Itse ohjelma on sen verran suppea, että saadaksesi kurssilta arvosanan 5 joudut tekemään hieman laajemman sovelluksen.

## Riippuvuudet

1. Sovelluksen toiminta on testattu Python versiolla `3.9.0`. Etenkin vanhempien Python versioiden kanssa saattaa ilmentyä ongelmia. Voit tarkistaa Python versiosi komennolla:

```bash
python --version
```

Jos käytössäsi on eri versio, uuden version asennus onnistuu vaivattomasti [pyenv](https://github.com/pyenv/pyenv)-kirjaston avulla.

2. Sovelluksen riippuvuuksien hallinnassa käytetään [pipenv](https://github.com/pypa/pipenv)-kirjastoa.

3. Sovelluksen riippuvuudet täytyy asentaa ennen ohjelman suorittamista komennolla:

```bash
pipenv install
```

4. Sovelluksen käyttämä SQLite-tietokanta täytyy alustaa ennen sovelluksen käyttöä. Alustus onnistuu komennolla:

```bash
pipenv run initialize-database
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
PIPENV_DOTENV_LOCATION=.env.test pipenv run test
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset suoritetaan komennolla:

```bash
pipenv run lint
```

