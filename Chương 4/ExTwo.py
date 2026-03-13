student_scores = {
    "An": 8.5,
    "Bình": 9.0,
    "Châu": 7.5
}

def calculate_average_score(scores_dict):
    if len(scores_dict) == 0:
        return 0
    return sum(scores_dict.values()) / len(scores_dict)
