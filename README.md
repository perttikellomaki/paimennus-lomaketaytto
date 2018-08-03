# paimennus-lomaketaytto
Kennelliiton paimennuslomakkeiden puoliautomaattinen täyttö

Prosessi:

1. Luo kokeen yhteisillä tiedoilla täytetyt koirakohtaisen lomakkeen
   mallit hakemistoon 'pohjat'. Näihin voit täyttää myös kokeen pisteytyksen.
   Nimeä lomakkeet PAIM-E.pdf, PAIM-1.pdf, PAIM-2.pdf ja PAIM-3.pdf

2. Tee koirakohtaiset tiedot sisältävä tiedosto koirat.csv, jonka
   ensimmäisellä rivillä on seuraavat otsikot:

    * Ohjaaja
    * Omistaja
    * Omistajan kotikunta
    * Virallinen nimi
    * Kutsumanimi
    * Luokka
    * Rotu
    * Rotukoodi
    * Rekisterinumero
    * TM-numero
    * Sukupuoli

   Koirien tiedot sitten seuraavilla riveillä. Luokat niiden virallisilla
   nimillä 'PAIM-E' jne.

3. Aja komento ./koirakohtaiset.py joka luo esitäytetyt koirakohtaiset
   lomakkeet hakemistoon esitaytetyt.
