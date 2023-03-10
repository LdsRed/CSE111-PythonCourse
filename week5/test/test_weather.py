from _pytest.python_api import approx

from week5.weather import cels_from_fahr


def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and
        comparing the values it returns to the expected values.
        Notice this test function uses pytest.approx to compare
        floating point numbers.
        """
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(27.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)