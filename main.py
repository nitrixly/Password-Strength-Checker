import re
from colorama import Fore, Style, init

init(autoreset=True)

def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
        feedback.append(Fore.GREEN + "✓ Nice! Length is good (12+ characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append(Fore.YELLOW + "✓ Decent length (8-11 characters).")
    else:
        feedback.append(Fore.RED + "✗ Too short, aim for at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Great! You've got uppercase letters.")
    else:
        feedback.append(Fore.RED + "✗ Add some uppercase letters to mix it up.")

    if re.search(r"[a-z]", password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Good job! Lowercase letters are included.")
    else:
        feedback.append(Fore.RED + "✗ Include some lowercase letters.")

    if re.search(r"\d", password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Nice! You've got numbers in there.")
    else:
        feedback.append(Fore.RED + "✗ Try adding some numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Awesome! Special characters included.")
    else:
        feedback.append(Fore.RED + "✗ Add a special character to make it stronger.")

    if score >= 5:
        strength = Fore.GREEN + Style.BRIGHT + "Very Strong"
    elif score >= 3:
        strength = Fore.YELLOW + Style.BRIGHT + "Moderate"
    else:
        strength = Fore.RED + Style.BRIGHT + "Weak"

    return strength, feedback

password = input(Fore.CYAN + "Enter a password to see how strong it is: ")

strength, feedback = evaluate_password(password)

print("\n" + Fore.BLUE + Style.BRIGHT + "Here's the breakdown of your password:")
for line in feedback:
    print("  " + line)

print("\n" + Fore.MAGENTA + Style.BRIGHT + f"Overall Password Strength: {strength}")
