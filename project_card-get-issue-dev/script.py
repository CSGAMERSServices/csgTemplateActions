import os
import re

cardNote = os.environ['INPUT_CARDNOTE']
issueUrl = os.environ['INPUT_ISSUEURL']

print('Issue URL')
print(issueUrl)

# Extract all email addresses from the Issue Note, store the last one
emailAddresses = re.findall(r'[\w\.-]+@[\w\.-]+', issueNote)
developer = emailAddresses[-1]

# Print developer as output
print(f"::set-output name=developer::{developer}")