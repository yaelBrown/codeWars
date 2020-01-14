with open("x.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print(i), repr(line)


"""
Stray byte? 

https://stackoverflow.com/questions/21639275/python-syntaxerror-non-ascii-character-xe2-in-file
"""