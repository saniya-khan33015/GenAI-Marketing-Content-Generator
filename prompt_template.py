def build_prompt(topic, audience, content_type, tone, length, examples):

    prompt = f"""
You are a professional marketing copywriter.

Generate a {length} {content_type} with a {tone} tone.

Topic: {topic}
Audience: {audience}

Use persuasive and engaging marketing language.

Relevant Examples:
{examples}
"""

    return prompt