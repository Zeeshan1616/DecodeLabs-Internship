# Expense Tracker

A simple command-line expense tracker built in Python with SQLite persistence. Built as part of the Decode Labs Python internship.

## Features

- **Add expenses** with amount, category, and auto-generated timestamp
- **View all expenses** in a clean tabular format
- **Summary report** with total, average, highest, lowest, and category-wise breakdown
- **Persistent storage** using SQLite (`expenses.db`)
- **Input validation** for amounts (no negatives, no invalid entries)
- Menu-driven interface — no external dependencies required

## Categories

Expenses are grouped into four categories:
- Food
- Transport
- Bills
- Other (default for anything unrecognized)

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `sqlite3` and `datetime`)

## How to Run

```bash
python expense_tracker.py
```

On first run, a database file `expenses.db` is created automatically in the same directory.

## Usage

Once running, you'll see a menu:

```
1. Add expense
2. View expenses
3. View summary
4. Quit
```

- **Add expense** — enter an amount and pick a category
- **View expenses** — see every recorded expense with ID, amount, category, and date
- **View summary** — get total spent, average, highest/lowest expense, and a breakdown by category
- **Quit** — exit the program

## Example Output

```
==================================================
ID  Amount      Category    Date
==================================================
1   250.00      food        2026-07-06 14:32
2   1500.00     bills       2026-07-06 14:33
==================================================
```

```
==============================
        EXPENSE SUMMARY
==============================
Total expenses entered : 2
Total spent            : 1750.00
Average expense        : 875.00
Highest expense        : 1500.00 (bills)
Lowest expense         : 250.00 (food)

Breakdown by category:
  food      : 250.00
  bills     : 1500.00
==============================
```

## Project Structure

```
expense_tracker.py   # Main application
expenses.db          # SQLite database (auto-created on first run)
```# DecodeLabs-Internship
Every task is uploaded into its seperate branch 
- Task 1:
    This branch is for the official task 1 of the internship
