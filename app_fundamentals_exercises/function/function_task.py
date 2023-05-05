def password_validator():
    return f"""Password validator:\nWrite a function that checks if a given password is valid. Password validations are:
    \n•	It should be 6 - 10 (inclusive) characters long\n•	It should consist only of letters and digits
    \n•	It should have at least 2 digits\nIf a password is valid, print "Password is valid". 
    \nOtherwise, for every unfulfilled rule, print a message: \n•	"Password must be between 6 and 10 characters" 
    \n•	"Password must consist only of letters and digits" \n•	"Password must have at least 2 digits\n\nExample:
    \nInput:\nlogin\nOutput:\nPassword must be between 6 and 10 characters\nPassword must have at least 2 digits """
