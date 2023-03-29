import os
import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
text_input = ""

while True:

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by Vishnu Prakash. How can I help you today?\nHuman: "+ text_input,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )

    text = response['choices'][0]['text']
    print(text)
    input("Press enter to continue")
    text_input = input("human:")

