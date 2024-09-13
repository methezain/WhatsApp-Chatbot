import re
import os
import json

# Path to your input file
input_file_path = "WhatsApp Chat with Hassan Islam.txt"

# Path to your output file
output_file_path = "chat.json"

# Regex pattern to match timestamps, dates, and usernames
pattern = re.compile(r'^\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}\s?(?:AM|PM|am|pm)? - (Technologist|Hassan Islam):\s')

# Regex pattern to detect links
link_pattern = re.compile(r'http[s]?://\S+')

# Read the file and clean the lines
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Create a list to hold the conversation in a structured format
conversation = []
current_question = None

# Loop through lines and classify them as either questions (from Technologist) or answers (from Hassan Islam)
for line in lines:
    match = pattern.match(line)
    if match:
        sender = match.group(1)
        message = pattern.sub('', line).strip()

        # Ignore <Media omitted> messages and links
        if message == "<Media omitted>" or link_pattern.search(message):
            continue

        if sender == "Technologist":
            if current_question is not None:
                conversation.append({"question": current_question, "answer": ""})
            current_question = message
        elif sender == "Hassan Islam":
            if current_question is not None:
                conversation.append({"question": current_question, "answer": message})
                current_question = None

# Handle any unanswered questions
if current_question is not None:
    conversation.append({"question": current_question, "answer": ""})

# Remove entries with empty question or answer
conversation = [qa for qa in conversation if qa["question"] and qa["answer"]]

# Write the structured conversation to a JSON file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(conversation, output_file, ensure_ascii=False, indent=4)

# Check if the output file was created successfully
if os.path.exists(output_file_path):
    print(f"File saved at: {output_file_path}")
else:
    print("Error: File not created.")
