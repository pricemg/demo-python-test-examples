from unittest import mock

import pytest

from conftest import Case, parametrize_cases

from examples.example_7 import(
    complex_calculation_1,
    complex_calculation_2,
)


class TestComplexCalculation1:
    """Tests for the complex_calculation_1 function."""

    @pytest.mark.skip(reason='test takes too long so we mock')
    def test_method_no_mock(self):
        """Test method using all the called functions.
        
        As these are expensive operations we should look to mock them.
        """
        a = 2
        b = 3
        actual = complex_calculation_1(a, b)

        expected = 13

        assert actual == expected

    @mock.patch('examples.example_7.slow_add')
    @mock.patch('examples.example_7.slow_multiply')
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

        actual = complex_calculation_1(a, b)

        expected = 13

        assert actual == expected

    @mock.patch('examples.example_7.slow_add', side_effect=[6, 14])
    @mock.patch('examples.example_7.slow_multiply', return_value=12)
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

        actual = complex_calculation_1(a, b)

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

        mocker.patch('examples.example_7.slow_add', side_effect=[6, 14])
        mocker.patch('examples.example_7.slow_multiply', return_value=12)

        actual = complex_calculation_1(a, b)

        expected = 13

        assert actual == expected


class TestComplexCalculation2:
    """Tests for the complex_calculation_2 function.
    
    These tests are more complex in that they use parameterised test cases and
    pytest fixtures on top of the mocking usage. These showcase how ordering
    or decorators and the function arguments differ between the use of the
    python unittest mock, and pytest-mock wrapper."""

    @pytest.fixture
    def c_value(self) -> int:
        """Fixture to provide value for `c` parameter."""
        return 1

    @pytest.mark.skip(reason='test takes too long so we mock')
    def test_method_no_mock(self, c_value):
        """Test method using all the called functions.
        
        As these are expensive operations we should look to mock them.
        """
        a = 1
        b = 1
        c = c_value
        actual = complex_calculation_2(a, b, c)

        expected = 1

        assert actual == expected


    @parametrize_cases(
        Case(
            label='small_values',
            a=1,
            b=1,
            slow_multiply_mock_value=1,
            slow_add_mock_value=2,
            expected=1,
        ),
        Case(
            label='small_values',
            a=10,
            b=20,
            slow_multiply_mock_value=200,
            slow_add_mock_value=210,
            expected=209,
        ),
    )
    @mock.patch('examples.example_7.slow_add')
    @mock.patch('examples.example_7.slow_multiply')
    def test_method_mock_1(
        self,
        mock_slow_multiply,
        mock_slow_add,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
        c_value,
    ):
        """Test function using the builtin unittest mock module.
        
        To use `mock` we much decorate the function with each mock patch, and
        then define these as input arguments for this function. Note that the
        order of `mock.patch` is reversed for the input arguments.

        In this example we define the values for each mock within the test
        function.
        
        Decorators ordered:
        1. parametrize cases
        2. Mock patches

        Arguments ordered:
        1. mock patches
        2. parametrize case values
        3. c_value fixture
        """
        mock_slow_multiply.return_value = slow_multiply_mock_value
        mock_slow_add.return_value = slow_add_mock_value

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    # To avoid bloat, define the cases from previous test to variables for use
    # in the subsequent tests. 
    case_1 = Case(
        label='small_values',
        a=1,
        b=1,
        slow_multiply_mock_value=1,
        slow_add_mock_value=2,
        expected=1,
    )
    case_2 = Case(
        label='small_values',
        a=10,
        b=20,
        slow_multiply_mock_value=200,
        slow_add_mock_value=210,
        expected=209,
    )

    @mock.patch('examples.example_7.slow_add')
    @mock.patch('examples.example_7.slow_multiply')
    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_mock_2(
        self,
        mock_slow_multiply,
        mock_slow_add,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
        c_value,
    ):
        """Test function using the builtin unittest mock module.
        
        Decorators ordered:
        1. Mock patches
        2. parametrize cases

        Arguments ordered:
        1. mock patches
        2. parametrize case values
        3. c_value fixture

        Even though the ordering of decorators has now changed, the mock
        patches must still be defined first in reverse order.
        """
        mock_slow_multiply.return_value = slow_multiply_mock_value
        mock_slow_add.return_value = slow_add_mock_value

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    # This example is so broken, using pytest skip mark doesn't prevent the
    # tests from erroring.
    #
    # @pytest.mark.skip(reason='test method argument order not valid.')
    # @mock.patch('examples.example_7.slow_add')
    # @mock.patch('examples.example_7.slow_multiply')
    # @parametrize_cases(
    #     case_1,
    #     case_2,
    # )
    # def test_method_mock_3(
    #     self,
    #     a,
    #     b,
    #     c_value,
    #     slow_multiply_mock_value,
    #     slow_add_mock_value,
    #     expected,
    #     mock_slow_add,
    #     mock_slow_multiply,
    # ):
    #     """Test function using the builtin unittest mock module.
    #
    #     Decorators ordered:
    #     1. Mock patches
    #     2. parametrize cases
    #
    #     Arguments ordered:
    #     1. parametrize case values
    #     2. mock patches
    #     3. c_value fixture
    #     """
    #     mock_slow_multiply.return_value = slow_multiply_mock_value
    #     mock_slow_add.return_value = slow_add_mock_value
    #
    #     c = c_value
    #
    #     actual = complex_calculation_2(a, b, c)
    #
    #     assert actual == expected

    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_1(
        self,
        mocker,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
        c_value,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. mocker
        2. parametrize case values
        3. c_value fixture
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected


    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_2(
        self,
        c_value,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
        mocker,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. c_value fixture
        2. parametrize case values
        3. mocker
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_3(
        self,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
        c_value,
        mocker,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. parametrize case values
        2. c_value fixture
        3. mocker
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_4(
        self,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
        mocker,
        c_value,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. parametrize case values
        2. mocker
        3. c_value fixture
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_5(
        self,
        c_value,
        mocker,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. c_value fixture
        2. mocker
        3. parametrize case values
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_6(
        self,
        mocker,
        c_value,
        a,
        b,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. mocker
        2. c_value fixture
        3. parametrize case values
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected

    @parametrize_cases(
        case_1,
        case_2,
    )
    def test_method_pytest_mock_7(
        self,
        mocker,
        a,
        b,
        c_value,
        slow_multiply_mock_value,
        slow_add_mock_value,
        expected,
    ):
        """Test function using the pytest-mock plugin.
        
        Arguments ordered:
        1. mocker
        2. some parametrize case values
        3. c_value fixture
        4. more parametrize case values

        Not sure how this one even works!
        """
        mocker.patch('examples.example_7.slow_add', return_value=slow_add_mock_value)
        mocker.patch('examples.example_7.slow_multiply', return_value=slow_multiply_mock_value)

        c = c_value

        actual = complex_calculation_2(a, b, c)

        assert actual == expected