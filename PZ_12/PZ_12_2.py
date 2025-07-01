import string

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

lowercase_chars = [char for char in text if char in string.ascii_lowercase]
print("Символы нижнего регистра:", ''.join(lowercase_chars))

