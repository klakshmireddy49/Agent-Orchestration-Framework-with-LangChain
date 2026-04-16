import wikipedia
import time


def research_agent(topic):

    time.sleep(1)

    try:

        summary = wikipedia.summary(topic, sentences=6)

        return f"""
Research Topic: {topic}

{summary}
"""

    except:

        return f"No detailed research found for {topic}"
