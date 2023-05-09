from twilio.rest import Client
def main():
    account_sid = 'AC042d3d8d98bc08c90d6e0f10ebb914cd'
    auth_token = 'ee8cc0a7b16838b6d3c5c5f67a542d86'
    client = Client(account_sid, auth_token)
    to_number = '+918825971199'
    from_number = '+16812216795'
    message = 'Thank you For Visiting my****'
    client.messages.create(to=to_number, from_=from_number, body=message)
    print("sucessfully send")
    
# Your Twilio account SID and auth token
# Create a Twilio client object

# The phone number you want to send the message to
# The phone number you want to send the message from (must be a Twilio phone number)
# The message you want to send
# Send the message





