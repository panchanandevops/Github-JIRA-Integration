import os
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    # Jira API endpoint URL
    url = "https://panigrahimitu.atlassian.net/rest/api/3/issue"

    # Retrieve API token and email from environment variables
    API_TOKEN = os.getenv("API_TOKEN")
    EMAIL_ID = os.getenv("EMAIL_ID")

    # Set up HTTP authentication
    auth = HTTPBasicAuth(EMAIL_ID, API_TOKEN)

    # Define headers for the HTTP request
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get the JSON body from the incoming POST request
    request_json = request.get_json()

    # Check if "/jira" is present in the 'comment' body
    if 'comment' in request_json and 'body' in request_json['comment'] and '/jira' in request_json['comment']['body']:
        # Construct the Jira issue payload
        payload = json.dumps({
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Order entry fails when selecting supplier.",
                                    "type": "text"
                                }
                            ],
                            "type": "paragraph"
                        }
                    ],
                    "type": "doc",
                    "version": 1
                },
                "project": {
                    "key": "MP"
                },
                "issuetype": {
                    "id": "10006"
                },
                "summary": "Main order flow broken",
            },
            "update": {}
        })

        # Make a POST request to the Jira API
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        # Return the formatted JSON response
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        # If "/jira" is not present, return an empty response with status code 204
        return '', 204

# Run the Flask app if the script is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
