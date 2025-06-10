from difflib import SequenceMatcher

def skill_match_score(required, actual):
    """
    Computes similarity-based skill match score between required and actual skills.
    A skill is considered matched if similarity > 0.7
    """
    match_count = 0
    for req in required:
        for act in actual:
            similarity = SequenceMatcher(None, req.lower(), act.lower()).ratio()
            if similarity >= 0.7:
                match_count += 1
                break  # Avoid double-counting
    return match_count / len(required) if required else 0
