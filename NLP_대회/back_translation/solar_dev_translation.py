import pandas as pd
from openai import OpenAI  # Ensure this version is installed: openai==1.2.0

# Initialize the OpenAI client
client = OpenAI(
    api_key="up_q3c3eiLxOGRqwteiJxXqkfJ2C87dX",  # Replace with your actual API key
    base_url="https://api.upstage.ai/v1/solar"
)

# Function to translate text using the solar-1-mini-translate-koen model
def translate_text(text):
    print(text)
    try:
        response = client.chat.completions.create(
            model="solar-1-mini-translate-koen",
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ],
            stream=False  # Set to True if you want to use streaming
        )
        # Return the translated text
        print(response.choices[0].message.content)
        print('----'*16)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error translating text: {e}")
        return None
    
# dev, test csv path여기에요
df = pd.read_csv("/data/ephemeral/home/data/dev.csv")  # Replace "train.csv" with your actual file path
df["translated_dialogue"] = df["dialogue"].apply(translate_text)
# 테스트 데이터시 여기 없애면 됩니다.
df["translated_summary"] = df["summary"].apply(translate_text)
# Save the translations back to a new CSV file
df.to_csv("dev_translated.csv", index=False)  # Saves the new CSV with the translations
print("완료")