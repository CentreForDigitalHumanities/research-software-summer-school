# Linting



## Callenge: Improve Your Code (Format & Lint)

Install and use a formatter and a linter to improve the style of your code.

### Python

[The program `ruff`](https://github.com/astral-sh/ruff) can both format _and_ lint Python code. [Install `ruff`](https://docs.astral.sh/ruff/installation/) from PyPI or conda. Don’t forget to add it to your `requirements.txt`, `pyproject.toml` or whichever file you use to define your dependencies.

#### Formatting

First, use the formatter. Note that the use without the `--check` flag ruff automatically changes your file. This is the default, because formatting does not change the behaviour of your code.

```bash
# Check for formatting
ruff format --check

# Fix formatting, if desired
ruff format
```

Do you agree with the default choices `ruff` made? You can [configure `ruff`](https://docs.astral.sh/ruff/tutorial/#configuration) to follow your choices if you need to, but be aware that the defaults were chosen for a reason.

#### Linting

Next, try out the linter. While fixing formatting is usually harmless, linting fixes change your code on a deeper level. By default, `ruff` only advises you. To automatically apply the linting, you need an explicit `--fix` flag. This is because linting can touch the functionality of your code, so make sure to review the changes ruff makes.

```bash
# Check for linting
ruff check

# Fix linting, if desired
ruff check --fix
```

What is your opinion on the linting suggestions? Again, you can [configure](https://docs.astral.sh/ruff/tutorial/#configuration) the details `ruff` pays attention to when linting. Did you learn something new about the Python language?

/// details | OpenAI Closing in   
    type: warning

Astral, the company that is behind *ruff*, was acquired by OpenAI in March 2026. This has lead some developers to speculate that ruff and other free products by Astral will become unavailable or degraded. This has not yet happened, but know that there are several python linters out there, and you can always find another one if you want to.
///


## (Optional) Challenge: Git Pre-Commit Hooks
Follow the exercise https://carpentries-incubator.github.io/reproducible-research-through-reusable-code-in-1-day/good-code.html#optional-git-pre-commit-hooks

## (Optional) Challenge: Modularity in Python

Carefully review the following code snippet:

```python
def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                fahrenheit = (celsius * (9 / 5)) + 32
                if fahrenheit < -459.67:
                    # Invalid temperature, below absolute zero
                    return "Invalid temperature"
                else:
                    return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return celsius, fahrenheit
    else:
        return "Invalid unit"
```

Refactor the code by extracting functions without altering its functionality.

- What functions did you create?
- What strategies did you use to identify them?


#### Example project

Example project (if you don't have your own project): https://github.com/popylar-org/prfmodel

### Challenge: Combining Functions

Let’s define two functions that will convert temperature from Fahrenheit to Kelvin, and Kelvin to Celsius:

```R
fahr_to_kelvin <- function(temp) {
  kelvin <- ((temp - 32) * (5 / 9)) + 273.15
  return(kelvin)
}

kelvin_to_celsius <- function(temp) {
  celsius <- temp - 273.15
  return(celsius)
}
```

Define the function to convert directly from Fahrenheit to Celsius, by reusing the two functions above (or using your own functions if you prefer).

## (Optional) Git pre-commit hooks
So far, formatting and linting were conscious choices: you have to remember to execute them yourself every once in a while. A more robust approach would be to take away this mental load and automate linting and formatting. This can be achieved through “git hooks”, which are a set of scripts git can run every time a certain action is performed. Here we have a look at “pre-commit hooks” that check your code changes before you commit them.

### Challenge: use a git pre-commit hook
The amount of git pre-commit hook scripts can grow rather large on bigger projects. pre-commit manages your commit hooks and helper programs in a declarative way and makes them easy to share between collaborators.

Use a git pre-commit hook to run formatters and linters every time before a git commit.

 - Install [pre-commit](https://pre-commit.com/) and add it to your `requirements.txt`. 
 - Create a `pre-commit` config file named .`pre-commit-config.yaml`.

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.14.8
  hooks:
    # Run the linter.
    - id: ruff-check
      # Possible choices: [ python, pyi, jupyter ]
      # Here we exclude Jupyter notebooks
      types_or: [ python, pyi ]

      # Comment _out_ to only check, not fix
      args: [ --fix ]

    # Run the formatter.
    - id: ruff-format

      # Comment _in_ to only check, not fix
      # args: [ --check ]

      # Possible choices: [ python, pyi, jupyter ]
      # Here we exclude Jupyter notebooks
      types_or: [ python, pyi ]
```

 - If you would want to run additional checks, you need to add a new `- repo:` entry to the `pre-commit` config file.
 - Make sure to add and commit this file to your git repository, so your collaborators will use the exact same configurations and versions.
 - Install the new git hook by running `pre-commit install` in the terminal.
 - You can test your script by executing it manually: `pre-commit run --all-files`
 - For updating your hooks to the latest version, run: `pre-commit autoupdate`


## Authorship
This material was created by Eduard Klapwijk and Ole Mussman and is also disclosed via [the Carpentries](https://carpentries-incubator.github.io/reproducible-research-through-reusable-code-in-1-day/aio.html). The memes are added by ME.