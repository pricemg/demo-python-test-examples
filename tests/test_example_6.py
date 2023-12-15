import pytest

from tests.conftest import (
    Case,
    parametrize_cases,
)

from examples.example_6 import (
    break_string_pattern,
    count_characters_in_strings,
)


@pytest.fixture
def list_of_string_that_had_no_underscores() -> list[str]:
    """The result of applying `'abcd'.split('_')."""
    return ['abcd']


@pytest.fixture
def list_of_string_that_had_one_underscore() -> list[str]:
    """The result of applying `'ab_cd'.split('_')."""
    return ['ab', 'cd']


@pytest.fixture
def list_of_string_that_had_three_underscores() -> list[str]:
    """The result of applying `'a_b_c_d'.split('_')."""
    return ['a' ,'b', 'c', 'd']


class TestBreakStringPattern:
    """Tests for the break_string_pattern function."""

    @parametrize_cases(
        Case(
            label='abcd',
            input_string='abcd',
            expected='list_of_string_that_had_no_underscores',
        ),
        Case(
            label='ab_cd',
            input_string='ab_cd',
            expected='list_of_string_that_had_one_underscore',
        ),
        Case(
            label='a_b_c_d',
            input_string='a_b_c_d',
            expected='list_of_string_that_had_three_underscores',
        ),
    )
    def test_expected_using_builtin_requests(
        self,
        input_string,
        expected,
        request,  # This is a built in pytest fixture.
    ):
        """Test using the built in pytest request fixture to access fixture data within the test.

        Here we need to:
        * specify the fixtures to use as a string that matches their name
        * pass `request` in as a fixture
        * wrap the fixture string in `request.getfixturevalue
        """
        actual = break_string_pattern(input_string)

        assert actual == request.getfixturevalue(expected)

    @parametrize_cases(
        Case(
            label='abcd',
            input_string='abcd',
            expected=pytest.lazy_fixture('list_of_string_that_had_no_underscores'),
        ),
        Case(
            label='ab_cd',
            input_string='ab_cd',
            expected=pytest.lazy_fixture('list_of_string_that_had_one_underscore'),
        ),
        Case(
            label='a_b_c_d',
            input_string='a_b_c_d',
            expected=pytest.lazy_fixture('list_of_string_that_had_three_underscores'),
        ),
    )
    def test_expected_using_lazy_fixture(self, input_string, expected):
        """Test using the built in pytest lazy_fixture add in to access fixture data within the test.

        Here we simply wrap the fixture string within the `pytest.lazy_fixture`
        method in our parameterisation setup.
        """

        actual = break_string_pattern(input_string)

        assert actual == expected


class TestCountCharactersInStrings:
    """Tests for the count_characters_in_strings function."""

    @parametrize_cases(
        Case(
            label='abcd',
            input_values='list_of_string_that_had_no_underscores',
            expected={'abcd': 4}
        ),
        Case(
            label='ab_cd',
            input_values='list_of_string_that_had_one_underscore',
            expected={'ab': 2, 'cd': 2}
        ),
        Case(
            label='a_b_c_d',
            input_values='list_of_string_that_had_three_underscores',
            expected={'a': 1, 'b': 1, 'c': 1, 'd': 1}
        ),
    )
    def test_expected_using_builtin_requests(
        self,
        input_values,
        expected,
        request,  # This is a built in pytest fixture.
    ):
        """Test using the built in pytest request fixture to access fixture data within the test.

        Here we need to:
        * specify the fixtures to use as a string that matches their name
        * pass `request` in as a fixture
        * wrap the fixture string in `request.getfixturevalue
        """
        actual = count_characters_in_strings(
            request.getfixturevalue(input_values)
        )

        assert actual == expected

    @parametrize_cases(
        Case(
            label='abcd',
            input_values=pytest.lazy_fixture('list_of_string_that_had_no_underscores'),
            expected={'abcd': 4}
        ),
        Case(
            label='ab_cd',
            input_values=pytest.lazy_fixture('list_of_string_that_had_one_underscore'),
            expected={'ab': 2, 'cd': 2}
        ),
        Case(
            label='a_b_c_d',
            input_values=pytest.lazy_fixture('list_of_string_that_had_three_underscores'),
            expected={'a': 1, 'b': 1, 'c': 1, 'd': 1}
        ),
    )
    def test_expected_using_lazy_fixture(self, input_values, expected):
        """Test using the built in pytest lazy_fixture add in to access fixture data within the test.

        Here we simply wrap the fixture string within the `pytest.lazy_fixture`
        method in our parameterisation setup.
        """

        actual = count_characters_in_strings(input_values)

        assert actual == expected
