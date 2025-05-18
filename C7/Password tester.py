import re
import secrets
import string

# Common password list (top100 weak passwords + custom extensions)
COMMON_PASSWORDS = {
    'password', '123456', '12345678', '123456789', '12345',
    '1234567', '1234567890', 'qwerty', 'abc123', '111111',
    'admin', 'letmein', 'welcome', 'monkey', 'password1',
    '123123', 'qwertyuiop', 'sunshine', 'iloveyou', 'admin123'
}

def is_common_password(password):
    """Check if password is in common password list"""
    return password.lower() in COMMON_PASSWORDS

def check_password_strength(password):
    """Evaluate password strength logic"""
    if is_common_password(password):
        return 0  # Weak
    
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[^A-Za-z0-9]', password)
    
    char_types = sum([bool(has_upper), bool(has_lower), 
                     bool(has_digit), bool(has_special)])
    
    if length >= 12 and char_types >= 3:
        return 2  # Strong
    elif length >= 8 and char_types >= 2:
        return 1  # Medium
    else:
        return 0  # Weak

def generate_strong_password(length=16):
    """Generate strong password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[^A-Za-z0-9]', password)):
            return password

def main():
    print("Password Security Check System")
    print("Type 'exit' to quit\n")
    
    while True:
        password = input("Enter password to check: ").strip()
        if password.lower() == 'exit':
            break
            
        strength = check_password_strength(password)
        
        print("\nCheck result:")
        if strength == 0:
            print("""Weak Password
This password is insecure. Attackers can quickly crack it.
Not suitable for high-security environments like banking or corporate systems""")
        elif strength == 1:
            print("""Medium Strength
This password has moderate security. It would take attackers significant time to crack,
but we recommend changing it regularly and not using it long-term""")
        else:
            print("""Strong Password
This is a highly secure password that would take attackers considerable time to crack,
suitable for high-security environments""")
            
        if strength < 2:
            generate = input("\nGenerate strong replacement? (y/n): ").lower()
            if generate == 'y':
                new_pass = generate_strong_password()
                print(f"\nRecommended strong password: {new_pass}")
                print("Please store this password securely\n")
                
        print("-" * 50)

if __name__ == "__main__":
    main()
