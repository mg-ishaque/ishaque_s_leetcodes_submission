import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    distinct_salaries = employee.salary.drop_duplicates()
    sorted_distinct_salaries = distinct_salaries.sort_values(ascending=False)
    
    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    if len(sorted_distinct_salaries) >= N:
        result = sorted_distinct_salaries.iloc[N - 1]
    else:
        result = None
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})