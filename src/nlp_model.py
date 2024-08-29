import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from config import MAX_SEQUENCE_LENGTH, EMBEDDING_DIM, NUM_CLASSES

class NLPModel:
    def _init_(self, vocab_size):
        self.model = self.build_model(vocab_size)

    def build_model(self, vocab_size):
        model = Sequential([
            Embedding(vocab_size, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH),
            LSTM(64),
            Dense(NUM_CLASSES, activation='softmax')
        ])
        model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])
        return model
    
    def train(self, X, y, epochs=50, batch_size=32):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, validation_split=0.2)

    def save_model(self, file_path):
        self.model.save(file_path)

    def laod_model(self, file_path):
        self.model = load_model(file_path)

    def predict_intent(self, text, tokenizer, label_encoder):
        sequence = tokenizer.texts_to_sequences([text])
        padded_sequence = padded_sequence(sequence, maxlen=MAX_SEQUENCE_LENGTH)
        prediction = self.model.predict(padded_sequence)
        intent_index = np.argmax(prediction)
        return label_encoder.inverse_transform([intent_index])[0]