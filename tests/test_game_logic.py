from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# Added tests: verify the documented bugs have been fixed.
# check_guess now returns a tuple (outcome, message), so these unpack it.
# ---------------------------------------------------------------------------
from app import get_range_for_difficulty, parse_guess, update_score


def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_wrong_guess_never_adds_score():
    start = 100
    for attempt in range(1, 9):
        assert update_score(start, "Too High", attempt) <= start
        assert update_score(start, "Too Low", attempt) <= start


def test_too_high_penalty_is_consistent():
    # Penalty must not depend on whether the attempt number is even/odd.
    assert update_score(100, "Too High", 2) == update_score(100, "Too High", 3)


def test_winning_increases_score():
    assert update_score(0, "Win", 1) > 0


def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err is not None


def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err is not None
