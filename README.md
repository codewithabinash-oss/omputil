# OMPUtil

A simple Python utility library developed by OMP (Optimal Matrix Platform).

## Features

- Calculator
- Password Generator
- QR Code Generator
- Text Utilities
- Timer
- AI-Powered Interview Question Generator
- AI Interview Answer Evaluation
- Mock Interview Sessions

## Installation

```bash
pip install omputil
```

## Requirements

For AI Interview features:

```bash
pip install ollama
```

Install and run Ollama:

```bash
ollama serve
```

Pull a model:

```bash
ollama pull qwen3
```

---

## Usage

### Calculator

```python
from omputils import add

print(add(5, 3))
```

Output:

```text
8
```

---

### Password Generator

```python
from omputils import generate_password

print(generate_password(12))
```

---

### Text Utilities

```python
from omputils import reverse_text

print(reverse_text("OMP"))
```

Output:

```text
PMO
```

---

### QR Code Generator

```python
from omputils.qr import create_qr

create_qr("https://github.com")
```

---

## AI Interview Module

### Generate Interview Question

```python
from omputils.interview import generate

question = generate(
    topic="Python",
    difficulty="medium"
)

print(question)
```

Example Output:

```text
What is the difference between a list and a tuple in Python?
```

---

### Generate Question with Answer

```python
from omputils.interview import generate

result = generate(
    topic="SQL",
    difficulty="hard",
    answer=True
)

print(result)
```

---

### Mock Interview

```python
from omputils.interview import mock_interview

print(
    mock_interview(
        topic="Java",
        count=5
    )
)
```

---

### Evaluate Candidate Answer

```python
from omputils.interview import evaluate_answer

feedback = evaluate_answer(
    question="What is a Python dictionary?",
    user_answer="""
A dictionary stores data in key-value pairs.
Keys are unique.
"""
)

print(feedback)
```

Example Output:

```text
Score: 8/10

Strengths:
- Correctly identified key-value structure.
- Mentioned unique keys.

Weaknesses:
- Did not explain mutability.
- Missing common methods.

Ideal Answer:
A dictionary is a mutable data structure...

Follow-Up Question:
How is a dictionary implemented internally?
```

---

## Section_G Information Utility

Retrieve student information instantly using roll numbers.

from omputils.sec import info

info(40)

Output:

Student Details
---------------
Name  : Abinash
RegNo : 250301370040

Another example:


Invalid roll number:

info(100)

Output:

Student not found.



## Roadmap

Upcoming Features:

- Project Roadmap Generator
- Attendance Calculator
- CGPA Calculator
- Resume Builder
- Team Name Generator
- Hackathon Idea Generator
- Learning Path Generator

---

## Developed By

**OMP — Optimal Matrix Platform**

Building the Future, Optimally.
