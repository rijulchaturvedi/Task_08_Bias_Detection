import json, os
from datetime import datetime

os.makedirs("results", exist_ok=True)
with open("prompts/generated_prompts.json") as f:
    prompts = json.load(f)

results = []
for condition, prompt in prompts.items():
    response = f"[Simulated GPT-4 Output for {condition} framing] - Bias detection placeholder text."
    results.append({
        "condition": condition,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.now().isoformat()
    })

with open("results/mock_llm_responses.json", "w") as f:
    json.dump(results, f, indent=2)

print("Simulated LLM responses saved → results/mock_llm_responses.json")
