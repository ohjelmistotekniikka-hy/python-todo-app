# Changelog

## Viikko 3

- Käyttäjä näkee listan kaikista tehtävistä
- Lisätty TodoRepository-luokka, joka vastaa tehtävien tallennuksesta CSV-tiedostoon
- Lisätty TodoService-luokka, joka vastaa sovelluslogiikan koodista
- Testattu, että TodoRepository-luokka palauttaa kaikki tehtävät

## Viikko 4

- Käyttäjä voi lisätä tehtävän
- Käyttäjä voi merkata tehtävän tehdyksi
- Käyttäjä näkee tehtävien listauksessa vain tekemättömät tehtävät
- Refaktoroitu tiedostoon tallennukseen liittyvää koodia TodoRepository-luokassa
- Testattu, että TodoRepository-luokka merkitsee tehtävät tehdyksi ja TodoService-luokka palauttaa tekemättömät tehtävät

## Viikko 5

- Käyttäjä voi rekisteröityä
- Lisätty UserRepository-luokka, joka vastaa käyttäjien tallennuksesta SQLite-tietokantaan
- Testattu, että UserRepository- ja TodoService-luokat toimivat käyttäjän luonnin osalta

## Viikko 6

- Käyttäjä voi kirjautua sisään
- Refaktoroitu TodoService-luokkaa kirjautuneen käyttäjän tietojen osalta
- Testattu, että kirjautuminen onnistuu oikealla salasanalla ja epäonnistuu väärällä salasanalla TodoService-luokassa 
