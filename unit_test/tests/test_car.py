import pytest
from unittest.mock import patch
from car import Car

def test_car():
    car = Car()

    assert car.doors_open == False
    assert car.engine_running == False
    assert car.is_moving == False
    
def test_car_start():
    car = Car()
    car.start()
    assert car.engine_running == True

def test_car_start_raises_exception():
    car = Car()
    car.engine_running = True
    with pytest.raises(RuntimeError) as excinfo:
        car.start()
        assert str(excinfo.value) == "Engine is running already"


def test_car_horn():
    car = Car()
    car.horn()


def test_car_accelerate():
    car = Car()
    car.start()
    with patch('move.accelerate') as mock_accelerate:
        car.accelerate(5.5)
        mock_accelerate.assert_called_once()
        assert car.is_moving == True

