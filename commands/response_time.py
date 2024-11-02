import time

def test_response_time(line, chat_id):
    start_time = time.time()
    line.sendMessage(chat_id, "Testing response time...")
    end_time = time.time()

    
    response_time = end_time - start_time
    line.sendMessage(chat_id, f"Response time: {response_time:.4f} seconds.")