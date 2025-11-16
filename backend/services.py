from openai import OpenAI
from secret_key import SECRET 

client= OpenAI(api_key=SECRET)

messages=[]
messages.append({"role":"system", "content":"you are a python developer"})

def chat(user_input):

    # user_input=input("")
    messages.append({"role":"user", "content": user_input})

    response= client.chat.completions.create(model="gpt-5-mini", messages=messages)
    ai_reply=response.choices[0].message.content
    messages.append({"role":"assistant", "content": ai_reply} )

    return ai_reply



















    # client = OpenAI(api_key=SECRET)

    # messages = [{"role": "system", "content": "You are a Java developer"}]

    # while True:
    #     user_input = input("How can I help you? ")
    #     messages.append({"role": "user", "content": user_input})

    #     resp = client.chat.completions.create(model="gpt-3.5-turbo",messages=messages)

    #     reply = resp.choices[0].message.content
    #     messages.append({"role": "assistant", "content": reply})

    #     print(f"ChatGPT says: {reply}")