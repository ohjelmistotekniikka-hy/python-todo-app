# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa tekemättömistään töistä eli _todoista_. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen tehtävälistansa.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan yksi käyttäjärooli eli _normaali käyttäjä_. Myöhemmin sovellukseen saatetaan lisätä suuremmilla oikeuksilla varustettu _pääkäyttäjä_.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri näkymästä

![](./kuvat/kayttoliittyma-hahmotelma.png)

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirtyä uuden käyttäjän luomisnäkymään tai onnistuneen kirjautumisen yhteydessä kirjaantuneen käyttäjän tehtävälistaan.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen

- Käyttäjä näkee omat tekemättömät työt eli _todot_
- Käyttäjä voi luoda uuden todon
  - Luotu todo näkyy ainoastaan sen luoneelle käyttäjälle
- Käyttäjä voi merkitä todon tehdyksi, jolloin todo häviää listalta
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Tehdyksi merkittyjen todojen tarkastelu
- Tehdyksi merkittyjen todojen merkkaaminen tekemättömiksi
- Todon tietojen editointi
- Todojen järjestely tärkeysjärjestykseen
- Todojen määrittely muille käyttäjille
- Käyttäjätiimit, jotka näkevät kaikki yhteiset todot
- Mahdollisuus useampaan erilliseen todo-listaan
- Lisätään todoon kenttä, johon on mahdollista merkitä tarkempia todoon liittyviä tietoja
- Käyttäjätunnuksen (ja siihen liittyvien todojen) poisto
