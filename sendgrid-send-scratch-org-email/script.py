import json
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


displayUserJson = json.loads(os.environ['INPUT_DISPLAYUSERJSON'])
displayUrlJson = json.loads(os.environ['INPUT_DISPLAYURLJSON'])
sendgridApiKey = os.environ['INPUT_SENDGRIDAPIKEY']
fromEmail = os.environ['INPUT_FROMEMAIL']
toEmail = os.environ['INPUT_TOEMAIL']

content = '''Your scratch org is now ready!

You can validate your changes at {displayUrl}.


Below are additional details of your org.

Org ID: {orgId}

Username: {username}

Instance URL: {instanceUrl}

Login URL: {loginurl}
'''.format(displayUrl = displayUrlJson['result']['url'],
           orgId = displayUserJson['result']['orgId'],
           username = displayUserJson['result']['username'],
           instanceUrl = displayUserJson['result']['instanceUrl'],
           loginurl = displayUserJson['result']['loginUrl'])

message = Mail(
    from_email = fromEmail,
    to_emails = toEmail,
    subject = 'Scratch org created',
    html_content = content)

try:
    sg = SendGridAPIClient(sendgridApiKey)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)