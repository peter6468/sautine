# ex of a custom module to be imported

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("√", email)
    )
