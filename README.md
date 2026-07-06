# Random Password Generator

A command-line utility for generating cryptographically secure passwords, with built-in entropy calculation and strength classification.

Developed as part of the Decode Labs Python Internship Program.

## Overview

This tool generates passwords using Python's `secrets` module, which is designed for cryptographic use cases (unlike the standard `random` module). It supports configurable character sets, guarantees representation from each selected character type, and reports the statistical strength of every password generated.

## Features

| Feature | Description |
|---|---|
| Cryptographic randomness | Uses the `secrets` module for secure random selection |
| Configurable character sets | Letters, numbers, and symbols can be toggled independently |
| Guaranteed character coverage | At least one character from each selected set is included in every password |
| Ambiguous character filtering | Optionally excludes visually similar characters (`i`, `l`, `1`, `L`, `o`, `0`, `O`) |
| Entropy calculation | Quantifies password strength in bits |
| Strength classification | Categorizes passwords as Weak, Moderate, Strong, or Very Strong |
| Batch generation | Generates multiple passwords per session |

## Requirements

- Python 3.x
- No external dependencies (uses the standard library modules `string`, `secrets`, and `math`)

## Installation

```bash
git clone <repository-url>
cd password-generator
```

No additional setup is required.

## Usage

Run the script from the command line:

```bash
python password_generator.py
```

The program will prompt for the following inputs:

1. **Password length** — minimum of 8 characters
2. **Character types** — whether to include letters, numbers, and/or symbols
3. **Ambiguous character exclusion** — whether to exclude lookalike characters
4. **Number of passwords** to generate

If no character type is selected, the program defaults to letters and numbers.

## Example

```
Random Password Generator - DecodeLabs
Generates cryptographically secure passwords using the secrets module.

Enter password length (min 8): 12
Include letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
Exclude ambiguous characters (l, 1, O, 0)? (y/n): n
How many passwords to generate? 3

==================================================
              GENERATED PASSWORDS
==================================================
1. xT9$mK2#pLzQ
2. R7&vB4nW!qA9
3. h2Xz@8mNpT#3
--------------------------------------------------
Length          : 12
Character pool  : 94 unique characters
Entropy         : 78.7 bits
Strength rating : Strong
==================================================
```

## Technical Details

**Character coverage guarantee**
One character is drawn from each selected character pool first, ensuring representation. The remaining characters are drawn from the combined pool, and the full result is shuffled to randomize character positions.

**Entropy calculation**
Entropy is calculated using the standard formula:

```
entropy (bits) = length × log2(pool_size)
```

**Strength classification**

| Entropy Range (bits) | Rating |
|---|---|
| < 40 | Weak |
| 40 – 59 | Moderate |
| 60 – 79 | Strong |
| 80+ | Very Strong |

## Project Structure

```
password_generator.py    # Application entry point and core logic
```

## License

This project is available for personal and educational use.
