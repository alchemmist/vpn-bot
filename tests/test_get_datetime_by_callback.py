import pytest

from vpn_bot.handlers.monthly_analytics import get_datetime_by_callback
from vpn_bot import exceptions


def test_empty_callback():
    with pytest.raises(exceptions.CallbackUndefined) as error:
        get_datetime_by_callback("")
    assert "Collback is empty in get_datetime_by_callback" == error.value.args[0]


def test_callback_is_None():
    with pytest.raises(exceptions.CallbackUndefined) as error:
        get_datetime_by_callback("None")
    assert "Collback is None in get_datetime_by_callback" == error.value.args[0]


def test_callback_incorrect_format():
    with pytest.raises(exceptions.CallbackIncorrectFormat) as error:
        get_datetime_by_callback("sometest")
    assert "Can't parse collback in get_datetime_by_callback. Callback: 'sometest'" == error.value.args[0]

    with pytest.raises(exceptions.CallbackIncorrectFormat) as error:
        get_datetime_by_callback("some_test_2024.01_test")
    assert "Can't parse collback in get_datetime_by_callback. Callback: 'some_test_2024.01_test'" == error.value.args[0]

    with pytest.raises(exceptions.CallbackIncorrectFormat) as error:
        get_datetime_by_callback("sometest_13.2024.test")
    assert "Can't parse collback in get_datetime_by_callback. Callback: 'sometest_13.2024.test'" == error.value.args[0]


def test_callback_incorrect_value():
    with pytest.raises(ValueError):
        get_datetime_by_callback("sometest_2024.01")

    with pytest.raises(ValueError):
        get_datetime_by_callback("sometest_13.2001")

    with pytest.raises(ValueError):
        get_datetime_by_callback("sometest_-8.0001")
