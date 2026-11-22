def parse_score(text):
    """
    Parses score string formatted as 'A-B' (e.g. '3-2').
    Returns a tuple of integers (a, b) or None if invalid.
    """
    if not isinstance(text, str):
        return None
    parts = text.split('-')
    if len(parts) != 2:
        return None
    try:
        a = int(parts[0].strip())
        b = int(parts[1].strip())
        if a < 0 or b < 0:
            return None
        return a, b
    except (ValueError, TypeError):
        return None


def game_lead(text):
    """
    Calculates point lead between two game scores (e.g. '40-30').
    Valid point keys are '0', '15', '30', '40'.
    Returns integer point lead or None if invalid.
    """
    if not isinstance(text, str):
        return None
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    parts = text.split('-')
    if len(parts) != 2:
        return None
    first = parts[0].strip()
    second = parts[1].strip()
    if first not in points or second not in points:
        return None
    return points[first] - points[second]


def set_spread(games_csv):
    """
    Calculates the spread (max - min) of games won per set from a CSV string (e.g. '6,4,7').
    Returns integer spread or None if invalid or empty.
    """
    if not isinstance(games_csv, str):
        return None
    parts = games_csv.split(',')
    games = []
    for g in parts:
        item = g.strip()
        if not item:
            return None
        try:
            val = int(item)
            if val < 0:
                return None
            games.append(val)
        except (ValueError, TypeError):
            return None
    if not games:
        return None
    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)


if __name__ == "__main__":
    main()
