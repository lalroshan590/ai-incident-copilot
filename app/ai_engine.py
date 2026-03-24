import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def mock_analysis(log_data: str):
    return f"""
[MOCK MODE]

Root Cause:
Likely failure detected based on log: "{log_data}"

Impact:
Service disruption affecting users and dependent services.

Suggested Fix:
- Restart affected service
- Check logs for deeper errors
- Validate dependencies (DB/API)

Prevention:
- Implement monitoring alerts
- Add retry mechanisms
- Improve resource scaling
"""

def analyze_incident(log_data: str):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return mock_analysis(log_data)

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a senior SRE engineer."},
                {"role": "user", "content": f"""
Analyze this incident log:
{log_data}

Provide:
1. Root cause
2. Impact
3. Fix
4. Prevention
"""}
            ],
            temperature=0.3
        )

        return "[AI MODE]\n" + response.choices[0].message.content

    except Exception:
        return mock_analysis(log_data)