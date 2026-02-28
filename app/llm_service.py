import os
import logging
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INPUT_COST_PER_1K = 0.00015
OUTPUT_COST_PER_1K = 0.0006


def calculate_cost(usage):
    input_tokens = usage.prompt_tokens
    output_tokens = usage.completion_tokens

    input_cost = (input_tokens / 1000) * INPUT_COST_PER_1K
    output_cost = (output_tokens / 1000) * OUTPUT_COST_PER_1K

    return round(input_cost + output_cost, 6)


def generate_rca(new_log, similar_logs):

    context = "\n\n".join(similar_logs) if similar_logs else "No historical context."

    prompt = f"""
You are an expert QA engineer.

New defect log:
{new_log}

Similar historical defects:
{context}

Provide structured output EXACTLY in this format:

Root Cause:
Impact:
Suggested Fix:

5-Why Analysis:
Why1:
Why2:
Why3:
Why4:
Why5:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert QA engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    usage = response.usage
    cost = calculate_cost(usage)

    logging.info(f"Token usage: {usage}")
    logging.info(f"RCA Cost: ${cost}")

    return response.choices[0].message.content, cost