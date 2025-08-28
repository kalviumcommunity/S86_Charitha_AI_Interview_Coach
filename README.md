# S86_Charitha_AI_Interview_Coach
# AI Interview Question Generator

## Project Overview
The **AI Interview Question Generator** is an AI-powered tool designed to automatically generate interview questions based on specific job roles or subjects. This project is useful for recruiters who want to save time creating interview questions and for candidates who want to practice and prepare for interviews.

---

## Features
- Generate interview questions for any role or subject dynamically.
- Supports **Zero-Shot, One-Shot, and Multi-Shot prompting** to guide the AI.
- AI explains its reasoning using **Chain of Thought prompting** before generating questions.
- Adjustable **LLM parameters**: Temperature, Top P/K, Stop Sequences.
- Logs **tokens used** to monitor efficiency and cost.
- Structured output for easy readability and copy-paste.

---

## Concepts Covered
This project demonstrates **8 key GenAI concepts**:
1. **Create Project Readme** – Document project idea, setup, and usage.
2. **System and User Prompt** – AI role is defined; user provides role/subject.
3. **Zero-Shot Prompting** – Generate questions without examples.
4. **One-Shot Prompting** – Provide one example to guide AI responses.
5. **Multi-Shot Prompting** – Provide multiple examples for more accurate question generation.
6. **Dynamic Prompting** – Prompts adapt to user input dynamically.
7. **Chain of Thought Prompting** – AI explains reasoning step by step.
8. **Tokens and Tokenization** – Monitor token usage for efficiency and cost.

---

## Tech Stack
- **Backend / AI**: Python, Groq LLM API
- **Frontend / UI**: Streamlit
- **Environment Management**: dotenv for storing API keys

---

## Folder Structure
```

ai\_interview\_generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
└── src/
├── config.py
├── groq\_client.py
└── utils.py

````

---

## Setup and Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd ai_interview_generator
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your **Groq API Key** in a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

5. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## Usage / Sample Inputs

* Enter a job role or subject, e.g., `Software Engineer` or `Data Scientist`.
* Choose **prompt type**: Zero-Shot, One-Shot, Multi-Shot.
* Enable **streaming output** for real-time responses.
* Example roles / subjects:

  * Software Engineer
  * Data Scientist
  * Product Manager
  * Frontend Developer
  * Digital Marketing Specialist

---

## Future Enhancements

* Export questions to PDF or Word.
* Add difficulty levels for questions.
* Integrate embeddings for matching candidate skills.
* Add a web-based dashboard for recruiters.

---

## License

MIT License

