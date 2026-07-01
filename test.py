from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
)

print(" AI Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input == "exit":
        print("AI: Goodbye! 👋")
        break

    response = llm.invoke(user_input)

    print(f"AI: {response.content}\n")