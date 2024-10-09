# WhatsApp Bot Workflow

## Overview

This document outlines the workflow for the WhatsApp bot built using Flask and WATI. The bot interacts with users by sending messages and collecting information.

## Workflow Steps

1. **Start**: User sends 'join' to WhatsApp bot.
2. **Welcome Message**: Bot responds with a welcome message.
3. **Name Prompt**: Bot prompts the user for their name.
4. **User Inputs Name**: User provides their name.
5. **Email Prompt**: Bot prompts the user for their email address.
6. **User Inputs Email**: User provides their email address.
7. **Data Storage**: Bot stores the information in a database.
8. **End**: Bot confirms successful data storage to the user.

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


