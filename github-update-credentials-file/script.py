import github
import json
import os

token = os.environ['INPUT_TOKEN']
repoName = os.environ['GITHUB_REPOSITORY']
projectCardId = os.environ['INPUT_PROJECTCARDID']
displayUserJson = json.loads(os.environ['INPUT_DISPLAYUSERJSON'])
displayUrlJson = json.loads(os.environ['INPUT_DISPLAYURLJSON'])


# Connect to GitHub
g = github.Github(token)

# Get credentials file from repo
repo = g.get_user().get_repo(repoName)
file = repo.get_file_contents('credentials.txt')

# Update file with new credentials
repo.update_file('credentials.txt', 'your_commit_message', 'your_new_file_content', file.sha)