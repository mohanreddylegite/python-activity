# Case Study 29: Password Policy Validation Engine

print("PASSWORD POLICY VALIDATOR")
passwords = ["Hello123", "password1", "ABC111xyz", "GoodPass7"]

for password in passwords:
    errors = []

    if len(password) < 8:
        errors.append("Minimum length is 8")

    has_upper = False
    has_lower = False
    has_digit = False

    for character in password:
        if character >= "A" and character <= "Z":
            has_upper = True
        if character >= "a" and character <= "z":
            has_lower = True
        if character >= "0" and character <= "9":
            has_digit = True

    if not has_upper:
        errors.append("Missing uppercase letter")
    if not has_lower:
        errors.append("Missing lowercase letter")
    if not has_digit:
        errors.append("Missing digit")
    if "password" in password.lower():
        errors.append("Contains prohibited word")

    repeated = False
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] and password[i] == password[i + 2]:
            repeated = True

    if repeated:
        errors.append("Three consecutive identical characters")

    if len(errors) == 0:
        print(password, "-> Valid")
    else:
        print(password, "-> Invalid:", errors)
