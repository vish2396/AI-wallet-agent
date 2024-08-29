from nlp_model import NLPModel
from responses import get_response
from coinbase_client import CoinbaseClient
from config import COINBASE_API_KEY, COINBASE_API_SECRET

app = Flask(__name__)
nlp_model = NLPModel()
coinbase_client = CoinbaseClient(COINBASE_API_KEY, COINBASE_API_SECRET)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    intent = nlp_model.predict_intent(user_message)
    response = get_response(intent, user_message, coinbase_client)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)