def analysis_agent(data):

    lines = data.split(".")

    key_points = []

    for line in lines[:5]:

        if len(line) > 20:

            key_points.append(line.strip())

    return key_points
