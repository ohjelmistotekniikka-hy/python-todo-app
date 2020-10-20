<!-- TODO -->
# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne koostuu _src_-hakemiston sisällä olevasta koodista. Koodi on organisoitu _entities_-, _repositories_-, _services_-, _tests_- ja _ui_-hakemistoihin:  

- Hakemisto _entities_ sisältää koodia, jonka avulla mallinnetaan sovelluksen käyttämää tietoa
- Hakemisto _repositories_ sisältää pysyväistallennuksesta vastaavaa koodia
- Hakemisto _services_ sisältää sovelluslogiikkaan liittyvää koodia
- Hakemisto _tests_ sisältää testit
- Hakemisto _ui_ sisältää käyttöliittymään liittyvää koodia

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Kirjautuminen
- Uuden käyttäjän luominen
- Todo-lista

Jokainen näistä on toteutettu omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainoastaan kutsuu [TodoService](../src/services/todo_service.py)-luokan metodeja.

Kun sovelluksen todo-listan tilanne muuttuu, eli uusi käyttäjä kirjautuu, todoja merkitään tehdyksi tai niitä luodaan, kutsutaan sovelluksen metodia [redrawTodolist](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/ui/TodoUi.java#L68) joka renderöi todolistanäkymän uudelleen sovelluslogiikalta saamansa näytettävien todojen listan perusteella.

## Sovelluslogiikka

Sovelluksen loogisen datamallin muodostavat luokat [User](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/User.java) ja [Todo](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/Todo.java), jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/a-2.png" width="400">

Toiminnallisista kokonaisuuksista vastaa luokkan [TodoService](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/TodoService.java) ainoa olio. Luokka tarjoaa kaikille käyttäliittymän toiminnoille oman metodin. Näitä ovat esim.
- boolean login(String username)
- List<Todo> getUndone() 
- void createTodo(String content, User user)
- void markDone(int id)

_TodoService_ pääsee käsiksi käyttäjiin ja todoihin tietojen tallennuksesta vastaavan pakkauksessa _todoapp.dao_ sijaitsevien rajapinnat _TodoDao_ ja _UserDao_ toteuttavien luokkien kautta. Luokkien toteutuksen [injektoidaan](https://en.wikipedia.org/wiki/Dependency_injection) sovelluslogiikalle konstruktorikutsun yhteydessä.

TodoServicen ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/a-3c.png" width="450">

## Tietojen pysyväistallennus

Pakkauksen _todoapp.dao_ luokat _FileTodoDao_ ja _FileUserDao_ huolehtivat tietojen tallettamisesta tiedostoihin.

Luokat noudattavat [Data Access Object](https://en.wikipedia.org/wiki/Data_access_object) -suunnittelumallia ja ne on tarvittaessa mahdollista korvata uusilla toteutuksilla, jos sovelluksen datan talletustapaa päätetään vaihtaa. Luokat onkin eristetty rajapintojen _TodoDao_ ja _UserDao_ taakse ja sovelluslogiikka ei käytä luokkia suoraan.

Sovelluslogiikan testauksessa hyödynnetäänkin tätä siten, että testeissä käytetään tiedostoon tallentavien DAO-olioiden sijaan keskusmuistiin tallentavia toteutuksia.

### Tiedostot

Sovellus tallettaa käyttäjien ja todojen tiedot erillisiin tiedostoihin.

Sovelluksen juureen sijoitettu [konfiguraatiotiedosto](https://github.com/mluukkai/OtmTodoApp/blob/master/dokumentaatio/kayttoohje.md#konfiguraatiotiedosto) [config.properties](https://github.com/mluukkai/OtmTodoApp/blob/master/config.properties) määrittelee tiedostojen nimet.

Sovellus tallettaa käyttäjät seuraavassa formaatissa

<pre>
mluukkai;Matti Luukkainen
hellas;Arto Hellas
</pre>

eli ensin käyttäjätunnus ja puolipisteellä erotettuna käyttäjän nimi.

Käyttäjien työt tallettavan tiedoston formaatti on seuraava

<pre>
1;Tiskaa;true;mluukkai
2;Valmistele OhPen luento;false;hellas
3;Imuroi ja käy kaupassa;false;mluukkai
</pre>

Kentät on eroteltu puolipistein. Ensimmäisenä todon tunniste eli _id_, toisena kuvaus, kolmantena tieto siitä onko tehtävä jo suoritettu ja viimeisenä tehtävän luoneen käyttäjän käyttäjätunnus.

### Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

#### käyttäjän kirjaantuminen

Kun kirjautumisnäkymässä on syötekenttään kirjoitettu käyttäjätunnus ja klikataan painiketta _loginButton_ etenee sovelluksen kontrolli seuraavasti:

<img src="https://raw.githubusercontent.com/mluukkai/OtmTodoApp/master/dokumentaatio/kuvat/a-4b.png" width="750">

Painikkeen painamiseen reagoiva [tapahtumankäsittelijä](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/ui/TodoUi.java#L92) kutsuu sovelluslogiikan _appService_ metodia [login](https://github.com/mluukkai/OtmTodoApp/blob/master/src/main/java/todoapp/domain/TodoService.java#L73) antaen parametriksi kirjautuneen käyttäjätunnuksen. Sovelluslogiikka selvittää _userDao_:n avulla onko käyttäjätunnus olemassa. Jos on, eli kirjautuminen onnistuu, on seurauksena se että käyttöliittymä vaihtaa näkymäksi _todoScenen_, eli sovelluksen varsinaisen päänäkymän ja renderöi näkymään kirjautuneen käyttäjän todot eli tekemättömät työt.

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
