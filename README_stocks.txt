=====================================================
            STOCK PORTFOLIO TRACKER (PYTHON)
=====================================================

1. ABOUT THE PROJECT
--------------------
A console-based Stock Portfolio Tracker written in Python.
The user enters stock symbols and the number of shares they
own. The program looks up each stock's price from a
hardcoded dictionary, calculates the value of each holding,
and displays the total investment value.

The summary can optionally be saved to a text file.

This project was built as part of a Python programming
internship task.


2. FEATURES
-----------
- Hardcoded dictionary of 10 stock prices (no internet/API)
- Shows the list of available stocks and their prices
- User enters a stock symbol and quantity
- Quantity can be a decimal number (e.g. 2.5 shares)
- Adding the same stock again adds to its quantity
- Input validation for unknown symbols and invalid or
  non-positive quantities
- Calculates the value of each holding (shares x price)
- Displays a portfolio summary with the total investment
- Optionally saves the summary to a file of your choice
  (default name: portfolio.txt)


3. AVAILABLE STOCKS AND PRICES
------------------------------
AAPL    $333.69
TSLA    $370.59
GOOGL   $343.50
MSFT    $517.53
AMZN    $251.52
LLY     $1142.85
META    $728.08
AVGO    $355.14
NVDA    $233.95
NFLX    $67.06

(Prices are fixed values stored in the program. To add or
change a stock, edit the "stock_prices" dictionary at the
top of stocks.py.)


4. REQUIREMENTS
---------------
- Python 3.6 or higher (uses f-strings)
- No external libraries needed


5. HOW TO RUN
-------------
1. Open a terminal / command prompt in the project folder
2. Run:

       python stocks.py

   (On some systems use: python3 stocks.py)


6. HOW TO USE
-------------
1. The program lists the available stocks and prices.
2. Type a stock symbol (e.g. AAPL) and press Enter.
3. Type the quantity of shares and press Enter.
4. Repeat for as many stocks as you like.
5. Type "done" to finish and see the summary.
6. Choose "y" to save the summary to a file, or "n" to exit.


7. SAMPLE RUN
-------------
Welcome to the Stock Portfolio Tracker!

Available stocks and their prices:
  AAPL   $333.69
  ...

Enter stock symbol (or 'done' to finish): aapl
Enter quantity of AAPL: 10
Added 10.0 share(s) of AAPL.

Enter stock symbol (or 'done' to finish): googl
Enter quantity of GOOGL: 20
Added 20.0 share(s) of GOOGL.

Enter stock symbol (or 'done' to finish): done

========================================
PORTFOLIO SUMMARY
========================================
AAPL     10.0 shares x $333.69 = $3,336.90
GOOGL    20.0 shares x $343.5  = $6,870.00
----------------------------------------
TOTAL INVESTMENT             $10,206.90
========================================

Save this summary to a file? (y/n): y
Enter filename (e.g. portfolio.txt): portfolio.txt
Saved! Check the file 'portfolio.txt' in your project folder.


8. HOW THE TOTAL IS CALCULATED
------------------------------
Value of each stock = number of shares x price per share
Total investment    = sum of all stock values

Example:
  AAPL  : 10 x 333.69 = 3,336.90
  GOOGL : 20 x 343.50 = 6,870.00
  Total : 3,336.90 + 6,870.00 = 10,206.90


9. PROGRAM STRUCTURE (FUNCTIONS)
--------------------------------
show_available_stocks()  - prints the stocks and prices
get_quantity(symbol)     - asks for and validates quantity
build_portfolio()        - collects stocks and quantities
calculate_total()        - computes each value and the total
print_summary()          - displays the portfolio summary
save_to_file()           - optionally saves the summary
main()                   - runs the whole program


10. CONCEPTS USED
-----------------
- Dictionaries (stock symbol -> price)
- Functions
- while loops and if conditions
- Input and output
- Exception handling (try / except)
- Basic arithmetic
- String formatting (f-strings)
- File handling (open, write, with statement)


11. FILE STRUCTURE
------------------
stock-portfolio-tracker/
|-- stocks.py           (main program)
|-- README_stocks.txt   (this file)
|-- portfolio.txt       (created only if you choose to save)


12. POSSIBLE IMPROVEMENTS
-------------------------
- Fetch live prices using a stock API
- Also save the summary as a .csv file
- Allow removing or editing stocks in the portfolio
- Show the percentage share of each stock


=====================================================
          Thank you for using the Portfolio Tracker!
=====================================================
