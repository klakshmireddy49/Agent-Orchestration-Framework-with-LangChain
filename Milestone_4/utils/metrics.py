import time


def calculate_metrics(start):

    end = time.time()

    return {
        "execution_time": round(end - start, 2),
        "agents_used": 5,
        "workflow_status": "Completed",
    }
