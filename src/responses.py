import random

def get_response(intent, user_message, coinbase_client):
    responses = {
        'greeting': ['Hello!', 'Hi there!', 'Greetings!'],
        'farewell': ['Goodbye!', 'See you later!', 'Take care!'],
        'thanks': ['You\'re welcome!', 'Glad I could help!', 'My pleasure!'],
        'price_inquiry': handle_price_inquiry,
        'help': ['I can help you with cryptocurrency prices and basic information. Just ask!'],
        'fallback': ['I\'m not sure I understand. Could you please rephrase that?', 'I didn\'t quite catch that. Can you try again?']
    }

    if intent in responses:
        if callable(responses[intent]):
            return responses[intent](user_message, coinbase_client)
        else:
            return random.choice(responses[intent])
        
    else:
        return random.choice(responses['fallback'])
    
def handle_price_inquiry(user_message, coinbase_client):
    crypto_currency = user_message.split()[-1]
    price = coinbase_client.get_price(crypto_currency)
    if price:
        return f'The current price of {crypto_currency} is ${price}.'
    else:
        return 'Sorry, I couldn\'t retrieve the price at the moment. Please try again later.'
    