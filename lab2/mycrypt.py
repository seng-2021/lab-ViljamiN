import codecs


def encode(s):
    if not isinstance(s, str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=', '!"#€%&/()=1234567890'))
    invalid_characters = {'\xe5', '\xe4', '\xf6'}

    if len(s) > 1000:
        raise ValueError
    else:
        # here we add padding to the string to make it 1000 characters long
        s += "a" * (1000 - len(s))

    for c in s:
        if c in invalid_characters:
            # in this case, the character is not allowed
            raise ValueError
        elif c.isalpha():
            if c.islower():
                c = c.upper()
            # Rot13 the character for maximum security
            crypted += codecs.encode(c, 'rot_13')
        elif c in digitmapping:
            crypted += digitmapping[c]
        else:
            # in this case, the character is not allowed
            raise ValueError

    origlen_crypted = crypted[:origlen]

    return origlen_crypted


def decode(s):
    decrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=', '!"#€%&/()=1234567890'))
    for c in s:
        if c.isalpha():
            if c.isupper():
                c = c.lower()
            decrypted += codecs.decode(c, 'rot_13')
        elif c in digitmapping:
            decrypted += digitmapping[c]

    return decrypted
