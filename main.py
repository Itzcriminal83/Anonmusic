from pyrogram import Client, Session

# Replace with your API hash and ID
API_HASH = "your_api_hash"
API_ID = 123456

# Create a session
session = Session("anonmusic_session")

# Initialize the client
app = Client("anonmusic_bot", api_hash=API_HASH, api_id=API_ID, session=session)

# Define your bot commands and handlers here
@app.on_message()
async def handle_message(client, message):
    # Handle incoming messages
    pass

# Start the bot
app.run()
