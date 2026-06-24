# More documentation
## In-code documentation
In-code documentation makes code more understandable and explains decisions we made. When not to use in-code documentation:

 - When the code is self-explanatory
 - To replace good variable/function names
 - To replace version control
 - To keep old (zombie) code around by commenting it out

### Readable code vs commented code
```python
# convert from degrees celsius to fahrenheit
def convert(d):
    return d * 5 / 9 + 32
```
vs
```python
def celsius_to_fahrenheit(degrees):
    return degrees * 5 / 9 + 32
```

/// details | good comments   
    type: tip

Consider these two comments:

**Comment A**
```python
# we regard temperatures below -50 degrees as measurement errors
  if temperature < -50:
      print("ERROR: temperature is too low")
```
**Comment B**
```python 
# now we check if temperature is below -50
  if temperature < -50:
      print("ERROR: temperature is too low")
```
Which of these comments is more useful? Can you explain why?

///

## What are “docstrings” and how can they be useful?
Here is the function `fahrenheit_to_celsius` which converts temperature in Fahrenheit to Celsius.

The first set of examples uses regular comments:
```python
# This function converts a temperature in Fahrenheit to Celsius.
def fahrenheit_to_celsius(temp_f: float) -> float:
    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c
```

The second set uses docstrings or sim
```python
def fahrenheit_to_celsius(temp_f: float) -> float:
    """
    Converts a temperature in Fahrenheit to Celsius.

    Parameters
    ----------
    temp_f : float
        The temperature in Fahrenheit.

    Returns
    -------
    float
        The temperature in Celsius.
    """

    temp_c = (temp_f - 32.0) * (5.0/9.0)
    return temp_c
```

Docstrings can do a bit more than just comments:

 - Tools can generate help text automatically from the docstrings.

 - Tools can generate documentation pages automatically from code.

It is common to write docstrings for functions, classes, and modules. Good docstrings describe:

 - What the function does.
 - What goes in (including the type of the input variables).
 - What goes out (including the return type).

**Naming is documentation**: giving explicit, descriptive names to your code segments (functions, classes, variables) already provides very useful and important documentation. In practice you will find that for simple functions it is unnecessary to add a docstring when the function name and variable names already give enough information.
