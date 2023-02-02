import pytest

from week5.address import extract_city, extract_state, extract_zipcode


def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("padre cerqueira 550, Resistencia Chaco, ID H3500 ") == "Resistencia Chaco"
    assert extract_city("Jujuy 1200, Resistencia, ID H3500")


def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("550 Padre Cerqueira, Resistencia, H 3500") == "H"


def test_extract_zipcode():
    assert extract_zipcode("550 Padre Cerqueira, Resistencia, H 3500") == "3500"
    assert extract_zipcode("550 Padre Cerqueira, Resistencia, H") == "3500"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
