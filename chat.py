import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="you are a humorous, fun teacher who teaches 10th grade CBSE science. you help in solving doubts while keeping answers to the point, short and consise and not telling other useless information, you are not teaching an enitre class, but only solving the problem of the user"
)

history = []
print("teacher: Hi, I'm your 10th grade CBSE science teacher. How can I help you today?")

while True: 
    
    user_input = input("You: ")

    chat_session = model.start_chat(
        history= history
    )

    response = chat_session.send_message(user_input)
    model_response = response.text

    print(f'teacher: {model_response}')
    print()

    history.append({"role": "user", "parts":[user_input]})
    history.append({"role": "model", "parts":[model_response]})