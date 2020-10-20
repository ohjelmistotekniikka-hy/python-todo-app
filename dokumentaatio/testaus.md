<!-- TODO -->
# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein JUnitilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### sovelluslogiikka

Automatisoitujen testien ytimen moudostavat sovelluslogiikkaa, eli pakkauksen [todoapp.domain](https://github.com/mluukkai/OtmTodoApp/tree/master/src/main/java/todoapp/domain) luokkia testaavat integraatiotestit [TodoServiceUserTest](https://github.com/mluukkai/OtmTodoApp/blob/master/src/test/java/todoapp/domain/TodoServiceUserTest.java) ja [TodoServiceTodoTest](https://github.com/mluukkai/OtmTodoApp/blob/master/src/test/java/todoapp/domain/TodoServiceUserTest.java) joiden määrittelevät testitapaukset simuloivat käyttöliittymän [TodoService](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/TodoService.java)-olin avulla suorittamia toiminnallisuuksia.

Integraatiotestit käyttävät datan pysyväistallennukseen DAO-rajapintojen keskusmuistitoteutuksia [FakeTodoDao](https://github.com/mluukkai/OtmTodoApp/blob/master/src/test/java/todoapp/domain/FakeTodoDao.java) ja [FakeUserDao](https://github.com/mluukkai/OtmTodoApp/blob/master/src/test/java/todoapp/domain/FakeTodoDao.java)

Sovelluslogiikkakerroksen luokille [User](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/User.java) ja [Todo](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/User.java) on tehty muutama yksikkötesti kattamaan tapaukset, joita integraatiotestit eivät kata (mm. olioiden _equals_-metodit).

### DAO-luokat

Molempien DAO-luokkien toiminnallisuus on testattu luomalla testeissä tilapäinen tiedosto hyödyntäen JUnitin [TemporaryFolder](https://junit.org/junit4/javadoc/4.12/org/junit/rules/TemporaryFolder.html)-ruleja.

### Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen rivikattavuus on 94% ja haarautumakattavuus 96%

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/t-1.png" width="800">

Testaamatta jäivät tilanteet, joissa käyttäjät tai tehtävät tallettavia tiedostoja ei ole, tai niihin ei ole luku- ja kirjoitusoikeutta.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](https://github.com/mluukkai/OtmTodoApp/blob/master/dokumentaatio/kayttoohje.md) kuvaamalla tavalla sekä OSX- että Linux-ympäristöön siten, että sovelluksen käynnistyshakemistossa on ollut käyttöohjeen kuvauksen mukainen _config.properties_-tiedosto.

Sovellusta on testattu sekä tilanteissa, joissa käyttäjät ja työt tallettavat tiedostot ovat olleet olemassa ja joissa niitä ei ole ollut jolloin ohjelma on luonut ne itse.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](https://github.com/mluukkai/OtmTodoApp/blob/master/dokumentaatio/vaatimusmaarittely.md#perusversion-tarjoama-toiminnallisuus) ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi. Kaikkien toiminnallisuuksien yhteydessä on syötekentät yritetty täyttää myös virheellisillä arvoilla kuten tyhjillä.

## Sovellukseen jääneet laatuongelmat

Sovellus ei anna tällä hetkellä järkeviä virheilmoituksia, seuraavissa tilanteissa
- konfiguraation määrittelemiin tiedostoihin ei ole luku/kirjoitusoikeuksia
