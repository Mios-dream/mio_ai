import fastgpt_chat_api
import audio


history = []
while True:
    user_input = input("阁下：")

    response = fastgpt_chat_api.chat_fastapi(user_input, history=history)

    history.append({"content": user_input, "role": "user"})

    print("澪：", response)
    audio.tts_text(response)
