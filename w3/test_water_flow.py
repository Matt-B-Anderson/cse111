from pytest import approx
import pytest
import water_flow

def test_water_column_height():
    assert water_flow.water_column_height(0.0, 0.0) == approx(0.0)
    assert water_flow.water_column_height(0.0, 10.0) == approx(7.5)
    assert water_flow.water_column_height(25.0, 0.0) == approx(25.0)
    assert water_flow.water_column_height(48.3, 12.8) == approx(57.9)


def test_pressure_gain_from_water_height():
    assert water_flow.pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert water_flow.pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert water_flow.pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert water_flow.pressure_loss_from_pipe(0.048692, 0.0, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200.0, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200.0, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200.0, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200.0, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.286870, 1000.0, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])