from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.optimizers import Adam
from data_preprocessing import get_preprocessed_data
from config import MODEL_CONFIG, NLP_CONFIG, MODEL_PATH

def create_model(vocab_size, num_classes):
    model = Sequential([
        Embedding(vocab_size, NLP_CONFIG['embedding_dim'], input_length=NLP_CONFIG['max_sequence_length']),
        GlobalAveragePooling1D(),
        Dense(16, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    X, y, tokenizer, label_encoder = get_preprocessed_data()
    
    vocab_size = len(tokenizer.word_index) + 1
    num_classes = len(label_encoder.classes_)
    
    model = create_model(vocab_size, num_classes)
    
    model.fit(
        X, y,
        epochs=MODEL_CONFIG['epochs'],
        batch_size=MODEL_CONFIG['batch_size'],
        verbose=MODEL_CONFIG['verbose']
    )
    
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()