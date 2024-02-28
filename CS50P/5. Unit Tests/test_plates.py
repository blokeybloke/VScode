from plates import is_valid

def main():
    test_min_and_max()
    test_start_with_2_letters()
    test_numbers_middle()
    test_CS()
    test_punctuation()

def test_min_and_max():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False

def test_start_with_2_letters():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False

def test_numbers_middle():
    assert is_valid("AAA111") == True
    assert is_valid("AA11AA") == False

def test_CS():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False

if __name__ == "__main--":
    main()