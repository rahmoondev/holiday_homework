python exercises

​1. Fahrenheit to Celsius Converter
​Goal: Write a function that takes a temperature in Fahrenheit as input and returns the temperature in Celsius.
​Formula: C = (F - 32) \times \frac{5}{9}

​2. Simple Calculator
​Goal: Create a script that takes two numbers and an operator (like +, -, *, /) from the user and performs the calculation.
​Concepts: if/elif/else statements, input handling.

​3. List Duplicates Remover
​Goal: Write a function that takes a list of numbers or strings and returns a new list with all duplicate items removed.
​Concepts: Lists, loops, or using the set() data structure.

​4. Factorial Calculator
​Goal: Write a program to calculate the factorial of a user-provided number (e.g., 5! = 5 \times 4 \times 3 \times 2 \times 1).
​Concepts: Loops (for or while), basic arithmetic.

​5. Christmas Countdown Timer
​Goal: Write a script that calculates and prints how many days, hours, and minutes are left until a specific date (e.g., New Year's Day or next Christmas).
​Concepts: Using the datetime module.
​🔐 Text and String Manipulation (Relevant to Encoding/Decoding)
​These problems focus on manipulating text, a key skill in cryptography and log analysis.

​6. Word Counter
​Goal: Write a script that takes a sentence from the user and counts how many times each word appears.
​Concepts: Strings, splitting strings, dictionaries (to store word counts).

​7. Reverse String Checker
​Goal: Write a function that checks if a string is a palindrome (reads the same forwards and backward, like "madam").
​Concepts: String indexing/slicing, conditional checks.

​8. Simple Vowel/Consonant Counter
​Goal: Write a program that takes a string and reports the total number of vowels and consonants found.
​Concepts: Loops, string checking (in keyword).
​📂 File Handling and Data Processing
​File handling is crucial for reading configuration files, processing logs, and handling data dumps.

​9. Log File Analyzer (Dummy Data)
​Goal: Create a simple text file (log.txt) with several lines, some containing the word "ERROR" and some "INFO". Write a script to read the file and count how many "ERROR" lines there are.
​Concepts: File I/O (open(), read(), readlines()), string searching.

​10. CSV Data Reader
​Goal: Create a simple CSV file with three columns (Name, Age, Role). Write a script to read the CSV file and print the name of everyone whose "Role" is "Admin".
​Concepts: Using the built-in csv module (or basic string splitting).
​⚙️ Introduction to Cybersecurity Concepts
​These problems introduce concepts used in cybersecurity, like hashing and basic network simulation.

​11. Basic Password Hashing Simulation
​Goal: Take a user's password as input and use the hashlib library (specifically the SHA-256 function) to print the hashed version of the password.
​Concepts: Importing libraries (import hashlib), calling module functions.
​Tip: Explain that hashing is a one-way street!

​12. Port Scanner Simulator
​Goal: Write a function that takes a list of ports (numbers) and checks if they are "open" or "closed" (e.g., port 80 is open, 22 is open, 1000 is closed). Crucially: He should NOT actually check the network. The program should just simulate it by using a predefined list of "open" ports (e.g., [21, 22, 80, 443]).
​Concepts: Lists, loops, conditional checks, simulating real-world functions.

​13. Simple Caesar Cipher Encrypter
​Goal: Implement a simple Caesar cipher (a shift cipher) that takes a message and a shift number (e.g., 3) and returns the encrypted message. For a shift of 3, 'A' becomes 'D', 'B' becomes 'E', etc.
​Concepts: Ordinal values (ord(), chr()), modular arithmetic for wrapping from 'Z' back to 'A'.
​🎲 Interactive and Game-like Problems
​These provide fun ways to practice input/output and logic.

​14. Simple Guessing Game
​Goal: The script randomly selects a number between 1 and 100. The user has to guess the number. The script should tell them if their guess is too high or too low until they get it right.
​Concepts: random module, while loops.

​15. Rock, Paper, Scissors
​Goal: Create a game where the user plays against the computer (which makes a random choice). The script keeps track of the score and declares a winner after 5 rounds.
​Concepts: random module, complex if/elif/else logic.
​Would you like me to elaborate on one of these problems, such as providing a basic code structure or explaining the cybersecurity relevance of a specific one?