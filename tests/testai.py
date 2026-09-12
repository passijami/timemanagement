"""Testit tekoälylle.

Periaate: tekoäly löytää varman voiton, kun sellainen on
olemassa käytetyllä syvyydellä.
"""

import pytest


def test_ai_finds_winning_move():
    """TODO: pelitilanne jossa yksi siirto voittaa suoraan."""
    pytest.skip("TODO")


def test_ai_finds_forced_win_in_n_moves():
    """TODO: käytä connect4.gamesolver.org rakentamaan tilanne jossa
    varma voitto on esim. 4 siirron päässä täydellisellä pelillä ja
    tarkista että tekoäly löytää sen riittävällä hakusyvyydellä."""
    pytest.skip("TODO")


def test_ai_never_returns_illegal_move():
    """TODO: choose_move palauttaa aina jonkin board.legal_moves()
    joukon sarakkeen."""
    pytest.skip("TODO")


def test_ai_blocks_opponents_immediate_win():
    """TODO: vastustaja uhkaa voittaa seuraavalla siirrolla, mikä  
       tekoälyn täytyy estää."""
    pytest.skip("TODO")


def test_move_ordering_reduces_node_count():
    """Minimax + alfa-beta löytää saman vastauksen
    riippumatta siirtojen järjestyksestä, vain nopeus muuttuu.

    TODO: lisää minimax-funktioon laskuri joka kasvaa joka kutsulla.
    Aja sama epäsymmetrinen keskipelin tilanne keskeltä-ulos-
    järjestyksellä ja käänteisessä järjestyksessä samalla
    syvyydellä. Tarkista että solmumäärä on selvästi
    pienempi keskeltä-ulos-järjestyksellä."""
    pytest.skip("TODO")
