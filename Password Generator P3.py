import string
import secrets
import math

AMBIGUOUS_CHARS = "il1Lo0O"


def get_length():
    while True:
        length = input("Enter password length (min 8): ")

        try:
            length = int(length)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if length < 8:
            print("Length should be at least 8 characters for a secure password.\n")
            continue

        return length


def get_yes_no(prompt):
    return input(prompt).strip().lower() == "y"


def build_char_pool(use_letters, use_numbers, use_symbols, exclude_ambiguous):
    pools = []
    if use_letters:
        pools.append(string.ascii_letters)
    if use_numbers:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if exclude_ambiguous:
        pools = [
            "".join(c for c in pool if c not in AMBIGUOUS_CHARS)
            for pool in pools
        ]

    return pools


def generate_password(length, pools):
    # guarantee at least one character from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]

    full_pool = "".join(pools)
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(full_pool) for _ in range(remaining)]

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def calculate_entropy(length, pool_size):
    if pool_size == 0:
        return 0
    return length * math.log2(pool_size)


def rate_strength(entropy_bits):
    if entropy_bits < 40:
        return "Weak"
    elif entropy_bits < 60:
        return "Moderate"
    elif entropy_bits < 80:
        return "Strong"
    else:
        return "Very Strong"


def generate_report(length, pools, count):
    full_pool = "".join(pools)
    entropy_bits = calculate_entropy(length, len(full_pool))
    strength = rate_strength(entropy_bits)

    print("\n==================================================")
    print("              GENERATED PASSWORDS")
    print("==================================================")

    for i in range(count):
        password = generate_password(length, pools)
        print(f"{i + 1}. {password}")

    print("--------------------------------------------------")
    print(f"Length          : {length}")
    print(f"Character pool  : {len(full_pool)} unique characters")
    print(f"Entropy         : {entropy_bits:.1f} bits")
    print(f"Strength rating : {strength}")
    print("==================================================\n")


def main():
    print("Random Password Generator - DecodeLabs")
    print("Generates cryptographically secure passwords using the secrets module.\n")

    while True:
        length = get_length()

        use_letters = get_yes_no("Include letters? (y/n): ")
        use_numbers = get_yes_no("Include numbers? (y/n): ")
        use_symbols = get_yes_no("Include symbols? (y/n): ")
        exclude_ambiguous = get_yes_no("Exclude ambiguous characters (l, 1, O, 0)? (y/n): ")

        if not (use_letters or use_numbers or use_symbols):
            print("\nNo character types selected. Defaulting to letters and numbers.")
            use_letters = True
            use_numbers = True

        pools = build_char_pool(use_letters, use_numbers, use_symbols, exclude_ambiguous)

        while True:
            count = input("How many passwords to generate? ")
            try:
                count = int(count)
                if count < 1:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a positive number.\n")

        generate_report(length, pools, count)

        again = get_yes_no("Generate more passwords? (y/n): ")
        if not again:
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()