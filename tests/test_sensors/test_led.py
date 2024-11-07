import pytest
from src.sensors.led import FixedLED

@pytest.fixture
def init_led():
    return FixedLED(None, 0, 0)

@pytest.mark.parametrize("led, red, green, blue, expected", [
    ("init_led", 0, 0, 0, 0),
    ("init_led", 1, 0, 0, 1),
    ("init_led", 5, 2, 0, 5),
    ("init_led", 2, 6, 0, 2)
])
def test_set_colour_red(led, red, green, blue, expected, request):
    led = request.getfixturevalue(led)
    led.set_colour(red, green, blue)
    assert led.red_value == expected

@pytest.mark.parametrize("led, red, green, blue, expected", [
    ("init_led", 0, 0, 0, 0),
    ("init_led", 0, 1, 0, 1),
    ("init_led", 2, 5, 0, 5),
    ("init_led", 0, 2, 6, 2)
])
def test_set_colour_green(led, red, green, blue, expected, request):
    led = request.getfixturevalue(led)
    led.set_colour(red, green, blue)
    assert led.green_value == expected

@pytest.mark.parametrize("led, red, green, blue, expected", [
    ("init_led", 0, 0, 0, 0),
    ("init_led", 0, 0, 1, 1),
    ("init_led", 0, 2, 5, 5),
    ("init_led", 5, 0, 2, 2)
])
def test_set_colour_blue(led, red, green, blue, expected, request):
    led = request.getfixturevalue(led)
    led.set_colour(red, green, blue)
    assert led.blue_value == expected
    
def test_turn_off(init_led):
    init_led.turn_off
    assert (init_led.red_value == 0 and init_led.blue_value == 0 and init_led.green_value == 0)

def test_get_color(init_led):
    init_led.set_colour(0, 0, 0)
    # print(init_led.red_value)
    assert init_led.get_colour() == (0, 0, 0)
