import pytest

from examples.example_2 import (
    raise_runtime_error,
    raise_value_error,
)


class TestRaiseRuntimeError:
    """Tests for the raise_runtime_error function."""

    def test_method(self):
        """Test method behaviour."""
        with pytest.raises(RuntimeError):
            raise_runtime_error()


class TestRaiseValueError:
    """Tests for the raise_value_error2 function."""

    def test_raises_error_for_zero(self):
        """Test method raises a ValueError when value is 0."""
        with pytest.raises(ValueError, match="We got a zero here!"):
            raise_value_error(0)

    def test_raises_error_for_non_zero(self):
        """Test method raises a differnet ValueError when value is not 0."""
        value = 1
        with pytest.raises(ValueError, match=f'Stopping the code {value=}.'):
            raise_value_error(value)
