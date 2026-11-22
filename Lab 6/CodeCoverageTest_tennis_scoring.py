import pytest
from tennis_scoring import game_score, set_winner, match_status

# Test cases designed for Code Coverage (achieving >= 90% line coverage)

def test_game_negative_points():
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 2)

def test_game_deuce():
    assert game_score(3, 3) == "deuce"

def test_game_win_from_deuce():
    assert game_score(5, 3) == "game A"
    assert game_score(3, 5) == "game B"

def test_game_advantage_a():
    assert game_score(4, 3) == "advantage A"

def test_game_win_normal():
    assert game_score(4, 0) == "game A"
    assert game_score(0, 4) == "game B"

def test_game_in_progress():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 2) == "15-30"

def test_set_winner_regular():
    assert set_winner(6, 0) == "A"
    assert set_winner(0, 6) == "B"

def test_set_undecided():
    assert set_winner(3, 2) is None

def test_match_winner():
    assert match_status(2, 0, 3) == "A wins"
    assert match_status(0, 2, 3) == "B wins"

def test_match_decider():
    assert match_status(1, 1, 3) == "decider"

def test_match_in_progress():
    assert match_status(0, 0, 3) == "in progress"
