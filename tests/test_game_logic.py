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

def test_hint_direction_for_high_guess():
    # Targets the high/low bug: a guess above the secret must tell the
    # player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_direction_for_low_guess():
    # Targets the high/low bug: a guess below the secret must tell the
    # player to go HIGHER, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_below_range():
    # Targets the out-of-range bug: a guess less than 1 must be flagged
    # as out of range, not compared to the secret.
    outcome, message = check_guess(0, 50)
    assert outcome == "Out of Range"

def test_guess_above_range():
    # Targets the out-of-range bug: a guess greater than 100 must be
    # flagged as out of range, not compared to the secret.
    outcome, message = check_guess(150, 50)
    assert outcome == "Out of Range"
