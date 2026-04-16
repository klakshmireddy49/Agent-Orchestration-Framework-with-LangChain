import time
import random


def evaluation_agent(email):

    time.sleep(1)

    return {
        "quality_score": random.randint(85, 98),
        "readability": "High",
        "status": "Approved",
    }
