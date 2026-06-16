# Integrated Development Environment (IDE)

## Learning goals
In this module, you will learn:

- What a IDE is, and why it is a good idea to use one
- How to pick an IDE for your preferences
- How to install and work on Python in Visual Studio Code

## What is an IDE?
Code in it's simplest form is just plain text. You could write Python code in any simple text editor, such as notepad, and it will run just fine. 
IDE stands for *Integrated Development Environment*. An IDE is a program that helps you write, run, test, and debug code all in one place. Instead of only giving you a blank text area, an IDE provides extra tools that make programming easier and more efficient. 

## Why use an IDE?
The most important purpose of an IDE is to offer a *complete* workspace for every task you need to perform to program. This goes beyond just writing code, and can include running or compiling the code, debugging, and testing. It also offers a way to organise projects, and files and directories within that project.  Many IDEs also implement Git, which we will learn about during the course, to provide source control in the same window. A feature-rich IDE eliminates the need to switch between different programs or command lines to program. 

### GUI
Most IDEs provide a graphical user interface, or GUI. This means you can interact with your files, folders, and tools using buttons, menus, and panels instead of only typing commands.
This is a useful feature, especially for beginners and intermediate programmers, because it removes some need to learn terminal commands/

### Code completion
One of the biggest upsides of using an IDE is code completion. As you type your code, the IDE will offer suggestions: variables, functions, classes that are already present in your codebase, or the third-party libraries you use in your project. This makes mistakes less common, and can help explore libraries.

### Syntax highlighting
Another common feature is *syntax highlighting*. An IDE (and most simple code editors) will color different parts of your code based on their functionality. For in Python, `if` and `else` get the same color, while integers might have a different color. 
An added upside is the ability to express your exquisite taste by using a color scheme that is tailored to your liking.


## Picking an IDE
Like many topics in programming, the choice of IDE is a highly personal one. It is good to keep in mind that every IDE has its strong points and weak points. Picking a tool can be a daunting task for a beginner in the field, where not all pro's and con's may be apparent. In general, there are a few things to look out for in the selection process:

- Which features are/are not implemented? This is the most important step in the selection.
- How obtainable is the tool? Free is better then expensive, but sometimes paid products have advantages.
- Is the codebase available under an open source license? If you do not know what this means yet: we will talk extensively about open source software in the course!
- How is the community around the tool? This is often a byproduct of user numbers, but some smaller tools may have more beginner-friendly or open communities.

### Some available IDEs for Python

#### PyCharm
[PyCharm][pycharm] is an IDE developed by JetBrains. It is considered one of the most feature-comlpete IDEs for developing Python projects. The *Community Edition* is free to use, and the codebase is available open source. The *Professional Edition* adds some more features, is paid, and has closed source components.

#### Spyder
[Spyder][spyder] is an IDE that is developed by a community of Python developers. It has an extensive graphical interface that is inpsired by MATLAB. It is especially useful for working on scientific projects where visualizations and keeping track of variables is important. It is free to use and the codebase is available under an open source license.

#### Visual Studio Code (our choice)
[Visual Studio Code][vscode] (often abbreviated to VS Code) is an IDE developed by Microsoft. It is [by far the most popular IDE][https://survey.stackoverflow.co/2025/technology/#1-dev-id-es] for developing a wide range of programming languagrs. This has two distinct advantages: there is a strong community around the IDE, and the workflow is adaptable to other languages then Python. If, for example, you decide to get into building interactive web applications, VS Code works just as well for HTML and Javascript as it does for Python. Out of the box, it offers less functionality for pure Python then PyCharm does, but with a few well-supported plugins this gap is easily bridged.

VS Code is not open source, but the engine it is built on is. An alternative that uses the same engine to build an open source version, [VS Codium][vscodium], exists. 

While we encourage you to use the IDE that fits your preferences, the materials in this course are designed around using VS Code. If you already have a lot of experience working in a certain IDE, you can continue to use it. Otherwise, we strongly suggest you use VS Code for the purpose of this course.
The next part of this module will walk you through installing, setting up, and using VS Code for Python development.


[vscode]: https://code.visualstudio.com/
[vscodium]: https://vscodium.com/
[spyder]: https://www.spyder-ide.org/
[pycharm]: https://www.jetbrains.com/pycharm/