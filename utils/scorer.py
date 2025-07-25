def score_document(clauses):
    score = 100
    issues = []

    if not clauses.get("Termination"):
        score -= 20
        issues.append("Missing Termination clause.")
    if not clauses.get("Confidentiality"):
        score -= 20
        issues.append("Missing Confidentiality clause.")
    if not clauses.get("Liability"):
        score -= 20
        issues.append("Missing Liability clause.")

    return max(score, 0), issues
