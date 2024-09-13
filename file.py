import re
import json

# Function to preprocess a sentence
def preprocess_sentence(sentence):
    sentence = sentence.lower().strip()
    sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
    sentence = re.sub(r'[" "]+', " ", sentence)
    sentence = re.sub(r"i'm", "i am", sentence)
    sentence = re.sub(r"he's", "he is", sentence)
    sentence = re.sub(r"she's", "she is", sentence)
    sentence = re.sub(r"it's", "it is", sentence)
    sentence = re.sub(r"that's", "that is", sentence)
    sentence = re.sub(r"what's", "what is", sentence)
    sentence = re.sub(r"where's", "where is", sentence)
    sentence = re.sub(r"how's", "how is", sentence)
    sentence = re.sub(r"\'ll", " will", sentence)
    sentence = re.sub(r"\'ve", " have", sentence)
    sentence = re.sub(r"\'re", " are", sentence)
    sentence = re.sub(r"\'d", " would", sentence)
    sentence = re.sub(r"won't", "will not", sentence)
    sentence = re.sub(r"can't", "cannot", sentence)
    sentence = re.sub(r"n't", " not", sentence)
    sentence = re.sub(r"n'", "ng", sentence)
    sentence = re.sub(r"'bout", "about", sentence)
    sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
    sentence = sentence.strip()
    return sentence

# Function to load and preprocess conversations
def load_conversations(messages):
    inputs, outputs = [], []
    for i in range(len(messages) - 1):
        inputs.append(preprocess_sentence(messages[i]))
        outputs.append(preprocess_sentence(messages[i + 1]))
        if len(inputs) >= MAX_SAMPLES:
            return inputs, outputs
    return inputs, outputs

# Load chat data from JSON file
def load_chat_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [message['text'] for message in data['messages']]

MAX_SAMPLES = 10000

# Assuming the JSON file is named 'chat_data.json'
file_path = 'chat.json'
messages = load_chat_data(file_path)

# Load conversations
questions, answers = load_conversations(messages)

# Optionally, print some of the processed questions and answers
for q, a in zip(questions[:5], answers[:5]):
    print(f"Question: {q}")
    print(f"Answer: {a}\n")