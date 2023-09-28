"""
using regex for email validation
"""

import re
email = input("Enter your email: ")

pattern = re.compile(r"^[a-z A-Z 0-9 _ .+-]+@[a-z A-Z 0-9 -]+\.[a-z A-Z 0-9 -.]+$")

if pattern.match(email):
    print("Valid email")
else:
    print("Invalid email")


"""
This regex pattern validates email addresses with the following rules:
The local part (before the "@") can have letters (both cases), digits, underscores, periods, plus signs, and hyphens.
The domain part (after the "@") can have letters (both cases), digits, and hyphens.
The top-level domain (TLD) can have letters (both cases), digits, hyphens, and periods.
The pattern matches the entire email address from start to finish.
"""

