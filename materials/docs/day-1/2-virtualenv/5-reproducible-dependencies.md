# Reproducible Dependencies

## Objectives

 - Why dependency management matters
 - What a requirements file is
 - How to create a requirements file
 - How to install dependencies from a requirements file
 - How to recreate an environment

## Requirements Files
Imagine: a colleague attempts to rerun a text-analysis pipeline six months after publication. Several packages have changed since the original work was completed. Without a record of the required dependencies, reproducing the original environment becomes difficult.

The virtual environment itself is not committed to Git. Instead, we commit information describing how to recreate that environment using the `requirements.txt` file. This file lists the Python packages required by a project, and can be used as a shortcut to install all the required packages in one go by running `pip install -r requirements.txt`

A simple requirements file might contain:

```
requests
pandas
matplotlib
```

But for optimal reusability, package versions need to be specified:
```
requests==2.32.0
pandas==2.2.3
matplotlib==3.10.1
```

/// details | Version pinning
    type: tip

You will learn the simplest way to create a requirements.txt file in this module, but as you make your way to even larger-scale projects, you will probably end up switching to a more elaborate way of keeping track of your package versions, such as [`piptools`](https://pypi.org/project/pip-tools/).
///

## How to read version numbers
You may have noticed that many (almost all) packages and libraries follow a similar pattern for version numbers. This is no coincidence, but a convention known as [Semantic Versioning](https://semver.org/). The idea is that, without knowing the exact changes, you can tell how a new version might influence your software.

/// define
Semantic Versioning

A software versioning convention that uses a three-part number: `MAJOR.MINOR.PATCH` to easily identify differences between versions of software.

- `MAJOR` versions introduce breaking changes to the software. Updating to a new major version will often introduce necessary changes to your code. Going from `pandas==2.2.3` to `pandas==3.1.0` may break your code.
- `MINOR` versions add new features, but should still be compatible within a major version. Updating `requests==2.2.3` to `requests==2.3.0` should pose no problems, but might offer some new features that you can use.
- `PATCH` versions fix bugs in a backward compatible way. It should always be safe, and advisable, to update to a new patch. Going from `matplotlib==3.10.1` to `matplotlib==3.10.2` should be no problem, and will probably fix a bug or security issue you may not even be aware of.

///

## Exercise: create a requirements file
Once packages have been installed into a virtual environment, pip can automatically generate a requirements file.

 - Activate the virtual environment.
 - Install a library (or several) using `pip install`
 - Run `pip freeze > requirements.txt`
 - Inspect the file. Do you see your library in it? What else do you see?
 - Commit the requirements file.

 /// details | Advanced: constraining versions
Using `pip freeze` constrains all package versions to an *exact* version. This is a good way to ensure all packages work together. However, there are cases where you want to be more or less specific about which versions to use. Following the semantic version convention, you may want to specify only the major version of a package. There are several ways to constrain package versions. Below are the most common ones:

```pip-requirements
# minimum version, will match any major, minor, or patch above 2.28
requests>=2.28

# compatible version, will match all patches of 2.0, but not go to 2.1
pandas~=2.0

# comma separated constraints must all match
# this will match all versions between 3.0 and 4.0
# this is a good way to ensure staying within major version
matplotlib>=3.0,<4.0
```

 ///

## Installing from a Requirements File
A requirements file can be used to recreate an environment on another machine. The `-r` flag tells pip to read package names from a file. We will do that now on one machine, but imagine that you are an exploring researcher stumbling on this new repository that they want to install locally.

## Exercise: recreate an environment

 - Deactivate and delete `.env`
 - Create a new environment and activate it.
 - Check which packages have already been installed using `pip list`
 - Run `pip install -r requirements.txt`
 - Verify that the required packages have been installed using `pip list`

## Updating Dependencies
Projects evolve over time. New dependencies are added and existing dependencies may change. Whenever dependencies change, the requirements file should be updated as well.


## Exercise: update requirements.txt

 - Run `pip install tqdm`
 - Run `pip freeze > requirements.txt`
 - Inspect changes using `git diff requirements.txt`
 - Commit the file.


## Next steps
This is the most reproducible, most commonly used way of managing your python dependencies. However, it is somewhat cumbersome, and many developers have created ways to help manage dependencies. While not the focus of this course, it might be worth checking out two other dependency manager systems for later:

1. [Pip-tools](https://pypi.org/project/pip-tools/): A library that helps you automatically update your requirements as your codebase develops. This is the current standard that we use in the Research Software Lab.
2. [uv]: A library that aims to combine the functionality of `pip`, `venv`, `pip-tools` in a single manager. A lot of python developers are using `uv` these days, as it is very fast and has a good user experience.


## Works cited:
https://packaging.python.org/
https://pip.pypa.io/en/stable/
