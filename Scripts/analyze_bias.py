import json, os
from textblob import TextBlob
import pandas as pd

os.makedirs("results", exist_ok=True)
with open("results/mock_llm_responses.json") as f:
    data = json.load(f)

records = []
for entry in data:
    sentiment = TextBlob(entry["response"]).sentiment.polarity
    records.append({
        "condition": entry["condition"],
        "sentiment": sentiment,
        "word_count": len(entry["response"].split())
    })

df = pd.DataFrame(records)
df.to_csv("results/sentiment_summary.csv", index=False)
print("Sentiment analysis completed → results/sentiment_summary.csv")
