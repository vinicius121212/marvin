import openai
from elevenlabs import set_api_key, generate, play


set_api_key("fdb4541ae79a92251b8235bba10a2173")


# Set your OpenAI API key
openai.api_key_path = "c:\marvin\APIKEY.txt"

def openai_chat(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ""}
        ]
    )

    return completion.choices[0].message['content']

def load_system_content(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():
    system_content = load_system_content("c:\marvin\prompt.txt")
    chat_history = system_content

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chat ended.")
            break
        
        chat_history += "\nYou: " + user_input
        response_text = openai_chat(chat_history)
        chat_history += "\nAI: " + response_text
        print("AI:", response_text)
        
         # Get the assistant's reply
        reply = response_text
        audio = generate(
        text= str(reply),
        voice="marvin",
        model='eleven_multilingual_v1'
        )
        
        play(audio)
        

if __name__ == "__main__":
    main()
