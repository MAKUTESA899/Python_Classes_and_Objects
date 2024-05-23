# Python Classes and Objects
- Fill in your solutions in the files in the <a name="exercises">exercises</a> folder

## Table of Contents

1. [Unittest](#unittest)
2. [pytest](#pytest)
3. [pipenv_and_pipenv shell](#pipenv_and_pipenv_shell)
4. [types_of_errors_and_forking_a_repository](#types_of_errors_and_forking_a_repository)
5. [forking_a_repository](#forking-a-repository)
6. [exercises](#exercises)
# Notes 
### Python's `unittest` Framework<a name="unittest"></a>

- **Overview**:
  - `unittest` is a built-in Python module used for creating and running tests.
  - It is modeled after Java's JUnit and has features like test automation, setup code for tests, and a collection of tests into test suites.

- **Basic Components**:
  - **Test Case**: The individual unit of testing. This is created by subclassing `unittest.TestCase`.
  - **Test Suite**: A collection of test cases, test suites, or both.
  - **Test Runner**: A component that orchestrates the execution of tests and provides the outcome.

- **Common Methods**:
  - `setUp()`: Method to set up any state before each test method is run.
  - `tearDown()`: Method to clean up after each test method runs.
  - `assertEqual(a, b)`: Check if `a` equals `b`.
  - `assertTrue(x)`: Check if `x` is True.
  - `assertFalse(x)`: Check if `x` is False.
  - `assertRaises(exception, callable, *args, **kwargs)`: Check if an exception is raised.

- **Example**:
  ```python
  import unittest

  class TestStringMethods(unittest.TestCase):

      def setUp(self):
          self.string = "hello world"

      def test_upper(self):
          self.assertEqual(self.string.upper(), "HELLO WORLD")

      def test_isupper(self):
          self.assertFalse(self.string.isupper())

      def tearDown(self):
          self.string = ""

  if __name__ == '__main__':
      unittest.main()
  ```

### `pytest` <a name="pytest"></a>

- **Overview**:
  - `pytest` is a more advanced testing framework compared to `unittest`.
  - It supports fixtures, parameterized testing, and has a more flexible and extensive plugin system.

- **Key Features**:
  - **Fixtures**: A way to set up context or state that tests need.
  - **Parameterization**: Allows running a test with different sets of data.
  - **Assertions**: Uses plain `assert` statements for test conditions.
  - **Plugins**: Extend functionality, such as pytest-cov for coverage, pytest-xdist for parallel testing.

- **Example**:
  ```python
  import pytest

  @pytest.fixture
  def sample_string():
      return "hello world"

  def test_upper(sample_string):
      assert sample_string.upper() == "HELLO WORLD"

  def test_isupper(sample_string):
      assert not sample_string.isupper()
  ```

### `pipenv` and `pipenv shell` <a name="pipenv_and_pipenv_shell"></a>

- **Overview**:
  - `pipenv` is a tool that combines `pip` and `virtualenv` to provide a comprehensive package management solution.
  - It simplifies dependency management and ensures that the right versions of packages are used.

- **Installation**:
  - Install `pipenv` using pip:
    ```sh
    pip install pipenv
    ```

- **Creating a Pipenv Environment**:
  1. Navigate to your project directory.
  2. Run `pipenv install` to create a `Pipfile` and `Pipfile.lock`:
     ```sh
     pipenv install <package_name>
     ```

- **Activating the Environment**:
  - Use `pipenv shell` to activate the virtual environment:
    ```sh
    pipenv shell
    ```

- **Benefits**:
  - **Dependency Management**: Tracks dependencies and their versions in `Pipfile`.
  - **Isolation**: Creates a virtual environment specific to the project, preventing dependency conflicts.
  - **Reproducibility**: `Pipfile.lock` ensures that installations are consistent across different environments.

### Types of Errors in Python

- **Syntax Errors**: Errors caused by incorrect syntax. They are detected by the parser.
  - Example: Missing a colon `:`, improper indentation.

- **Runtime Errors**: Errors that occur during program execution. They are not detected until the program runs.
  - Example: Division by zero, accessing an undefined variable.

- **Logical Errors**: Errors that cause incorrect behavior but do not throw exceptions. They are the hardest to detect as the code runs without errors.
  - Example: Incorrect implementation of an algorithm.

- **Exceptions**: Events that can be handled using try-except blocks.
  - Common exceptions: `ValueError`, `TypeError`, `IndexError`.

### Setting Up a Simple Pipenv Environment

1. **Install `pipenv`**:
   ```sh
   pip install pipenv
   ```

2. **Create a Project Directory**:
   ```sh
   mkdir my_project
   cd my_project
   ```

3. **Initialize a Pipenv Environment**:
   ```sh
   pipenv install <package_name>
   ```

4. **Activate the Virtual Environment**:
   ```sh
   pipenv shell
   ```

5. **Deactivate the Environment**:
   - Simply type `exit` to exit the shell.

### Forking a Repository<a name="forking-a-repository"></a>

- **Forking**:
  - Forking is creating a personal copy of someone else's repository on GitHub.
  - Allows you to freely experiment with changes without affecting the original project.

- **Steps to Fork a Repository**:
  1. Navigate to the repository on GitHub.
  2. Click the "Fork" button at the top right of the repository page.
  3. Choose your GitHub account to create the fork.

- **Cloning the Forked Repository**:
  - Clone the forked repository to your local machine:
    ```sh
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

- **Benefits of Forking**:
  - **Experimentation**: Safely make changes without affecting the original project.
  - **Contribution**: Propose changes to the original repository via pull requests.
  - **Personalization**: Customize and use the project for your own purposes.

By understanding these tools and processes, you can create robust Python projects, manage dependencies effectively, and contribute to open-source projects confidently.


## Exercise1: Creating a `Person` Class<a name="exercises"><a>
### Task
1. Create a class `Person` with the following attributes
    - `name` (string)
    - `age` (integer)

2. Include a method `greet` that returns a string greeting the person by name 
eg. Hello my name is `Bob`

## Exercise2: Implementing a `BankAccount` Class
### Task
1. Create a class `BankAccount` with the following attributes
    - `account_number` (String)
    -  `balance` (Float, starting at 0.0)
2. Include methods to  `deposit` and `withdraw` amounts from the account
3. Ensure that the balance cannot go negative.

## Exercise 3: Building a `Book` Class
### Task:
1. Create a class Book with the following attributes:
    - `title` (string)
    - `author` (string)
    - `pages` (integer)
2. Include a method description that returns a string describing the book.
    eg. `The River Between` by `Ngugi wa Thiongo` `200` pages
3. Add a class variable total_books to keep track of the number of books created.