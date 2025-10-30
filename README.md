
Python Calculator

Video Demo: ??>>>>

Description:

Introduction

Hi, I’m Shiv Shankar Prasad Gupta, and this is my CS50P Project00 . For my project, I built a command-line calculator in Python.

The goal was simple: create a calculator that does the basics really well, but also shows good programming practices like modular design, error handling, and automated testing with pytest.

I decided to make this project because almost everyone uses a calculator daily, and I wanted to design one that’s easy to use, reliable, and extendable.

⸻

Features

✔️ Interactive menu-based interface for choosing operations
✔️ Supports addition, subtraction, multiplication, and division
✔️ Input validation to prevent crashes when entering invalid numbers
✔️ Handles division by zero with clear error messages
✔️ Tested with pytest to ensure correctness of functions

⸻

Project Structure

Here’s how my project is organized:
	•	project.py
The main Python file. Contains:
	•	main() → Entry point that runs the program.
	•	add(x, y), subtract(x, y), multiply(x, y), divide(x, y) → Core arithmetic functions.
	•	Input loop for users to perform calculations interactively.
	•	test_project.py
Includes automated tests for each arithmetic function using pytest. Ensures everything works correctly and prevents regressions if the code changes.
	•	requirements.txt
Lists dependencies. For this project, it just contains pytest.
	•	README.md
This file. It explains what the project is, how it’s structured, and how to run it.

⸻

Installation and Usage

1. Clone the Project

If using GitHub:
git clone https://github.com/<shivgupta69>/cs50-calculator.git
cd cs50-calculator

Or just download the folder if you’re working in CS50 Codespace.

2. Install Requirements

Make sure you have Python 3 installed, then run:

pip install -r requirements.txt

3. Run the Calculator

python project.py

You’ll see a menu like this:

Welcome to CS50 Calculator!
Choose an operation:
1. Add
2. Subtract
3. Multiply
4. Divide

Just enter your choice, input numbers, and get results instantly.

4. Run Tests

pytest test_project.py

This runs unit tests for each arithmetic function.

⸻

Design Choices
	•	I kept each operation as a separate function so the code is modular and easy to extend.
	•	Errors like invalid input and division by zero are handled gracefully so the program never crashes.
	•	The calculator runs in a loop until the user decides to quit.
	•	I used pytest instead of just manual testing to ensure correctness.

This design makes the project simple, but also a great base for adding more advanced features later.

⸻

Future Improvements

🔹 Add scientific functions (square root, exponentiation, logarithms)
🔹 Add a memory function to store and recall results
🔹 Build a GUI version with Tkinter or PyQt
🔹 Allow multiple operations in one line (e.g., 2 + 3 * 4)

⸻

Conclusion

This project is simple, but it reflects what I’ve learned in CS50P:
	•	Writing clean, modular Python code
	•	Handling errors gracefully
	•	Using tests to build reliable software

I’m proud of how it turned out, and I’d love to keep improving it in the future.

Thanks for checking out my project! 🚀

⸻

