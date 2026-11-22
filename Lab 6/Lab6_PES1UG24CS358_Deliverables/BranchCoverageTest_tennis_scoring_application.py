import pytest
from tennis_scoring import game_score, set_winner, match_status

# Comprehensive Test cases for 100% Branch Coverage and 100% Line Coverage

# --- game_score branch tests ---

def test_game_negative_points_a():
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)

def test_game_negative_points_b():
    with pytest.raises(ValueError, match="negative points"):
        game_score(0, -1)

def test_game_deuce():
    assert game_score(3, 3) == "deuce"
    assert game_score(4, 4) == "deuce"

def test_game_win_from_deuce_player_a():
    assert game_score(5, 3) == "game A"

def test_game_win_from_deuce_player_b():
    assert game_score(3, 5) == "game B"

def test_game_advantage_player_a():
    assert game_score(4, 3) == "advantage A"

def test_game_advantage_player_b():
    assert game_score(3, 4) == "advantage B"

def test_game_win_normal_player_a():
    assert game_score(4, 0) == "game A"
    assert game_score(4, 2) == "game A"

def test_game_win_normal_player_b():
    assert game_score(0, 4) == "game B"
    assert game_score(2, 4) == "game B"

def test_game_in_progress():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 2) == "15-30"
    assert game_score(2, 1) == "30-15"
    assert game_score(3, 2) == "40-30"


# --- set_winner branch tests ---

def test_set_winner_regular_a():
    assert set_winner(6, 0) == "A"
    assert set_winner(6, 4) == "A"

def test_set_winner_regular_b():
    assert set_winner(0, 6) == "B"
    assert set_winner(4, 6) == "B"

def test_set_winner_tiebreak_a():
    assert set_winner(7, 6) == "A"

def test_set_winner_tiebreak_b():
    assert set_winner(6, 7) == "B"

def test_set_undecided():
    assert set_winner(3, 2) is None
    assert set_winner(5, 5) is None
    assert set_winner(6, 5) is None
    assert set_winner(5, 6) is None


# --- match_status branch tests ---

def test_match_winner_a():
    assert match_status(2, 0, 3) == "A wins"

def test_match_winner_b():
    assert match_status(0, 2, 3) == "B wins"

def test_match_decider():
    assert match_status(1, 1, 3) == "decider"

def test_match_in_progress():
    assert match_status(0, 0, 3) == "in progress"
    assert match_status(1, 0, 3) == "in progress"
    assert match_status(0, 1, 3) == "in progress"
