from datetime import datetime, timedelta

import pytest

from tests.conftest import (
    Case,
    parametrize_cases,
)

from examples.example_5 import calculate_datetime_delta


class TestCalculateDatetimeDelta:
    """Tests for the calculate_datetime_delta function."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
            (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
        ],
    )
    def test_with_builtin_parametrize_v1(self, a, b, expected):
        """Test function using built in pytest parametrize functionality.
        
        Here we let pytest generate the test IDs.

        Output when running `pytest -v` will look like:
        ```
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_timedistance_v0[a0-b0-expected0]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_timedistance_v0[a1-b1-expected1]
        ```
        """
        actual = calculate_datetime_delta(a, b)
        assert actual == expected

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
            (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
        ],
        ids=["forward", "backward"],
    )
    def test_with_builtin_parametrize_v2(self, a, b, expected):
        """Test function using built in pytest parametrize functionality.
        
        Here we specified ids as a list of strings which were used as the test
        IDs. These are succinct, but can be a pain to maintain.

        Output when running `pytest -v` will look like:
        ```
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_timedistance_v2[forward]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_timedistance_v2[backward]
        ```
        """
        actual = calculate_datetime_delta(a, b)
        assert actual == expected

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            pytest.param(
                datetime(2001, 12, 12),
                datetime(2001, 12, 11),
                timedelta(1),
                id="forward",
            ),
            pytest.param(
                datetime(2001, 12, 11),
                datetime(2001, 12, 12),
                timedelta(-1),
                id="backward",
            ),
            # This case demonstrates how a pytest mark can be implemented for
            # an individual test case.
            pytest.param(
                datetime(2001, 12, 11),
                datetime(2001, 12, 12),
                timedelta(-2),
                id="failed",
                marks=pytest.mark.xfail,
            ),
        ],
    )
    def test_with_builtin_parametrize_v3(self, a, b, expected):
        """Test function using built in pytest parametrize functionality.
        
        Here we used pytest.param to specify the test IDs together with the
        actual data, instead of listing them separately.

        Output when running `pytest -v` will look like
        ```
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_timedistance_v3[forward]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_timedistance_v3[backward]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_with_builtin_parametrize_v3[failed]
        ```

        This is the closest we can get the builtin parametrize function to
        match to our custom version, but is still not entirely clear.
        """
        actual = calculate_datetime_delta(a, b)
        assert actual == expected

    @parametrize_cases(
        Case(
            a=datetime(2001, 12, 12),
            b=datetime(2001, 12, 11),
            expected=timedelta(1),
        ),
        Case(
            a=datetime(2001, 12, 11),
            b=datetime(2001, 12, 12),
            expected=timedelta(-1),
        ),
    )
    def test_with_custom_parametrize_v1(self, a, b, expected):
        """Test function using the custom parametrize_cases functionality.

        Now we specify the names for each parameter for better clarity.
        
        Here we let pytest generate the test IDs.

        Output when running `pytest -v` will look like:
        ```
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_with_custom_parametrize_v1[a0-b0-expected0]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_with_custom_parametrize_v1[a1-b1-expected1]
        ```
        """
        actual = calculate_datetime_delta(a, b)
        assert actual == expected

    @parametrize_cases(
        Case(
            label="forward",
            a=datetime(2001, 12, 12),
            b=datetime(2001, 12, 11),
            expected=timedelta(1),
        ),
        Case(
            label="backward",
            a=datetime(2001, 12, 11),
            b=datetime(2001, 12, 12),
            expected=timedelta(-1),
        ),
        # This case demonstrates how a pytest mark can be implemented for an
        # individual test case.
        Case(
            label="failed",
            marks=pytest.mark.xfail,
            a=datetime(2001, 12, 11),
            b=datetime(2001, 12, 12),
            expected=timedelta(-2),
        ),
    )
    def test_with_custom_parametrize_v2(self, a, b, expected):
        """Test function using the custom parametrize_cases functionality.

        Now we specify the names for each parameter for better clarity.
        
        Here we start each test case with the `label` parameter allowing
        clearer labelling of each testcase.

        Output when running `pytest -v` will look like:
        ```
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_with_custom_parametrize_v2[forward]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_with_custom_parametrize_v2[backward]
        tests/test_example_4.py::TestCalculateDatetimeDelta::test_with_custom_parametrize_v2[failed]
        ```
        """
        actual = calculate_datetime_delta(a, b)
        assert actual == expected