def categorize_questions(questions):
    categories = {
        "Informational": [],
        "Usage": [],
        "Safety": [],
        "Purchase": [],
        "Comparison": []
    }

    for q in questions:
        ql = q.lower()
        if "what" in ql or "ingredient" in ql:
            categories["Informational"].append(q)
        elif "use" in ql or "apply" in ql:
            categories["Usage"].append(q)
        elif "safe" in ql or "side" in ql:
            categories["Safety"].append(q)
        elif "price" in ql or "buy" in ql:
            categories["Purchase"].append(q)
        else:
            categories["Comparison"].append(q)

    return categories
