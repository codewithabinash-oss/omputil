import ollama


def generate(
    topic="Python",
    difficulty="medium",
    answer=False,
    model="qwen2.5-coder:7b"
):
    """
    Generate an interview question using Ollama.

    Parameters:
        topic (str): Subject (Python, Java, SQL, DSA, etc.)
        difficulty (str): easy, medium, hard
        answer (bool): Include answer or not
        model (str): Ollama model name

    Returns:
        str
    """

    prompt = f"""
    Generate ONE {difficulty} level interview question on {topic}.

    {'Also provide a concise answer.' if answer else 'Only provide the question.'}

    Format:
    Question: ...
    """

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def mock_interview(
    topic="Python",
    count=5,
    difficulty="medium",
    model="qwen2.5-coder:7b"
):
    """
    Generate multiple interview questions.
    """

    prompt = f"""
    Generate {count} {difficulty} interview questions on {topic}.

    Number them properly.
    """

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def daily_question(
    topic="Python",
    model="qwen2.5-coder:7b"
):
    """
    Generate one daily interview question.
    """

    prompt = f"""
    Generate one unique interview question on {topic}.
    Do not repeat common beginner questions.
    """

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

