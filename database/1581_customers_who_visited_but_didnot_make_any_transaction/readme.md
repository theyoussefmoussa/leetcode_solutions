# 1581. Customer Who Visited but Did Not Make Any Transactions

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2ea44f?style=for-the-badge)](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1581-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-366_ms-9B59B6?style=for-the-badge)
![Performance](https://img.shields.io/badge/Beats-41.96%25-3498DB?style=for-the-badge)

</div>

## Problem

Given the `Visits` and `Transactions` DataFrames, find the customers who visited the mall without making any transactions and count how many times each customer made such visits.

Return a DataFrame containing `customer_id` and `count_no_trans`. The result can be returned in any order.

## Approach

1. **Left Join:** Merge `visits` with `transactions` using `visit_id` and a left join to preserve every visit.
2. **Filter:** Select rows where `transaction_id` is missing (`NaN`), indicating that no transaction occurred during the visit.
3. **Group and Count:** Group the remaining rows by `customer_id` and use `size()` to count each customer's visits without transactions.
4. **Format Output:** Use `reset_index(name='count_no_trans')` to produce the required DataFrame columns.

## Solution

```python
import pandas as pd


def find_customers(
    visits: pd.DataFrame,
    transactions: pd.DataFrame
) -> pd.DataFrame:
    merged = visits.merge(transactions, on='visit_id', how='left')

    result = (
        merged[merged['transaction_id'].isna()]
        .groupby('customer_id')
        .size()
        .reset_index(name='count_no_trans')
    )

    return result
```

## Example Output

| customer_id | count_no_trans |
|---:|---:|
| 54 | 2 |
| 30 | 1 |
| 96 | 1 |

## Complexity

Let \(n\) be the number of visits and \(m\) the number of transactions.

- **Time:** Approximately \(O(n + m)\) for the join and grouping, on average.
- **Space:** \(O(n + m)\) for the merged DataFrame and intermediate results.

## Key Pandas Concepts

- `merge(..., how='left')` preserves all rows from the left DataFrame.
- `isna()` identifies visits without matching transactions.
- `groupby()` groups visits by customer.
- `size()` counts rows in each group.
- `reset_index(name=...)` converts the grouped result into a DataFrame with the required column name.