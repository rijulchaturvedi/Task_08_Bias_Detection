import pandas as pd, os

os.makedirs("results", exist_ok=True)
ground_truth = pd.DataFrame({
    "driver": ["Driver A", "Driver B", "Driver C"],
    "points": [45, 50, 43]
})

ground_truth["validated"] = ground_truth["points"].apply(lambda x: "Accurate" if x > 40 else "Needs Review")
ground_truth.to_csv("results/claim_validation.csv", index=False)

print("Validation report saved → results/claim_validation.csv")
