# Github-JIRA-Integration


## Project Overview:

### Objective:
- The objective of this project is to deploy a Flask API on an AWS EC2 instance that listens for GitHub webhook events.
- The Flask API, when triggered by a GitHub webhook, will create Jira issues based on the content of comments on GitHub issues.

### Components:

1. **GitHub Repository:**
   - A GitHub repository containing issues and comments that will trigger the webhook.

2. **Flask API on AWS EC2:**
   - A Flask web application deployed on an AWS EC2 instance.
   - The Flask app has an endpoint `/createJira` that is designed to receive GitHub webhook events.
   - The app checks if the comment in the webhook payload contains the string "/jira".
   - If "/jira" is present, it creates a Jira issue using the Jira REST API.
   - The app is set to listen on port 5000.

3. **GitHub Webhook:**
   - A GitHub webhook configured in the GitHub repository settings.
   - The webhook is set to trigger on specific events (e.g., Issue comments).
   - When an event occurs, GitHub sends a payload to the specified Flask API endpoint (`/createJira`).

4. **Jira API:**
   - Interaction with the Jira REST API to create issues based on GitHub comments.

### Workflow:

1. **User Comments on GitHub Issue:**
   - A user comments on an issue in the GitHub repository.

2. **GitHub Webhook Triggered:**
   - The GitHub webhook is triggered by the comment event.

3. **Flask API Receives GitHub Webhook Payload:**
   - The Flask API on the EC2 instance receives the GitHub webhook payload at the `/createJira` endpoint.

4. **Flask API Processes Webhook Payload:**
   - The Flask app processes the payload, checking if "/jira" is present in the comment body.
   - If present, it creates a corresponding Jira issue using the Jira API.

5. **Jira Issue Created:**
   - A Jira issue is created based on the content of the GitHub comment.

6. **Flask API Response:**
   - The Flask API responds with the result of the Jira issue creation.

### Additional Considerations:

- **Environment Variables:**
  - Sensitive information like API tokens and email IDs are stored in a `.env` file and loaded using the `dotenv` library.



## Configure GitHub Webhook:

In your GitHub repository, go to "Settings" > "Webhooks" > "Add webhook".
Set the Payload URL to http://your-ec2-instance-ip:5000/createJira (replace 5000 with the actual port if different).
Set the Content type to application/json.
Optionally, set a secret if you want to validate the authenticity of the incoming requests.
Select the events you want to trigger the webhook (e.g., Issue comments).
Add the webhook.

## Acknowledgments

I would like to express my gratitude to my teacher, **Abhishek Veeramalla**, for his invaluable guidance and support throughout the development of this project. His expertise and dedication have been instrumental in shaping my understanding and skills. I highly recommend checking out his insightful tutorials on his YouTube channel [Abhishek Veeramalla](https://www.youtube.com/@AbhishekVeeramalla) for further learning and inspiration.
