import numpy as np

def extract_features(record, peer):
    """
    record: dict (employee data)
    peer: dict (department averages)
    """
    salary_change_pct = (
        (record["salary"] - record["prev_salary"]) /
        max(record["prev_salary"], 1)
    )

    overtime_ratio = record["overtime_hours"] / max(record["total_hours"], 1)

    return np.array([
        salary_change_pct,
        record["salary"] - peer["avg_salary"],
        overtime_ratio,
        record["overtime_hours"] - peer["avg_overtime"]
    ])
