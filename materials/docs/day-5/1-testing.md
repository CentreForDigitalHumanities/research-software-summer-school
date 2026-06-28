# Testing

Writing test code for your software has multiple benefits. The most obvious one is that it creates a safeguard that helps you maintain a minimum level of quality. A less obvious and perhaps also less intuitive benefit is that it *saves time*, compared to not writing test code. We will see why this is the case below. Other benefits:

- Tests help you think about, and make explicit, what you _expect_ your software to do.
- As a result of the previous point, tests also provide a form of developer-oriented documentation.
- Tests help guide decisions when structuring your code, because some ways to structure your code are easier to test than others. Structures that are easier to test are often also easier to maintain and reuse. More on this below as well.

We generally distinguish two main types of tests:

1. Tests that check whether individual parts of the code base work as intended. Depending on use case and context, we may refer to these most commonly as *unit tests*, but also *behavioral tests*, *module tests* or *white-box tests*, among others. The latter refers to the fact that these tests are written with detailed knowledge about the inner workings of the software; the test author must be able to "see in the box".
2. Tests that check whether the software as a whole, or at least large chunks of it, function as desired. Common names for tests in this category include *functional tests*, *end-to-end tests* and *black-box tests*. The latter refers to the opposite of a *white-box test*: the test is only concerned with the end product and does not require knowledge of its inner workings.

The second type is mostly worthwhile for large projects of which the behavior has somewhat stabilized. The first type, however, is widely applicable, from brand new projects to decades old legacy software and from the smallest script to the largest operating system. Unit tests are a **must-have** for every project. They are true low-hanging fruit, because they test individual functions and are generally easy to write.

/// details | Take it from the ones who ought to now
    type: tip

Really, truly, we know it does not feel efficient to write a test, especially for code that already functions when you use it. However, once you start writing software with several 'moving parts', it will save you **days of work** trying to figure out why your code no longer works.
///


## Introducing unit testing

