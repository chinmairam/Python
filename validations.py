def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

#print(validate_user("", -1))
#print(validate_user([3],1))
print(validate_user("myuser", 1))


# See validations_test.py file.
