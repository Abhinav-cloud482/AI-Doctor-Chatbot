# AI-Doctor-Chatbot


## AI Doctor Chatbot (Rule-Based System)

> **Disclaimer:**  
This project is NOT a replacement for a real doctor.  
It is an educational AI simulation tool. Always consult a certified medical professional for any health concerns.


## Overview

The **AI Doctor Chatbot** is a simple rule-based medical assistant that predicts possible diseases based on user-reported symptoms.

It uses a predefined dataset (`symptoms_dataset.csv`) and matches user symptoms with known disease patterns to provide:
- Possible disease predictions
- Confidence score (match percentage)
- Basic health advice


## Features

- Rule-based symptom matching algorithm
- Interactive question-based chatbot
- Emergency symptom detection system
- Disease prediction with confidence score
- CSV-based extensible dataset
- Lightweight and fast (no ML model required)


## Project Structure


```
AI-Doctor-Chatbot/
│
├── chatbot.py # Main chatbot script
├── symptoms_dataset.csv # Dataset of diseases & symptoms
├── README.md # Project documentation
```



## How It Works

1. The chatbot asks the user a series of health-related questions.
2. User inputs symptoms in text form.
3. Input is processed and cleaned.
4. Symptoms are matched against dataset entries.
5. Diseases are ranked based on similarity score.
6. Top 3 possible conditions are displayed.

---

## Algorithm

The system uses a simple **set-based similarity approach** :-

```

score = (matching symptoms) / (total symptoms of disease)

```

Results are sorted in descending order of score.


## Emergency Detection

The system immediately warns the user if critical symptoms are detected:

- Chest pain
- Difficulty breathing
- Unconsciousness

If detected :-

```

EMERGENCY! Go to hospital immediately!

```


## 🧪 Example Usage

```

==================================================
👨‍⚕️ AI Doctor Chatbot
==================================================
⚠️ Not medical advice

Type 'start' or 'exit': start

What symptoms are you feeling? fever cough
Do you have fever? yes
Do you have pain? Where? throat
Any nausea or vomiting? no
Any breathing issues? mild
Any other symptoms? tired

Possible conditions :-

- flu (75.0% match)
Advice: rest and drink fluids

- viral infection (62.5% match)
Advice: stay hydrated and monitor symptoms

Always consult a real doctor.

```


## Dataset Format

Your `symptoms_dataset.csv` should look like:

| disease | symptoms | advice |
|--------|----------|--------|
| flu | fever cough cold | rest and fluids |
| malaria | fever chills sweating | consult doctor immediately |


## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-doctor-chatbot.git
cd ai-doctor-chatbot
```

### 2. Install dependencies
```
pip install pandas
```

### 3. Run the chatbot
```
python symptom_checker.py
```


## Requirements

- Python 3.x
- pandas


## Future Improvements
- Integrate Machine Learning / NLP model
- Web-based UI using Flask or Streamlit
- Mobile app version
- Real medical dataset integration
- Medical report generation


## Disclaimer

This project is for educational purposes only.

It does NOT :-

- Replace doctors
- Provide medical diagnosis
- Guarantee accuracy

Always consult a qualified medical professional.


## Author

Abhinav Dixit

Python Developer | Data & ML Enthusiast
