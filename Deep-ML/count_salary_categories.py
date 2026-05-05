# https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = (accounts['income'] < 20000).sum()
    avg_salary = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_salary = (accounts['income'] > 50000).sum()

    data = [("Low Salary", low_salary), ("Average Salary", avg_salary), ("High Salary", high_salary)]

    df = pd.DataFrame(data, columns=['category', 'accounts_count'])

    return df