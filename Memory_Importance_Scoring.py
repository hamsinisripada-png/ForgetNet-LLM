def importance_score(memory):
    return (
        memory.recency * 0.3 +
        memory.frequency * 0.4 +
        memory.user_emphasis * 0.3
    )
