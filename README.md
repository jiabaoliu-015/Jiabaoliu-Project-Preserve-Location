# This is used for C7. Implement a security solution of your choice and put it on your GitHub. (Written in Python)

## Password tester:
The password strength detector uses four factors to determine whether a password is strong or not.
1. Local blacklist check for common passwords (including 20 high-risk passwords).
2. The password strength detector uses four factors to determine whether a password is strong or not. (Length / Capitalisation / Lowercase / Numbers / Special Characters) 
3. Grade-based security alert system: Alerts users on the strength of their passwords and whether they need to be changed.
4. Loop interaction test interface: Enables users to conduct tests with multiple passwords in succession without the need to restart the system.
## Hard password generator
If the user needs to enhance security, the user can use a "hard password generator". To generate a hard password, avoid brute force password cracking.
1. Users can input a password that they can remember as the base token for the generator.
2. Use PBKDF2-HMAC-SHA256 as the key derivation algorithm
3. The fixed salt value is stored in the code.
4. Generation process: User password + fixed salt → PBKDF2 iteration 100,000 times → 64-byte derived key → Base64 encoding → Extract 16-character password


