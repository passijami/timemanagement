# Viikkoraportti 2

Tällä viikolla tapahtui käänne aiheen kanssa. Juttelin ohjaajan kanssa alkuperäisestä aiheesta, jonka laajuus osoittautui kurssin vaatimustason alapuolelle. Sovimme, että valitsen uuden aiheen ja päädyin valitsemaan valmiista aiheista pelin Connect4, jolle on tarkoitus luoda tekoäly. Kirjoitin uuden määrittelydokumentin ja pystytin projektille kunnollisen rungon.

Ohjelman puolella en ole vielä päässyt varsinaiseen algoritmin toteutukseen. Toistaiseksi board.py ja ai.py ovat runkoja, joissa metodit on nimetty ja dokumentoitu mutta ei toteutettu. Sama koskee testejä. Kirjoitin testitapaukset valmiiksi nimettyinä ja kommentoituina. Seuraava konkreettinen tavoite on saada board.py ja ensimmäinen versio minimaxista toimimaan.

Opin tällä viikolla paljon minimaxista ja alfa-beta-karsinnasta. Ymmärrän, miksi siirtojen järjestäminen ja rajaukset vaikuttaa paljon karsinnan tehokkuuteen. Opin myös, miksi iteratiivisessa syvenemisessä hajautustauluun saa tallettaa vain parhaaksi arvioidun siirron, ei sen arvoa. Alfa-beta-karsinnan takia moni laskettu arvo on vain ylä- tai alaraja, ei tarkka luku, joten niiden käyttäminen sellaisenaan syvemmällä haulla johtaisi vääriin päätöksiin. Tehokkaan voitontarkistuksen idea eli tarkistetaan vain viimeisimmän siirron kautta kulkevat suunnat, oli myös hyvä esimerkki siitä, miten pelin säännöistä johtuva invariantti voi säästää paljon laskenta-aikaa.

Rakenne ja suunnittelu ovat kunnossa, mutta konkreettinen koodi, sekä tuotantokoodi että testit, on vielä kirjoittamatta. Ensi viikolla lähden viemään näitä eteen päin.

Tuntimäärällisesti käytin tällä viikolla projektiin noin 13 tuntia.
