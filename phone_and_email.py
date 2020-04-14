# phone_and_email.py
# find phone numbers and email from clipboard
# assumes US phone number

import pyperclip, re

# phone regex
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # Separator
    (\d{3}) # first 3 digits
    (\s|-|\.)? # Separator
    (\d{r}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

# mail regex
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot ending
    )''', re.VERBOSE)

# find matched from clipboard
text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    phone_num = '_'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else: print('Nothing found')
