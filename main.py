from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACefa8cf472e13295a5a5e21c7949efde2"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17135577076",
    from_="+14788889199",
    body="Hello from Python!")

print(message.sid)
