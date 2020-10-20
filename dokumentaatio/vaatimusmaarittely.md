<!-- TODO -->
# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa tekemättömistään töistä eli _todoista_. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen tehtävälistansa.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli _normaali käyttäjä_. Myöhemmin sovellukseen saatetaan lisätä suuremmilla oikeuksilla varustettu _pääkäyttäjä_.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri näkymästä

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/v-1.png" width="750">

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirtyä uuden käyttäjän luomisnäkymään tai onnistuneen kirjautumisen yhteydessä kirjaantuneen käyttäjän tehtävälistaan.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä

- käyttäjä voi kirjautua järjestelmään
  - kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus kirjautumislomakkeelle
  - jos käyttäjää ei olemassa, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- käyttäjä näkee omat tekemättömät työt eli _todot_

- käyttäjä voi luoda uuden todon
  - luotu todo näkyy ainoastaan sen luoneelle käyttäjälle

- käyttäjä voi merkitä todon tehdyksi, jolloin todo häviää listalta

- käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla

- tehdyksi merkittyjen todojen tarkastelu
- tehdyksi merkittyjen todojen merkkaaminen tekemättömiksi
- todon tietojen editointi
- todojen järjestely tärkeysjärjestykseen
- todojen määrittely muille käyttäjille
- käyttäjätiimit, jotka näkevät kaikki yhteiset todot
- mahdollisuus useampaan erilliseen todo-listaan
- lisätään todoon kenttä, johon on mahdollista merkitä tarkempia todoon liittyviä tietoja
- käyttäjien yhteyteen salasana, joka vaaditaan kirjautuessa
- käyttäjätunnuksen (ja siihen liittyvien todojen) poisto
