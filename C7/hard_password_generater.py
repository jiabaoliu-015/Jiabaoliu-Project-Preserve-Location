import hashlib
import base64
import getpass

# Configuration parameters
SALT = b'fixed_cline_salt_1234'  # 32-byte fixed salt
ITERATIONS = 100000              # PBKDF2 iterations
PWD_LENGTH = 16                 # Generated password length

def generate_strong_password():
    try:
        # Get and normalize user input
        user_input = getpass.getpass("Enter your base password: ").strip()
        
        if not user_input:
            raise ValueError("Password cannot be empty")
        if len(user_input) < 4:
            raise ValueError("Password must be at least 4 characters")
        
        # PBKDF2 key derivation
        dk = hashlib.pbkdf2_hmac(
            'sha256',
            user_input.encode('utf-8'),
            SALT,
            ITERATIONS,
            64  # generate a 64-byte key
        )
        
        # Base64 encode and replace special characters
        b64_str = base64.b64encode(dk).decode('utf-8')
        safe_str = b64_str.replace('+', '@').replace('/', '!').replace('=', '$')
        
        # Ensure inclusion of four character types
        final_pwd = []
        char_types = {
            'lower': 'abcdefghjkmnpqrstuvwxyz',
            'upper': 'ABCDEFGHJKLMNPQRSTUVWXYZ',
            'digit': '23456789',
            'special': '@!$'
        }
        
        # Select at least one character from each type
        final_pwd.append(char_types['lower'][len(safe_str) % 23])
        final_pwd.append(char_types['upper'][len(safe_str) % 19])
        final_pwd.append(char_types['digit'][len(safe_str) % 8])
        final_pwd.append(char_types['special'][len(safe_str) % 4])
        
        # Fill remaining characters
        remaining = PWD_LENGTH - 4
        for i in range(remaining):
            final_pwd.append(safe_str[(i*3) % len(safe_str)])
        
        # Shuffle while maintaining determinism
        return ''.join(final_pwd)[::-1][:PWD_LENGTH]
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    strong_pwd = generate_strong_password()
    if strong_pwd:
        print("\nGenerated Strong Password:")
        print(f"{strong_pwd[:4]}-{strong_pwd[4:8]}-{strong_pwd[8:12]}-{strong_pwd[12:]}")
