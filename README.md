# demo-python-test-examples
A collection of examples for testing python code using pytest.

## How to structure the test suite

```
demo-python-testing-examples/
├── examples/
│   ├── example_1.py
│   ├── ...
│   ├── example_N.py
│   └── further_examples/
│       ├── example_Nplus1.py
│       └── ...
├── tests/
│   ├── conftest.py
│   ├── test_example_1.py
│   ├── ...
│   ├── test_example_N.py
│   └── further_examples/
│       ├── test_example_Nplus1.py
│       └── ...
├── pyproject.toml
└── ...
```

Consider in the file  `example/further_examples/example_Nplus1.py` there is a function named `complex_function_15`. All the tests concerning this function will be found in the file named `tests/further_examples/test_example_Nplus1.py` in a class named `TestComplexFunction15`.

By structuring your code and tests in this manner it is trivial for anyone looking at the code to be able to locate all the tests for any part of the code with ease.

### 1. Simple testing of a function
[code](https://github.com/pricemg/demo-python-testing-examples/blob/main/examples/example_1.py)
[tests](https://github.com/pricemg/demo-python-testing-examples/blob/main/tests/test_example_1.py)

A basic example which demonstrates how a test suite for a function should be structured.

### 2. Simple testing of an expected error
[code](https://github.com/pricemg/demo-python-testing-examples/blob/main/examples/example_2.py)
[tests](https://github.com/pricemg/demo-python-testing-examples/blob/main/tests/test_example_2.py)

This example demonstrates how to test a function which has a known raise statement within it.
The example contains 2 functions:
1. `raise_runtime_error` simply raises a `RuntimeError` and the corresponding tests ensure that this is the raised exception
2. `raise_value_error` can raise two different `ValueError`s depending on the value passed to the function. 
   To ensure that the wrong excepction isn't being raised for each case, the tests make use of the `match` parameter in the `pytest.raises` context manager
   This ensures that not only the specified excpetion is raised, but also with the matching message.

(See also the pytest documentation on [expected exceptions](https://docs.pytest.org/en/7.2.x/how-to/assert.html#assertions-about-expected-exceptions))

### 3. Using `marks` - TO DO

### 4. Using `pytest.fixture` to reuse data across tests - TO DO

### 5. Builtin `parameterize` v custom `parametrize_cases` to test multiple scenarios

This example shows how a single function can be tested with more than one set
of inputs in a succinct DRY manner. The test code demonstrates using
1. the built in pytest `parametrize` functionality
2. the use of custom `parametrize_cases` and `Case` code which is kept in `conftest.py`

The benefit of using option 2 is that it provides more readable test cases
compared to the built in functionality.

[code](https://github.com/pricemg/demo-python-testing-examples/blob/main/examples/example_5.py)
[tests](https://github.com/pricemg/demo-python-testing-examples/blob/main/tests/test_example_5.py)

### 6. Combining fixtures and parameterised tests using `pytest-lazy-fixture`

### 7. Usage of `mock` v `pytest-mock` for mocking function calls
[code](https://github.com/pricemg/demo-python-testing-examples/blob/main/examples/example_7.py)
[tests](https://github.com/pricemg/demo-python-testing-examples/blob/main/tests/test_example_7.py)

### 8. Mocking a single function call within a function - TODO

### 9. Mocking multiple calls to same function within a function - TODO

### To add
* Positive and negative 
* skipped test
* xfail test
* passing xfail test
* test coverage
* pytest output