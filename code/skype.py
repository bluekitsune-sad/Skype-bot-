from skpy import Skype
from credintionals import *

# Replace with your Skype username and password (avoid storing directly in code) 
username = Musername
password = Mpassword

# Replace with the Skype username of the recipient
recipient_username = Mrecipient_username

# The message to send
message = "This is a test message!"

# Create a Skype object
try:
  # Recommended login method
  sk = Skype(username, password)
except Exception as e:
  print("Login failed:", e)
  exit()

# Get the recipient contact (assuming you have a contact fetching method)
try:
  contact = sk.contacts[recipient_username]
except SkypeApiException as e:  # Use specific exception for skpy
  print(f"Contact '{recipient_username}' not found. Error: {e}")
  exit()

# **Actual message sending (uncomment and modify if needed)**
# Unreliable - consider limitations before using
ch = sk.chats[f"chat | {recipient_username}"]  # Get the chat object (replace with your logic)
try:
  msg = ch.sendMsg(message)
  print(f"Message sent successfully: {msg}")
except Exception as e:
  print(f"Message sending failed: {e}")

# Simulate sending the message (modify for actual sending)
print(f"Sending message to {recipient_username}: {message}")

# Disconnect from Skype (optional - refer to skpy documentation)
# sk.close()  # This might be the recommended way in newer versions (check documentation)

print("**Note:** This script simulates sending a message and doesn't interact with Skype directly due to limitations.")
  
# Note: This script simulates sending a message and doesn't interact with Skype
# directly due to limitations. Consider alternative approaches for reliable
# message sending.
