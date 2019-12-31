'''
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
'''

# def bool_to_word(bool):
#   if (bool.lower() == "yes"):
#     return True
#   if (bool.lower() == "no"):
#     return False

# print(bool_to_word("Yes"))
# print(bool_to_word("No"))

def bool_to_word(yn):
  if (yn == True):
    return "Yes"
  if (yn == False):
    return "No"


'''
Can be cast to bool

def bool_to_word(bool):
    return ['No', 'Yes'][bool]

Standard 2 line answer

def bool_to_word(bool):
    return "Yes" if bool else "No"

'''
