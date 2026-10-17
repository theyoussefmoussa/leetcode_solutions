# 1378. Replace Employee ID With The Unique Identifier

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2ea44f?style=for-the-badge)](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Join](https://img.shields.io/badge/Left_Join-4B8BBE?style=for-the-badge)](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1378-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-311_ms-9B59B6?style=for-the-badge)
![Performance](https://img.shields.io/badge/Beats-87.99%25-3498DB?style=for-the-badge)

</div>

## Problem

Given two DataFrames, `Employees` and `EmployeeUNI`, return the unique ID and name of every employee.

If an employee does not have a unique ID, the `unique_id` column should contain `null`.

**Example:**

```text
Input: Employees

+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+

Input: EmployeeUNI

+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+

Output:

+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
```

## Approach

1. **Left Join:** Merge `Employees` with `EmployeeUNI` using the `id` column and `how='left'` to preserve all employees.
2. **Select Columns:** Return only `unique_id` and `name`.
3. **Handle Missing Values:** The left join automatically assigns missing values (`NaN`) to employees without a matching unique ID.

## Solution

```python
import pandas as pd

def replace_employee_id(
    employees: pd.DataFrame,
    employee_uni: pd.DataFrame
) -> pd.DataFrame:

    merged = pd.merge(
        employees,
        employee_uni,
        on='id',
        how='left'
    )

    return merged[['unique_id', 'name']]
```

## Complexity

- **Time:** O(n + m) average, assuming a hash-based join, where `n` and `m` are the numbers of rows in the two DataFrames.
- **Space:** O(n + m) for the merged result.

## Notes

- `how='left'` preserves every row from the left DataFrame.
- `on='id'` specifies the common column used to match employees.
- `pd.merge()` returns a DataFrame containing the matched columns.
- Selecting columns with double brackets (`[['unique_id', 'name']]`) returns a DataFrame rather than a Series.
- Missing unique IDs remain missing in the Pandas result and are represented as `null` in the expected output.