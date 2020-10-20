<!-- TODO -->
# Käyttöohje

Lataa tiedosto [todoapp.jar](https://github.com/mluukkai/OtmTodoApp/releases/tag/0.1)

## Konfigurointi

Ohjelma olettaa, että sen käynnistyshakemistossa on konfiguraatiotiedosto _config.properties_, joka määrittelee käyttäjät ja todot tallettavien tiedostojen nimet. Tiedoston muoto on seuraava

```
userFile=users.txt
todoFile=todos.txt
```

## Ohjelman käynnistäminen

Ohjelma käynnistetään komennolla 

```
java -jar todoapp.jar
```

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/k-1.png" width="400">

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus syötekenttään ja painamalla _login_.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään panikkeella _create new user_.

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla _create_

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/k-2.png" width="400">

Jos käyttäjän luominen onnistuu, palataan kirjautumisnäkymään.

## Todojen luominen ja tehdyksi merkkaaminen

Onnistuneen kirjautumisen myötä siirrytään käyttäjien tekemättömät työt listaavaan näkymään

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/k-3.png" width="400">

Näkymä mahdollistaa olemassaolevien todojen merkkaamisen tehdyksi painikkeella _done_ sekä uusien todojen luomisen kirjoittamalla syötekenttään tehtävän kuvauksen ja painamalla _create_. 

Klikkaamalla näkymän oikean ylänurkan painiketta _logout_ käyttäjä kirjautuu ulos sovelluksesta ja sovellus palaa takaisin kirjaantumisnäkymään.
