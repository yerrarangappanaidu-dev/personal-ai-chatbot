
import ollama

print("Connecting to Gemma 3 1B...")

try:
    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": "Explain what an LLM is in two simple sentences."
            }
        ]
    )

    answer = response["message"]["content"]

    print("\nAI Response:")
    print(answer)

except Exception as error:
    print("\nConnection failed.")
    print("Error:", error)
