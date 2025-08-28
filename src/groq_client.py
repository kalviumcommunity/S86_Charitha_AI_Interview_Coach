# src/groq_client.py
from groq import Groq
from src.config import GROQ_API_KEY, DEFAULT_MODEL, DEFAULT_TEMPERATURE, DEFAULT_TOP_P, DEFAULT_MAX_TOKENS, DEFAULT_STOP_SEQUENCE

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


# ---- AI Response ----


def get_ai_response(prompt, stream=False):
    if stream:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=DEFAULT_TEMPERATURE,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            top_p=DEFAULT_TOP_P,
            stream=True,
            stop=DEFAULT_STOP_SEQUENCE
        )
        response_text = ""
        for chunk in completion:
            delta = getattr(chunk.choices[0], "delta", None)
            content = getattr(delta, "content", "")
            if content:
                print(content, end="", flush=True)
                response_text += content
        print()
        return response_text
    else:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=DEFAULT_TEMPERATURE,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            top_p=DEFAULT_TOP_P,
            stop=DEFAULT_STOP_SEQUENCE
        )
        tokens_used = getattr(response.usage, "total_tokens", None)
        if tokens_used:
            print(f"Tokens used: {tokens_used}")
        return response.choices[0].message.content
