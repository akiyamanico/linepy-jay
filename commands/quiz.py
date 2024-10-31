import random
import threading

questions = [
    {"question": "kenapa saya jelek?", "answer": "ya jelek"},
    {"question": "kenapa saya goblok", "answer": "ya goblok"},
    {"question": "ga tau mau isi apa lagi yang penting jalan", "answer": "mager"},
]

current_quiz = None  
quiz_timer = None  

def start_quiz(line, chat_id):
    global current_quiz, quiz_timer
    try:
        if len(questions) < 1:
            line.sendMessage(chat_id, f"ga cukup pertanyaan cuma ada {len(questions)} pertanyaan, next tambahin lah anjg")
            return
        
        question_data = random.choice(questions)
        question = question_data["question"]
        correct_answer = question_data["answer"]

        line.sendMessage(chat_id, f"pertanyaannya : {question}")

        current_quiz = {
            "correct_answer": correct_answer,
            "chat_id": chat_id  
        }

        quiz_timer = threading.Timer(180, stop_quiz, [line])  
        quiz_timer.start()

    except Exception as e:
        line.sendMessage(chat_id, f"lol error: {e}")

def check_answer(line, text):
    global current_quiz, quiz_timer
    try:
        if current_quiz is None:
            return "tidak ada kuis aktif."

        correct_answer = current_quiz["correct_answer"]
        response = text.lower().strip()

        if response == correct_answer:
            line.sendMessage(current_quiz["chat_id"], f"pinter! 🎉 lanjut!")
            start_quiz(line, current_quiz["chat_id"])

    except Exception as e:
        line.sendMessage(current_quiz["chat_id"], f"lol error: {e}")

    return True

def stop_quiz(line, chat_id):
    global current_quiz, quiz_timer
    if quiz_timer is not None:
        quiz_timer.cancel() 
        quiz_timer = None

    if current_quiz is not None:
        current_quiz = None  
