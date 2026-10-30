import re

def validate_identifier(reg_id):
    errors = []
    if not reg_id:
        return ["Identifier is empty"]
    
    parts = reg_id.split("-")
    if len(parts) != 3:
        errors.append("Malformed separators: expected exactly two hyphens ('-')")
        return errors

    year, dept, roll = parts

    if not (len(year) == 2 and year.isdigit()):
        errors.append("Invalid year component: must be exactly 2 digits")

    if not (3 <= len(dept) <= 4 and dept.isalpha() and dept.isupper()):
        errors.append("Invalid department component: must be 3-4 uppercase letters")

    if not (len(roll) == 4 and roll.isdigit()):
        errors.append("Invalid roll number component: must be exactly 4 digits")

    return errors

def validate_email(email):
    errors = []
    if not email:
        return ["Email is empty"]

    if email.count("@") != 1:
        errors.append("Malformed separator: must contain exactly one '@' symbol")
        return errors

    local_part, domain = email.split("@")

    if not local_part:
        errors.append("Missing local part")
    else:
        if local_part[0] in "._-" or local_part[-1] in "._-":
            errors.append("Invalid local part: cannot start or end with a separator")
        if re.search(r"[._-]{2,}", local_part):
            errors.append("Invalid local part: contains consecutive separators")
        if not re.fullmatch(r"[a-zA-Z0-9._-]+", local_part):
            errors.append("Invalid character group in local part: allowed characters are alphanumeric, '.', '_', '-'")

    if not domain:
        errors.append("Missing domain part")
    else:
        valid_tlds = (".edu", ".ac.in")
        if not any(domain.endswith(tld) for tld in valid_tlds):
            errors.append("Invalid domain suffix: must terminate in '.edu' or '.ac.in'")
        
        domain_labels = domain.split(".")
        if any(len(label) == 0 for label in domain_labels):
            errors.append("Malformed domain: contains empty labels or consecutive dots")
        else:
            for label in domain_labels:
                if not (label.isalpha() and label.islower()):
                    errors.append(f"Invalid domain label '{label}': must contain only lowercase letters")
                    break

    return errors

def main():
    test_id = input().strip()
    test_email = input().strip()

    id_errors = validate_identifier(test_id)
    email_errors = validate_email(test_email)

    print("--- Identifier Validation ---")
    if not id_errors:
        print("Status: VALID")
    else:
        print("Status: INVALID")
        for err in id_errors:
            print(f"- {err}")

    print("\n--- Email Validation ---")
    if not email_errors:
        print("Status: VALID")
    else:
        print("Status: INVALID")
        for err in email_errors:
            print(f"- {err}")

if __name__ == "__main__":
    main()
