# Python Environments

## Objectives

 - What Python packages and dependencies are
 - Why virtual environments are useful
 - How to create a virtual environment
 - How to activate and deactivate a virtual environment
 - How to use `.gitignore` to exclude generated files
 - How to install packages into an environment

## Packages and Dependencies
One of Python's strengths is its large ecosystem of libraries, which you can download as packages using the Python Package Index (PyPI). These packages provide additional functionality that can be installed and used in your own software.

/// define
Package

- a collection of Python code that can be installed and reused in other projects.
///

Most research software projects depend on external packages. For example, a text-analysis tool may depend on `nltk`, while a data processing pipeline may depend on `pandas`.

/// define
Dependency

- a package that your software requires in order to run correctly.
///


## Virtual Environments
As projects grow, managing dependencies becomes increasingly important. Moreover, as you work on different projects, you find that your new projects require different versions of packages used in your other projects, which can lead to conflicts if you install all your packages into your global python version. Python provides virtual environments to solve this problem. Each project can have its own virtual environment, allowing it to use exactly the packages and versions that it requires without interference from other python versions. After you are done with the environment (when finishing or archiving your project for example), you can just delete the folder that contains the environment and you are done!


/// define
Virtual environment

- an isolated Python installation that contains its own packages and configuration, independent of other Python projects on the same machine.
///

## Exercise: create a virtual environment

 - Step 1: Navigate to your `sandbox_NAME` repository.
 - Step 2: Run `python -m venv .env`
 - Step 3: Verify that `.env` has been created in the working directory.
 - Step 4: Activate your virtual environment by running `source .env/bin/activate` (on Linux/MacOS) or `.env/bin/activate` (on Windows)
 - Step 5: Verify that your virtual environment works by checking if `(.env)` has appeared in front of your terminal cursor. 
 - Step 6: Run `python` and print 'hello world'.
 - Step 6: Deactivate the virtual environment by running `deactivate`.
 - Step 6: Delete the `.env` folder in your working directory.

## Git and Virtual Environments
When Git examines your repository, it will also see the files inside your virtual environment and show them in your staging area as having been added to your working directory. However, virtual environments should generally not be committed to version control. Not only are they specific to your machine, they can always be recreated later and often contain thousands of generated files.

The solution for this is the `.gitignore` file, which tells Git which files and directories should not be tracked.


## Exercise: ignore a virtual environment

 - Step 1: Re-create your virtual environment.
 - Step 2: Run `git status` and look at the Source Control menu: do you see the .env directory with all its files in the staging area?
 - Step 3: Create a `.gitignore` file.
 - Step 4: Add `.env/` to the file and save it.
 - Step 5: Run `git status` and look at the Source Control menu again: what do you notice?
 - Step 6: Commit `.gitignore`.

## Works cited:
https://docs.python.org/3/library/venv.html
