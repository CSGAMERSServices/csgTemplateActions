import os
import github


token = os.environ['INPUT_TOKEN']
fromColumnId = os.environ['INPUT_FROMCOLUMNID']
fromColumnName = os.environ['INPUT_FROMCOLUMNNAME']
toColumnId = os.environ['INPUT_TOCOLUMNID']
toColumnName = os.environ['INPUT_TOCOLUMNNAME']

# Authenticate to GitHub API
github = github.Github(token)

# Get source and destination column
fromColumn = github.get_project_column(int(fromColumnId))
toColumn = github.get_project_column(int(toColumnId))

# Check whether expected source and destination column match
isMatch = (fromColumn.name.lower() == fromColumnName.lower() and toColumn.name.lower() == toColumnName.lower())

# Print isMatch as output
print(f"::set-output name=isMatch::{isMatch}")