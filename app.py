from flask import Flask, request, jsonify
import requests
from models import db, User

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize the database
with app.app_context():
    db.create_all()

# WATI API credentials
WATI_API_URL = 'https://api.wati.io/v1/messages/send'
WATI_API_KEY = 'YOUR_WATI_API_KEY' #Wati api key(If we get key we can add here)

# Function to send a message
def send_message(phone_number, message):
    headers = {
        'Authorization': f'Bearer {WATI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'phone': phone_number,
        'message': message
    }
    response = requests.post(WATI_API_URL, headers=headers, json=data)
    return response.json()

# Webhook to receive messages
@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_data = request.json
    phone_number = incoming_data['data']['sender']['phone']
    message = incoming_data['data']['message']

    # Find user by phone number
    user = User.query.filter_by(phone_number=phone_number).first()

    if message.lower() == 'join':
        # New user joins the conversation
        if user is None:
            user = User(phone_number=phone_number)
            db.session.add(user)
            db.session.commit()
        send_message(phone_number, "Welcome to our service! What is your name?")
    
    elif user and user.name is None:
        # User provided their name
        user.name = message
        db.session.commit()
        send_message(phone_number, f"Thank you, {message}! What is your email address?")
    
    elif user and user.email is None:
        # User provided their email
        user.email = message
        db.session.commit()
        send_message(phone_number, "Thank you for sharing your information!")
        

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
