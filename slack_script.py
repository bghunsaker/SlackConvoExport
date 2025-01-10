# Author: Bryson Hunsaker
# Date:1/9/2025

import sys
import os
from dotenv import load_dotenv
#import logging
#logging.basicConfig(level=logging.DEBUG)
from slack_sdk import WebClient
import json 
OUTPUT_FILE = "convo_hist.txt"


load_dotenv()
token = os.getenv("slack_token")

if not token:
    print("Token environment variable not found.")
    
client = WebClient(token)
response = client.conversations_list(types="im, mpim")
#response = client.conversations_list(types="im, mpim, public_channel,private_channel")
    
# conversation history
conversation_history = []
# ID of the channel you want to send the message to
channel_id = os.getenv("channel_id")


# Call the conversations.history method using the WebClient
# conversations.history returns the first 100 messages by default
# These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
result = client.conversations_history(channel=channel_id, include_all_metadata=True)

with open('OUTPUT_FILE', 'w') as f:
    conversation_history = result["messages"]
    for x in conversation_history:
        f.write(json.dumps(x))
        f.write('\n')
        
    next = result["response_metadata"]['next_cursor']

    while next is not None:
        result = client.conversations_history(channel=channel_id, include_all_metadata=True, cursor=next)

        conversation_history = result["messages"]
        for x in conversation_history:
            f.write(json.dumps(x))
            f.write('\n')
        
        next = result["response_metadata"]['next_cursor']
        