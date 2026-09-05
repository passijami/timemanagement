# Määrittelydokumentti
Helsingin yliopiston Aineopintojen harjoitustyö: Algoritmit ja tekoäly.  
Suoritan kurssin syksyllä 2026 Tietojenkäsittelytieteen kandiohjelmassa (TKT).

## Aihe ja toteutus
Harjoitustyössä toteutetaan Pythonilla algoritmikokonaisuus, jonka tavoitteena on löytää mahdollisimman tehokas aikataulu annetuista tehtävistä. Työssä vertaillaan kolmea erilaista lähestymistapaa:  

- täydellinen haku
- ahne algoritmi
- dynaaminen ohjelmointi

Kaikissa menetelmissä lähtökohtana on sama ongelma. Käytettävissä on yhteensä aikaa T, ja n tehtävästä pitäisi valita sopiva osajoukko sekä niiden suoritusjärjestys siten, että valittujen tehtävien kokonaiskesto pysyy käytettävissä olevan ajan rajoissa ja saavutettu kokonaispistemäärä on mahdollisimman suuri.

Jokaisella tehtävällä on nimi, kesto, deadline ja tärkeyteen perustuva pistearvo. Tehtävästä saatava pistemäärä riippuu myös siitä, milloin tehtävä valmistuu. Jos tehtävä valmistuu ajoissa, siitä saa suurimman mahdollisen pistemäärän, kun taas myöhästyminen pienentää saatavaa pistemäärää. Jos tehtävä jätetään kokonaan tekemättä, siitä voidaan lisäksi antaa sakko. Ongelma ei siis ole pelkästään tehtävien järjestäminen, vaan samalla täytyy päättää, mitkä tehtävät kannattaa ylipäätään tehdä. Esimerkiksi pitkä ja paljon aikaa vievä tehtävä voi olla kannattavampaa jättää välistä, jos sen sijaan ehditään tehdä kaksi lyhyempää tehtävää ja saada niistä yhteensä enemmän pisteitä. Rakenteeltaan ongelma muistuttaa yksikoneaikataulutusta sekä repunpakkausongelmaa.

## Projektin kielet
Käytän työssäni Pythonia.  
Vertaisarvioinnissa muiden yleisten kielten arviointi ja seuraaminen onnistuu.  
Sovellus ja dokumentaatio on suomeksi.


## Lähteet
