from flask import Flask, request, jsonify
from models import db, User
import os
from dotenv import load_dotenv
from twilio.rest import Client  # Twilio library for sending messages

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()

# Twilio API settings, loaded from .env file
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Function to send a message using Twilio API
# Function to send a message using Twilio API
def send_message(phone_number, message):
    try:
        # Ensure phone number is in the correct format for Twilio
        twilio_number = TWILIO_PHONE_NUMBER  # Get Twilio WhatsApp number
        full_number = f"whatsapp:{phone_number}"  # Format user number with WhatsApp prefix
        
        print(f"Sending message to {full_number}: {message}")  # Debug statement
        message = twilio_client.messages.create(
            body=message,
            from_=twilio_number,  # Use the Twilio WhatsApp number
            to=full_number  # User's WhatsApp phone number
        )
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        print(f"Error sending message: {str(e)}")  # Debug statement
        return {"status": "error", "error": str(e)}


# Webhook to receive messages
@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract data from Twilio's form-encoded request
    phone_number = request.form.get('From')  # User's phone number in WhatsApp
    message = request.form.get('Body')  # Message content sent by the user
    
    # Format phone number correctly for database lookup
    phone_number = phone_number.replace("whatsapp:", "")  # Twilio sends numbers in this format

    # Find user by phone number in the database
    user = User.query.filter_by(phone_number=phone_number).first()

    if user is None:
        print(f"Creating new user with phone number: {phone_number}")  # Debug statement
        user = User(phone_number=phone_number)  # Create a new user in the database
        db.session.add(user)
        db.session.commit()
        send_message(phone_number, "Welcome to our service! What is your name?")
    
    elif user.name is None:
        # User provided their name
        user.name = message  # Save the name in the database
        db.session.commit()
        send_message(phone_number, f"Thank you, {message}! What is your email address?")
    
    elif user.email is None:
        # User provided their email
        user.email = message  # Save the email in the database
        db.session.commit()
        send_message(phone_number, "Thank you for sharing your information!")
    
    else:
        # User is already registered, respond to casual messages
        send_message(phone_number, "Hello! How can I assist you today?")

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
