Overview
This is a simple calculator application that supports basic arithmetic operations like addition, subtraction, multiplication, and division. The app can be run from the command line with user inputs, and it includes features like:

Handling user input with exception handling
Random test data generation using the Faker library
Test data generation with pytest to create N test records
Error management for invalid input and division by zero
Features
Basic arithmetic operations:
Addition
Subtraction
Multiplication
Division (with error handling for division by zero)
Faker integration: Generate fake data for testing the calculator with random numbers and operations.
Command-line usage: Run the calculator from the terminal with input arguments for two numbers and the operation.
Test coverage: The project includes tests for various operations and edge cases, using pytest for test automation and pylint for code quality checks.
Error handling: Handles invalid input gracefully and provides appropriate error messages.
Requirements
To run this application, you will need to set up a Python environment and install the required libraries.

Dependencies

Python 3.6+
Faker - For generating random test data
pytest - For running tests
pylint - For code linting and style checks
