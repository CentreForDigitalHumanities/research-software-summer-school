## What are command line arguments?
When running a program from a command line interface (CLI), that program may accept a number of *arguments* as input. For example, we learned the behaviour of the `ls` program without and with additional arguments:

- `ls` displays the contents of the current directory
- `ls /path/to/directory` displays the content of `/path/to/directory`
- `ls -l` displays the content of the current directory in long format
- `ls` accepts many more arguments. Use `man ls` to get an overview, or look it up in the [documentation](https://man7.org/linux/man-pages/man1/ls.1.html).

Python programs are no exception to this, and will actually take an arbitrary number of CLI arguments. It is up to the program to do something with those arguments.

By using arguments, a program can respond to different inputs, making it much more flexibile. You can compare CLI arguments to function parameters: instead of just performing a task in a singular way, different inputs can shape the process or result of the function. Let's take a very simple Python script that adds two numbers together:

```python
a = 2
b = 3
result = a + b
print('The result is: {}'.format(result))
```

And execute it:

```
python add.py
```

If we want to add two different numbers, we would need to change the script. This is not very flexible. Ideally, we would provide the numbers that we want to add:

```
python add.py 4 5
```

Python accepts this as input, but does not act on it. Without changing the script, the output will still be `The result is: 5`. 

## Using CLI arguments in Python
Arguments can be accessed in Python by using the [`sys` module](https://docs.python.org/3/library/sys.html). This module is part of the [Python Standard Library](https://docs.python.org/3/library/index.html), which means it is available in all Python installations. The relevant variable is `sys.argv` [(documentation)](https://docs.python.org/3/library/sys.html#sys.argv). *argv* stands for *arguments vector*, and contains a list of the program name and any additional arguments.

### Exercise 1
- Write a Python script that adds two numbers together, and outputs the result
    - The numbers should be provided as CLI arguments
    - Use `sys.argv` to access the arguments
    - What should happen when 1 number is provided? And 3 numbers? You decide, and implement a solution