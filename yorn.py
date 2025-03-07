"""
2025 Mar 09 tigerpointe
This variant was posted because it is different from the others.
The code uses a format string to generate the input prompt text.
It also uses logical and ternary operators for Boolean conversions.
A message is displayed in case the user accidentally chooses default.
The implementation is minimal with no additional modules imported.
The code is Python 3 compatible.  For Python 2, substitute:
answer = raw_input('{} ({}): '.format(prompt, yn)).strip()[:1].lower()
"""


def yorn(prompt, default=None):
    """ Prompts for Yes or No (yorn) input.  CAPS is used to denote the
    default value when neither Yes nor No is chosen.  The user input is
    stripped of any leading/trailing white-space and the lowercase first
    character is evaluated until a 'y' or 'n' is matched.
    Parameters:
    prompt  : (required) String representing a Yes or No question
    default : (optional) default value of None, True (Yes) or False (No)
    Returns:
    True for Yes, False for No, depending upon the user input
    """
    yn = 'Yes|No' if default is None else 'YES|no' if default else 'yes|NO'
    answer = ''
    while answer not in {'y', 'n'}:
        answer = input(f'{prompt} ({yn}): ').strip()[:1].lower()
        if (answer == '') and (default is not None):
            answer = 'y' if default else 'n'
            print('  Using default value:', 'Yes' if default else 'No')
    return answer == 'y'  # returns whether or not 'answer' equals 'yes'


# Sample usage
is_good = yorn('Is this a good example?', default=True)
if is_good:
    print('  I am really glad.')
else:
    print('  I am so sorry.')
