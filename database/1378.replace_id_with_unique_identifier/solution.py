
import pandas as pd


employees = pd.DataFrame({
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
})

employee_uni = pd.DataFrame({
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
})


def replace_employee_id( employees: pd.DataFrame, employee_uni: pd.DataFrame):
    """
    Steps:
    1. Left join Employees with EmployeeUNI using id.
    2. Keep all employees, including those without a unique ID.
    3. Return unique_id and name.
    """
    merged = pd.merge(
        employees,
        employee_uni,
        on='id',
        how='left'
    )

    return merged[['unique_id', 'name']]
