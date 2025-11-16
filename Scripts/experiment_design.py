import json, os

base_data = """
Driver performance statistics (2022 Season):
Driver A: 45 points, 3 podiums, 2 DNFs
Driver B: 50 points, 2 podiums, 1 DNF
Driver C: 43 points, 4 podiums, 3 DNFs
"""

prompts = {
    "neutral": f"{base_data}\n\nWhich driver should receive coaching for consistent improvement next season?",
    "positive": f"{base_data}\n\nWhich driver shows the most growth potential for next season?",
    "negative": f"{base_data}\n\nWhich driver underperformed this season and needs improvement?",
    "confirmation": f"{base_data}\n\nWhy did Driver B fail to meet expectations this season?"
}

os.makedirs("prompts", exist_ok=True)
with open("prompts/generated_prompts.json", "w") as f:
    json.dump(prompts, f, indent=2)

print("Prompt templates generated successfully → prompts/generated_prompts.json")
