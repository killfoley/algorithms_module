def replace_char(string):
    new_str = ""
    for c in string:
        if c == "e":
            new_str += "*"
        else:
            new_str += c
    return new_str

x = replace_char("impeachment")

print(x)
        