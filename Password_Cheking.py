def Strong_pwd(char) :
    if len(char)<8 :
        return False
    if not any(i.isdigit() for i in char) :
        return False
    if not any(i.isupper() for i in char) :
        return False
    if not any(i.lower() for i in char) :
        return False
    if not any(i in "!@#$%^&*()_ " for i in char) :
        return False
    return True

print(Strong_pwd("Helowd"))
print(Strong_pwd("Helo@123"))