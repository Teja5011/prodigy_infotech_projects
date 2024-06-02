import re

def check_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Calculate score
    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Strength assessment
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

if __name__== "__main__":
    main()
