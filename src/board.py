"""Connect4-pelilaudan logiikka: siirrot, voitontarkistus, tilan hallinta.

Lauta on 6 riviä x 7 saraketta. Sallittujen siirtojen generointi,
voitontarkistus ja siirron suoritus toteutetaan itse.
"""

ROWS = 6
COLS = 7


class Board:
    """Connect4-lauta.

    TODO: valitaan sisäinen esitys. Yksinkertaisin on 2D-lista (rivi x
    sarake). Yksinkertainen, optimoi myöhemmin.
    """

    def __init__(self):
        """Alusta tyhjä lauta ja vuorossa oleva pelaaja. TODO."""
        raise NotImplementedError

    def legal_moves(self) -> list[int]:
        """Palauttaa sarakkeet, joihin voi pudottaa merkin.

        TODO.
        """
        raise NotImplementedError

    def play(self, column: int) -> None:
        """Pudottaa vuorossa olevan pelaajan merkin sarakkeeseen.

        TODO: päivitä myös tieto viimeisimmästä siirrosta (rivi, sarake),
        tarvitaan tehokkaaseen voitontarkistukseen.
        """
        raise NotImplementedError

    def undo(self, column: int) -> None:
        """Peruuttaa viimeisimmän siirron sarakkeessa.

        TODO: tämä mahdollistaa minimaxin vetäytymisen ilman koko
        laudan kopiointia joka rekursiotasolla.
        """
        raise NotImplementedError

    def check_win(self) -> bool:
        """Onko viimeisin siirto muodostanut nelirivin?

        TODO: tarkista VAIN ne suunnat,
        jotka kulkevat viimeisimmän siirron ruudun kautta, ei koko
        laudan läpikäyntiä (ks. Määrittelydokumentti).
        """
        raise NotImplementedError

    def is_full(self) -> bool:
        """Onko peli päättynyt tasapeliin (lauta täynnä)? TODO."""
        raise NotImplementedError
