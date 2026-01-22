from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HF_API_TOKEN")
)

def analyze_issue_with_ai(issue):
    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant. Return ONLY valid JSON. No explanation."
            },
            {
                "role": "user",
                "content": f"""
Analyze the following GitHub issue and return ONLY valid JSON in this format:

{{
  "summary": "",
  "type": "",
  "priority_score": "",
  "suggested_labels": [],
  "potential_impact": ""
}}

Issue Title:
{issue['title']}

Issue Body:
{issue['body']}

Comments:
{issue['comments']}
"""
            }
        ],
        max_tokens=300,
        temperature=0.3
    )

    return response.choices[0].message["content"]
