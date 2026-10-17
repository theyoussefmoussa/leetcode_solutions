# 1484. Group Sold Products By The Date

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2ea44f?style=for-the-badge)](https://leetcode.com/problems/group-sold-products-by-the-date/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![GroupBy](https://img.shields.io/badge/GroupBy-4B8BBE?style=for-the-badge)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1484-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/group-sold-products-by-the-date/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-333_ms-9B59B6?style=for-the-badge)
![Performance](https://img.shields.io/badge/Beats-59.56%25-3498DB?style=for-the-badge)

</div>

## Problem

Given the `Activities` DataFrame containing product names and their sale dates, find the number of distinct products sold on each date and list their names in lexicographical order.

Return the result ordered by `sell_date`.

**Example:**

```text
Input:

+------------+------------+
| sell_date  | product    |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+

Output:

+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-Shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
```

## Approach

1. **Group by Date:** Use `groupby('sell_date')` to process each date separately.
2. **Count Distinct Products:** Use `nunique()` to count each product only once per date.
3. **Sort and Concatenate:** Use `unique()` to remove duplicates, `sorted()` to arrange product names lexicographically, and `','.join()` to combine them into a single string.
4. **Aggregate:** Use `agg()` to calculate both `num_sold` and `products` in one operation.
5. **Reset Index and Sort:** Use `reset_index()` to return a DataFrame and `sort_values()` to order dates.

## Solution

```python
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = (
        activities.groupby('sell_date')['product']
        .agg(
            num_sold='nunique',
            products=lambda x: ','.join(sorted(x.unique()))
        )
        .reset_index()
        .sort_values('sell_date')
    )

    return result
```

## Complexity

Let `n` be the number of rows and `k` the number of distinct products within a date.

- **Time:** Approximately O(n + k log k) per date for grouping, deduplication, and sorting.
- **Space:** O(n) for grouping and intermediate results.

## Notes

- `nunique()` counts distinct values.
- `unique()` returns distinct product names.
- `sorted()` orders the names lexicographically.
- `','.join()` creates the comma-separated string.
- Named aggregation allows multiple output columns to be calculated in a single `agg()` call.