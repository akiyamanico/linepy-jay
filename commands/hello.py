def send_hello(line, to):
    try:
        line.sendMessage(to, "Hello World")
    except Exception as e:
        pass
