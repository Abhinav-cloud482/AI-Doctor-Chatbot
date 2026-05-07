"""
AI Doctor Chatbot (Accurate Rule-Based System)

DISCLAIMER:
This is NOT a doctor.
Always consult a medical professional.
"""

import sys
import pandas as pd

# -----------------------------
# Emergency symptoms
# -----------------------------
EMERGENCY = ["chest pain", "difficulty breathing", "unconscious"]

# -----------------------------
# Load dataset
# -----------------------------
def load_data():
    df = pd.read_csv("symptoms_dataset.csv")

    df["symptoms"] = df["symptoms"].apply(lambda x: x.lower().split())
    df["disease"] = df["disease"].str.lower()
    df["advice"] = df["advice"].str.lower()

    return df

# -----------------------------
# Chatbot Questions
# -----------------------------
QUESTIONS = [
    "What symptoms are you feeling?",
    "Do you have fever?",
    "Do you have pain? Where?",
    "Any nausea or vomiting?",
    "Any breathing issues?",
    "Any other symptoms?"
]

# -----------------------------
# Collect user symptoms
# -----------------------------
def collect_symptoms():
    user_symptoms = []

    print("\n डॉक्टर: I will ask a few questions.\n")

    for q in QUESTIONS:
        try:
            ans = input(f"{q} ").lower().strip()

            if ans:
                user_symptoms.extend(ans.split())

        except KeyboardInterrupt:
            print("\nSession cancelled.")
            return []

    return list(set(user_symptoms))

# -----------------------------
# Match symptoms
# -----------------------------
def diagnose(df, user_symptoms):
    scores = []

    for _, row in df.iterrows():
        disease = row["disease"]
        symptoms = row["symptoms"]

        match_count = len(set(symptoms) & set(user_symptoms))
        score = match_count / len(symptoms)

        scores.append((disease, score, row["advice"]))

    # Sort by score
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return scores[:3]

# -----------------------------
# Main chatbot
# -----------------------------
def main():
    print("\n" + "="*50)
    print("AI Doctor Chatbot")
    print("="*50)
    print("Not medical advice\n")

    df = load_data()

    while True:
        cmd = input("\nType 'start' or 'exit': ").lower().strip()

        if cmd == "exit":
            print("Stay healthy!")
            sys.exit()

        if cmd != "start":
            continue

        user_symptoms = collect_symptoms()

        if not user_symptoms:
            print("No symptoms detected.")
            continue

        # Emergency check
        if any(e in " ".join(user_symptoms) for e in EMERGENCY):
            print("\nEMERGENCY! Go to hospital immediately!\n")
            continue

        results = diagnose(df, user_symptoms)

        print("\n🩺 Possible conditions:\n")

        for disease, score, advice in results:
            print(f"- {disease} ({round(score*100,2)}% match)")
            print(f" Advice: {advice}\n")

        print("Always consult a real doctor.\n")

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    main()
