<!-- TODO -->
# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus _ui_ sisältää käyttöliittymästä, _services_ sovelluslogiikasta ja _repositories_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Kirjautuminen
- Uuden käyttäjän luominen
- Todo-lista

Jokainen näistä on toteutettu omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainoastaan kutsuu [TodoService](../src/services/todo_service.py)-luokan metodeja.

Kun sovelluksen todo-listan tilanne muuttuu, eli uusi käyttäjä kirjautuu, todoja merkitään tehdyksi tai niitä luodaan, kutsutaan sovelluksen metodia [redrawTodolist](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/ui/TodoUi.java#L68) joka renderöi todolistanäkymän uudelleen sovelluslogiikalta saamansa näytettävien todojen listan perusteella.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat [User](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/entities/user.py) ja [Todo](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/entities/todo.py), jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

![Tietomalli](./kuvat/tietomalli.png)

Toiminnallisista kokonaisuuksista vastaa luokkan [TodoService](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/services/todo_service.py) ainoa olio. Luokka tarjoaa kaikille käyttäliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi:

- `login(username, password)`
- `get_undone_todos()`
- `create_todo(content)`
- `set_todo_done(todo_id)`

_TodoService_ pääsee käsiksi käyttäjiin ja todoihin tietojen tallennuksesta vastaavan pakkauksessa _repositories_ sijaitsevien luokkien [TodoRepository](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/repositories/todo_repository.py) ja [UserRepository](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/repositories/user_repository.py) kautta. Luokkien toteutuksen [injektoidaan](https://en.wikipedia.org/wiki/Dependency_injection) sovelluslogiikalle konstruktorikutsun yhteydessä.

`TodoService`-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![Pakkausrakenne ja luokat](./kuvat/arkkitehtuuri-pakkaus-luokat.png)

## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokat `TodoRepository` ja `UserRepository` huolehtivat tietojen tallettamisesta. `TodoRepository`-luokka tallentee tietoa CSV-tiedostoon, kun taas `UserRepository`-luokka SQLite-tietokantaan.

Luokat noudattavat [Repository](https://en.wikipedia.org/wiki/Data_access_object) -suunnittelumallia ja ne on tarvittaessa mahdollista korvata uusilla toteutuksilla, jos sovelluksen datan talletustapaa päätetään vaihtaa. Sovelluslogiikan testauksessa hyödynnetäänkin tätä siten, että testeissä käytetään tiedostoon ja tietokantaan tallentavien olioiden sijaan keskusmuistiin tallentavia toteutuksia.

### Tiedostot

Sovellus tallettaa käyttäjien ja todojen tiedot erillisiin tiedostoihin.

Sovelluksen juureen sijoitettu [konfiguraatiotiedosto](./kayttoohje.md#konfiguraatiotiedosto) [.env](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/.env) määrittelee tiedostojen nimet.

Sovellus tallettaa tehtävät CSV-tiedostoon seuraavassa formaatissa:

```
65eef813-330a-4714-887b-2bda4d744487;opiskele pythonia;1;kalle
5749b61f-f312-45ef-94a1-71a758feee2b;kirjoita dokumentaatio;0;matti
```

Eli tehtävän id, sisältö, tehtystatus (0 = ei tehty, 1 = on tehty) ja käyttäjän käyttäjätunnus. Kenttien arvot erotellaan puolipisteellä (;).

Käyttäjät tallennetaan SQLite-tietokannan tauluun `users`, joka alustetaan [initialize_database.py](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/initialize_database.py)-tiedostossa.

### Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

#### käyttäjän kirjaantuminen

Kun kirjautumisnäkymän syötekenttiin kirjoitetetataan käyttäjätunnus ja salasana, jonka jälkeen klikataan painiketta _Login_, etenee sovelluksen kontrolli seuraavasti:

![](./kuvat/sekvenssi-kirjautuminen.png)

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/login_view.py#L182) kutsuu sovelluslogiikan `TodoService` metodia [login](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/TodoService.java#L73) antaen parametriksi kirjautuneen käyttäjätunnuksen. Sovelluslogiikka selvittää _userDao_:n avulla onko käyttäjätunnus olemassa. Jos on, eli kirjautuminen onnistuu, on seurauksena se että käyttöliittymä vaihtaa näkymäksi _todoScenen_, eli sovelluksen varsinaisen päänäkymän ja renderöi näkymään kirjautuneen käyttäjän todot eli tekemättömät tehtävät.

#### uuden käyttäjän luominen

Kun uuden käyttäjän luomisnäkymässä on syötetty käyttäjätunnus joka ei ole jo käytössä sekä nimi ja klikataan painiketta _createUser_ etenee sovelluksen kontrolli seuraavasti:

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/a-5.png" width="750">

[Tapahtumakäsittelijä](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/ui/TodoUi.java#L138) kutsuu sovelluslogiikan metodia [createUser](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/TodoService.java#L111) antaen parametriksi luotavan käyttäjän tiedot. Sovelluslogiikka selvittää _userDao_:n avulla onko käyttäjätunnus olemassa. Jos ei, eli uuden käyttäjän luominen on mahdollista, luo sovelluslogiikka _User_-olion ja tallettaa sen kutsumalla _userDao_:n metodia _create_. Tästä seurauksena on se, että käyttöliittymä vaihtaa näkymäksi _loginScenen_ eli kirjautumisnäkymän.

#### Todon luominen

Uuden todon luovan _createTodo_-painikkeen klikkaamisen jälkeen sovelluksen kontrolli eteneeseuraavasti:

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/a-6.png" width="750">

[Tapahtumakäsittelijä](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/ui/TodoUi.java#L193) kutsuu sovelluslogiikan metodia [createTodo](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/TodoService.java#L29) antaen parametriksi luotavan työn tiedot. Sovelluslogiikka luo uuden _Todo_-olion ja 
 tallettaa sen kutsumalla _todoDao_:n metodia _create_. Tästä seurauksena on se, että käyttöliittymä päivittää näytettävät todot kutsumalla omaa metodiaan _redrawTodolist_.

#### Muut toiminnallisuudet

Sama periaate toistoo sovelluksen kaikissa toiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia, sovelluslogiikka päivittää todojen tai kirjautuneen käyttäjän tilaa. Kontrollin palatessa käyttäliittymään, päivitetään tarvittaessa todojen lista sekä aktiivinen näkyvä.

## Ohjelman rakenteeseen jääneet heikkoudet

### käyttöliittymä

Graafinen käyttöliittymä on toteutettu määrittelemällä lähes koko käyttöliittymän struktuuri luokan _TodoUi_ metodissa _start_. Ainakin kaikkien sovelluksen kolmen päänäkymän rakentava koodi olisi syytä erottaa omiksi metodeikseen tai kenties luokiksi. Muuttujien nimentää olisi myös syytä parantaa. 

Käyttöliittymän rakenteen ohjelmallinen määrittely kannattaisi kenties korvata FXML-määrittelyllä, tällöin sovelluslogiikan ja käyttöliittymän tapahtumankäsittelijöiden välinen kommunikointi ei hukkuisi GUI-elementtejä rakentavan koodin sekaan.

### DAO-luokat

FileDao-toteutuksiin on jäänyt paljon toisteista koodia, molemmat mm. sisältävät hyvin samankaltaisen logiikan tiedoston lukemiseen ja tidostoon kirjoittamiseen. Tämä koodi olisi syytä eroittaa omaan luokkaansa.

DAO-toteutusten automaattiset testit tekisivät refaktoroinnin suhteellisen riskittömäksi.
