"""Tekoäly: minimax (alfa-beta-karsinta) + iteratiivinen syveneminen.
"""

from connect4.board import Board


def choose_move(board: Board, time_limit_seconds: float) -> int:
    """Valitsee parhaan sarakkeen annetulla aikarajalla.

    TODO:
        1. Iteratiivinen syveneminen, aja minimax syvyydellä 1, 2, 3...
           kunnes time_limit_seconds täyttyy. Pidä aina tallessa viimeksi
           KOKONAAN valmistuneen syvyyden paras siirto, ei keskeytynyttä syvyyttä.
        2. Käytä jokaisen syvyyden alussa edellisen syvyyden hajautustaulua siirtojen  
           järjestämiseen. Kokeile ensin edellisellä kierroksella parhaaksi havaittua siirtoa.
        3. Uusi tyhjä hajautustaulu joka kerta kun ihminen on tehnyt
           oman siirtonsa ja tekoäly alkaa laskea omaansa.
    """
    raise NotImplementedError


def minimax(
    board: Board,
    depth: int,
    alpha: float,
    beta: float,
    maximizing: bool,
    move_order_hint: dict,
) -> tuple[float, int]:
    """Minimax alfa-beta-karsinnalla, yksi kiinteä syvyys.

    Args:
        board: nykyinen pelitilanne, play/undo
        depth: jäljellä oleva hakusyvyys
        alpha, beta: karsintarajat
        maximizing: onko vuorossa pelaaja jota maksimoidaan
        move_order_hint: edellisen iteraation hajautustaulu siirtojen
            järjestämiseen.

    Returns:
        (arvo, paras_sarake).

    TODO:
        - Kokeile siirrot keskisarakkeesta reunoja kohti, ellei
          move_order_hint tarjoo parempaa ehdotusta ensimmäiseksi
          kokeiltavaksi.
        - Tarkista board.check_win() jokaisen play()-kutsun jälkeen, ja
          board.is_full() tasapelin varalta.
        - depth == 0 ja peli ei päättynyt -> palauta evaluate(board).
        - Muista board.undo() aina rekursiivisen kutsun jälkeen.
    """
    raise NotImplementedError


def evaluate(board: Board) -> float:
    """Heuristinen arvio kesken jääneen pelitilanteen hyvyydestä.

    TODO: suunnittele oma funktio  
    Esimerkki lähtökohdaksi: laske kummankin pelaajan
    mahdolliset neljän suorat "ikkunat" ja
    pisteytä niiden täyttöasteen mukaan.
    """
    raise NotImplementedError
