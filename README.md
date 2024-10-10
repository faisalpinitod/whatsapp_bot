# WhatsApp Bot Workflow

## Overview

This document outlines the workflow for the WhatsApp bot built using Flask and WATI. The bot interacts with users by sending messages and collecting information.

## Workflow Steps

1. **Start**: User sends a join code to the WhatsApp bot.
2. **User Joins**: The bot validates the join code and creates the user profile.
3. **Greeting**: User sends "hi" to the WhatsApp bot.
4. **Welcome Message**: The bot responds with a welcome message.
5. **Name Prompt**: The bot prompts the user for their name.
6. **User Inputs Name**: The user provides their name.
7. **Email Prompt**: The bot prompts the user for their email address.
8. **User Inputs Email**: The user provides their email address.
9. **Data Storage**: The bot stores the information (name and email) in a database.
10. **Confirmation**: The bot confirms successful data storage to the user.
11. **Further Interaction**: The bot responds to any further user messages with appropriate replies, such as "How can I assist you today?" for greetings.


## Diagram

Here’s a visual representation of the workflow:

![WhatsApp Bot Workflow Diagram](images/whatsapp_bot_workflow.png)

## Running the Bot with Ngrok

To test the bot locally, you can use [Ngrok](https://ngrok.com/) to expose your local server to the internet. Follow these steps to run the bot:

1. Install Ngrok by following the instructions on their [official website](https://ngrok.com/download).
2. Start your Flask server by running:
   ```bash
   flask run
   ```
3. In a separate terminal window, run Ngrok to expose your Flask server:
   ```bash
   ngrok http 5000
   ```
4. Ngrok will generate a public URL (e.g., https://xyz.ngrok.io). Use this URL as the webhook URL in your WATI     account settings or Twilio console for the WhatsApp bot.
5. Your bot is now publicly accessible, and you can interact with it via WhatsApp.


## Conclusion

This workflow ensures a smooth interaction between the user and the WhatsApp bot, allowing for efficient data collection and confirmation.


