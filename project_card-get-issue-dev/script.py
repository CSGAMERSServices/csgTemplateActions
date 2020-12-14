import os
import re

issueNote = os.environ['INPUT_ISSUENOTE']

# Extract all email addresses from the Issue Note, store the last one
emailAddresses = re.findall(r'[\w\.-]+@[\w\.-]+', issueNote)
developer = emailAddresses[-1]

# Print developer as output
print(f"::set-output name=developer::{developer}")