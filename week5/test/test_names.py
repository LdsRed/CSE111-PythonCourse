import names
import pytest

from week5.names import make_full_name, extract_family_name, extract_given_name


def test_make_full():
    assert make_full_name("jordan", "larcher") == "larcher; jordan"
    assert make_full_name("Miss", "Fortune") == "Fortune; Miss"
    assert make_full_name("", "") == ";"


def test_extract_family_name():
    assert extract_family_name("Larcher; Erick") == "Larcher"
    assert extract_family_name("Fantini; Sarah") == "Fantini"
    assert extract_family_name("; Erick") == ";"


def test_extract_given_name():
    assert extract_given_name("Larcher; Jordan") == "Jordan"
    assert extract_given_name("Cristoforo; Ricardo") == "Ricardo"



# Stretch Challenges


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
