from unittest import mock

import pytest

from examples.example_5 import(
    complex_calculation,
)


class TestComplexCalculation:
    """Tests for the complex_calculation function."""

    # @pytest.mark.skip(reason='test takes too long so we mock')
    def test_method_no_mock(self):
        """Test method using all the called functions.
        
        As these are expensive operations we should look to mock them.
        """
        a = 2
        b = 3
        actual = complex_calculation(a, b)

        expected = 13

        assert actual == expected

    @mock.patch('examples.example_5.slow_add')
    @mock.patch('examples.example_5.slow_multiply')
    def test_method_mock_1(
        self,
        mock_slow_multiply,
        mock_slow_add,
    ):
        """Test function using the builtin unittest mock module.
        
        To use `mock` we much decorate the function with each mock patch, and
        then define these as input arguments for this function. Note that the
        order of `mock.patch` is reversed for the input arguments.

        In this example we define the values for each mock within the test
        function.
        """
        a = 2
        b = 3

        mock_slow_add.side_effect = [6, 14]
        mock_slow_multiply.return_value = 12

        actual = complex_calculation(a, b)

        expected = 13

        assert actual == expected

    @mock.patch('examples.example_5.slow_add', side_effect=[6, 14])
    @mock.patch('examples.example_5.slow_multiply', return_value=12)
    def test_method_mock_2(
        self,
        mock_slow_multiply,
        mock_slow_add,
    ):
        """Test function using the builtin unittest mock module.
        
        To use `mock` we much decorate the function with each mock patch, and
        then define these as input arguments for this function. Note that the
        order of `mock.patch` is reversed for the input arguments.

        In this example we define the values for each mock within the decorator
        definition for each mock. Note we still need to define each mock as
        an input argument despite not being used within this test function
        directly.
        """
        a = 2
        b = 3

        actual = complex_calculation(a, b)

        expected = 13

        assert actual == expected

    def test_method_pytest_mock(self, mocker):
        """Test function using the pytest-mock plugin.
        
        pytest-mock is a wrapper around the built in unittest mock module.
        The differene is we now do not need to decorate this test function with
        each mock patch. Instead these are defined within.
        """
        a = 2
        b = 3

        mocker.patch('examples.example_5.slow_add', side_effect=[6, 14])
        mocker.patch('examples.example_5.slow_multiply', return_value=12)

        actual = complex_calculation(a, b)

        expected = 13

        assert actual == expected
