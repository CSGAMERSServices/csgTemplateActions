import github
import os
import re

token = os.environ['INPUT_TOKEN']
cardNote = os.environ['INPUT_CARDNOTE']
issueUrl = os.environ['INPUT_ISSUEURL']


# If project card is linked to issue, collect issue assignees
if (issueUrl != None and len(issueUrl) > 0):
    # Get issue number from content URL
    issueNo = int(issueUrl.rsplit('/', 1)[-1])

    # Connect to GitHub
    g = github.Github(token)

    # Query issue information
    repo = g.get_repo('CSGAMERSServices/csgTemplate')
    issue = repo.get_issue(number=issueNo)
    
    # Collect email addresses in a list, convert list to comma-separated string
    assignees = ','.join([assignee.email for assignee in issue.assignees])

# If project card has no linked issue, extract email address from note
else:
    # Extract all email addresses from the note, only keep the last one
    emailAddresses = re.findall(r'[\w\.-]+@[\w\.-]+', cardNote)
    assignees = emailAddresses[-1]

# Print assignees as output
print(f"::set-output name=assignees::{assignees}")