As an example of a function that we might want to test, let us revisit the following function from [Day 2](../day-2/2-other-documentation.md#readable-code-vs-commented-code):

```python
def celsius_to_fahrenheit(degrees):
    return degrees * 9 / 5 + 32
```

Suppose that the above function is saved in a module named `temperature.py`. A Python programmer who just wrote that function, and who does not yet know about unit testing, might want to check that the function works as intended by opening the Python interpreter in [interactive mode](https://stackoverflow.com/a/2665150) and entering a few statements like the following:

```python
>>> from temperature import celsius_to_fahrenheit
>>> celsius_to_fahrenheit(-40)
-40.0
>>> celsius_to_fahrenheit(5)
41.0
```

/// details | Testing is for everyone
    type: warning

 It may seem over-cautious to verify such a simple function right after writing it. However, an early version of these course materials had the `5` and the `9` reversed, i.e., `5 / 9` instead of `9 / 5`. That mistake could slip through exactly *because the function had not been tested*. A common adagium is that **untested code is broken**, which was true in our case, and we are all supposedly professional coders!
 ///

The above prompts in the interactive Python interpreter are basically an implicit, throwaway unit test. It is implicit because only the author can tell whether the outcome of the test was correct or not. It is throwaway, because the author will have to write these lines again every time they want to test. We will turn this into an explicit and reusable unit test in two steps.

To make the test explicit about the expected outcome, we wrap the function calls in assertions:

```python
>>> from temperature import celsius_to_fahrenheit
>>> assert celsius_to_fahrenheit(-40) == -40.0
>>> assert celsius_to_fahrenheit(5) == 41.0
```

Now, Python is able to distinguish a passing test from a failed test. If the return value of the function is different from the right hand of the equation, an `AssertionError` will be raised.

To make this reusable and somewhat self-documenting, we just have to save the code in a test module. Let's call the module `test_temperature.py`. It looks almost the same as above:

```python
from temperature import celsius_to_fahrenheit


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(-40) == -40.0
    assert celsius_to_fahrenheit(5) == 41.0
```

With [pytest][pytest], actually making this test run is as easy as running `pytest` within in your project's directory:

[pytest]: https://docs.pytest.org/en/stable/index.html

```shell
$ pytest
=========================== test session starts ===========================
platform linux -- Python 3.14.5, pytest-9.0.2, pluggy-1.6.0
collected 1 item                                                          

test_temperature.py .                                               [100%]

============================ 1 passed in 0.01s ============================
```

Pytest takes a no-overhead, no-nonsense approach to unit testing. It understands that modules with a name starting with `test_` (such as `test_temperature.py`) contain tests, that functions with `test_` (such as `test_celsius_to_fahrenheit`) *are* tests, and that a failed assertion means a failed test. By default, it finds all your tests and runs all of them, even if some of them fail along the way. It also gives informative output in case of failure. For example, if we had accidentally written `23` instead of `32`, we would get this output:

```shell
$ pytest
=========================== test session starts ===========================
platform linux -- Python 3.14.5, pytest-9.0.2, pluggy-1.6.0
collected 1 item                                                          

test_temperature.py F                                               [100%]

================================ FAILURES =================================
_______________________ test_celsius_to_fahrenheit ________________________

    def test_celsius_to_fahrenheit():
>       assert celsius_to_fahrenheit(-40) == -40.0
E       assert -49.0 == -40.0
E        +  where -49.0 = celsius_to_fahrenheit(-40)

test_temperature.py:5: AssertionError
========================= short test summary info =========================
FAILED test_temperature.py::test_celsius_to_fahrenheit - assert -49.0 ==...
============================ 1 failed in 0.01s ============================
```

At this point, it should be clear how unit testing saves time and improves code quality and reliability. There may be a slight upfront time cost to installing pytest and saving test functions instead of writing bare assertions directly to the Python interpreter, but this effort is already earned back *the second time you run a test*. The only way to spend even less time on programming is to "YOLO" and ship severely broken code to your users!

## How tests improve code structure

Our `celsius_to_fahrenheit` function would have been more difficult to test if it had directly printed its result instead of returning it, like this:

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f'{celsius} degrees celsius is {fahrenheit} degrees fahrenheit.')
```

To see why this is more difficult, try to imagine writing a test for this version of `celsius_to_fahrenheit` based on what you read in the previous section. The function always returns `None`, so you cannot use an assertion based on its return value to determine whether it made the correct calculation. Instead, you would have to capture the text that is printed as a side effect to `sys.stdout`. This is technically possible (pytest has [a way](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html) to do this), but a lot more involved, and then you still have to figure out how to find the computed value between the other text.

This difficult-to-test version of `celsius_to_fahrenheit` has a property that we often see with difficult-to-test code: it has too many concerns. We make it easier to test by *separating concerns*, a type of making code more modular. The two main concerns in play here are *making a calculation* and *presenting the result of a calculation*. Here is how we might separate them:

```python
# making the calculation (back to the previous version)
def celsius_to_fahrenheit(degrees):
    return degrees * 9 / 5 + 32

# presenting the result
format_c2f = '{} degrees celsius is {} degrees fahrenheit.'.format
```

With this more modular version of the code, instead of running `celsius_to_fahrenheit(5)` to directly get the output `5 degrees celsius is 41.0 degrees fahrenheit.`, we combine the concerns by running `print(format_c2f(5, celsius_to_fahrenheit(5)))`.

We can now easily test `celsius_to_fahrenheit` with comparison assertions as we did before. `format_c2f` is a declarative value so we do not really need to test it, but if we want to do this anyway, it is still easy:

```python
from temperature import format_c2f

def test_format_c2f():
    # note that the numbers need not be correct because format_c2f is
    # only concerned with presenting and not with calculating
    expected = '5 degrees celsius is 41 degrees fahrenheit'
    actual = format_c2f(5, 41)
    assert actual == expected
```

We do not need to test `print` because it is a built-in function.

## Next steps

At this point, you know enough to start writing tests for your own code, but you may want to review pytest's [Get Started][pytest-get-started] as you go. Soon enough, you will encounter something that seems difficult to test. It may very well be the case that you can restructure your code in a way that makes it easier to test while also improving the modularity.

[pytest-get-started]: https://docs.pytest.org/en/stable/getting-started.html

Eventually, you will encounter situations where two or more tests need similar example data or setup code. When you reach that stage, be sure to read up on [fixtures][pytest-how-to-use-fixtures].

[pytest-how-to-use-fixtures]: https://docs.pytest.org/en/stable/how-to/fixtures.html
