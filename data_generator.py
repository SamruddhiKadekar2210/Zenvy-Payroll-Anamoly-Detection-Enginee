import pandas as pd
import numpy as np

np.random.seed(42)

data = []
for i in range(1000):
    salary = np.random.normal(50000, 8000)
    overtime = np.random.normal(10, 3)

    if np.random.rand() < 0.02:  # anomalies
        salary *= 2
        overtime *= 3

    data.append({
        "employee_id": i,
        "salary": salary,
        "prev_salary": salary * 0.95,
        "overtime_hours": overtime,
        "total_hours": 160
    })

pd.DataFrame(data).to_csv("data.csv", index=False)
