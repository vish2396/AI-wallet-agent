import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import DATA_PATH, TRAINING_DATA_PATH, NLP_CONFIG

def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents

def prepare_training_data(intents, max_sequence_length):
    patterns = []
    labels = []
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            patterns.append(pattern)
            labels.append(intent['tag'])
    
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(patterns)
    
    X = tokenizer.texts_to_sequences(patterns)
    X = pad_sequences(X, maxlen=max_sequence_length)
    
    le = LabelEncoder()
    y = le.fit_transform(labels)
    
    return X, y, tokenizer, le

def save_training_data(X, y, tokenizer, label_encoder, file_path):
    data = {
        'X': [str(x) for x in X.tolist()],  # Convert numpy arrays to strings
        'y': y.tolist(),
        'tokenizer': tokenizer.to_json(),
        'label_encoder': label_encoder.classes_.tolist()
    }
    pd.DataFrame(data).to_csv(file_path, index=False)

def get_preprocessed_data():
    intents = load_intents(DATA_PATH)
    X, y, tokenizer, le = prepare_training_data(intents, NLP_CONFIG['max_sequence_length'])
    save_training_data(X, y, tokenizer, le, TRAINING_DATA_PATH)
    return X, y, tokenizer, le

if __name__ == "__main__":
    get_preprocessed_data()