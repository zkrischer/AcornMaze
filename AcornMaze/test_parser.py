from game_parser import parse


def test_parse():
    # Bad Letter
    try:
        parse(["**X**","**C**","**Y**"])
    except ValueError as a:
        assert str(a) == "Bad letter in configuration file: C."
    
    # More than one X
    try:
        parse(["**X**","****X","**Y**"])
    except ValueError as a:
        assert str(a) == "Expected 1 starting position, got 2."
    
    # No X
    try:
        parse(["*****","*****","**Y**"])
    except ValueError as a:
        assert str(a) == "Expected 1 starting position, got 0."

    # More than one Y
    try:
        parse(["**X**","****Y","**Y**"])
    except ValueError as a:
        assert str(a) == "Expected 1 ending position, got 2."

    # No Y
    try:
        parse(["**X**","*****","*****"])
    except ValueError as a:
        assert str(a) == "Expected 1 ending position, got 0."

    # Corner Case - No X or Y
    try:
        parse(["*****","*****","*****"])
    except ValueError as a:
        assert str(a) == "Expected 1 starting position, got 0."
    
    # Teleport Pad does not have a match.
    try:
        parse(["**X**","*1***","***2*","**Y**"])
    except ValueError as a:
        assert str(a) == "Teleport pad 1 does not have an exclusively matching pad."
    
    # Teleport Pad Number has 4 pads!
    try:
        parse(["**X**","*1*1*","*1*1*","**Y**"])
    except ValueError as a:
        assert str(a) == "Teleport pad 1 does not have an exclusively matching pad."
        


def run_tests():
    test_parse()

run_tests()