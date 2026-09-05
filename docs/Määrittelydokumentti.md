# Määrittelydokumentti
Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly.  
Suoritan kurssin syksyllä 2026 Tietojenkäsittelytieteen kandiohjelmassa (TKT).

## Aihe ja toteutus
Harjoitustyössä toteutetaan Pythonilla algoritmikokonaisuus, jonka tavoitteena on löytää mahdollisimman tehokas aikataulu annetuista tehtävistä. Työssä vertaillaan kolmea erilaista lähestymistapaa:  

- täydellinen haku
- ahne algoritmi
- dynaaminen ohjelmointi

Kaikissa menetelmissä lähtökohtana on sama ongelma. Käytettävissä on yhteensä aikaa T, ja n tehtävästä pitäisi valita sopiva osajoukko sekä niiden suoritusjärjestys siten, että valittujen tehtävien kokonaiskesto pysyy käytettävissä olevan ajan rajoissa ja saavutettu kokonaispistemäärä on mahdollisimman suuri. Suurin osa kehitysajasta käytetään näiden kolmen algoritmin toteuttamiseen, oikeellisuuden testaamiseen ja keskinäiseen vertailuun.

Jokaisella tehtävällä on nimi, kesto, deadline ja tärkeyteen perustuva pistearvo. Tehtävästä saatava pistemäärä riippuu myös siitä, milloin tehtävä valmistuu. Jos tehtävä valmistuu ajoissa, siitä saa suurimman mahdollisen pistemäärän, kun taas myöhästyminen pienentää saatavaa pistemäärää. Jos tehtävä jätetään kokonaan tekemättä, siitä voidaan lisäksi antaa sakko. Ongelma ei siis ole pelkästään tehtävien järjestäminen, vaan samalla täytyy päättää, mitkä tehtävät kannattaa ylipäätään tehdä. Esimerkiksi pitkä ja paljon aikaa vievä tehtävä voi olla kannattavampaa jättää välistä, jos sen sijaan ehditään tehdä kaksi lyhyempää tehtävää ja saada niistä yhteensä enemmän pisteitä. Rakenteeltaan ongelma muistuttaa yksikoneaikataulutusta sekä repunpakkausongelmaa.

| Algoritmi | Aika | Tila | Tehtävä | Idea |
|---|---|---|---|---|
| Täydellinen haku | O(n!) | O(n) | Käy läpi tehtävien osajoukkojen mahdolliset järjestykset ja valitsee parhaan pistemäärän tuottavan. | Käytössä pienillä syötteillä. | 
| Ahne algoritmi | O(n log n) | O(n) | Järjestää tehtävät pistemäärä/kesto-suhteen tai deadlinen mukaan ja lisää niitä aikatauluun niin kauan kuin ne mahtuvat jäljellä olevaan aikaan. | Toteutus priority queue:n avulla, jotta löydetään paras seuraava tehtävä. |
| Dynaaminen ohjelmointi | O(n·T) | O(n·T), optimoitavissa O(T):hen | Taulukossa on n·T solua ja jokainen solu lasketaan vakioajassa edellisten solujen perusteella. | Aikavaativuus noudattaa repunpakkausongelmaa. |

## Projektin kielet
Käytän työssäni Pythonia.  
Vertaisarvioinnissa muiden yleisten kielten arviointi ja seuraaminen onnistuu.  
Sovellus ja dokumentaatio on suomeksi.


## Lähteet
[Dynaaminen ohjelmointi (Wikipedia)](https://en.wikipedia.org/wiki/Dynamic_programming)  
[Ahne algoritmi (Wikipedia)](https://en.wikipedia.org/wiki/Greedy_algorithm)  
[Täydellinen haku (Wikipedia)](https://en.wikipedia.org/wiki/Brute-force_search)
