from examples.example_1 import (
    return_eight,
)


class TestReturnEight:
    """Tests for the return_eight function."""

    def test_method(self):
        """Test method behaviour."""
        actual = return_eight()

        expected = 8

        assert actual == expected
