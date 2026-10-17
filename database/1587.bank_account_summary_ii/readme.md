# 1587. Bank Account Summary II

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2ea44f?style=for-the-badge)](https://leetcode.com/problems/bank-account-summary-ii/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1587-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/bank-account-summary-ii/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-373_ms-9B59B6?style=for-the-badge)
![Performance](https://img.shields.io/badge/Beats-21.95%25-3498DB?style=for-the-badge)

</div>

## Problem

Given the `Users` and `Transactions` DataFrames, calculate each user's bank account balance by summing all transaction amounts for that account.

Return the names and balances of users whose balance is **strictly greater than 10,000**. The result can be returned in any order.

## Approach

1. **Left Join:** Merge `users` with `transactions` using `account` to retain all users.
2. **Group and Sum:** Group by `account` and `name`, then use `sum()` to calculate each account's balance.
3. **Rename Column:** Rename `amount` to `balance`.
4. **Filter:** Keep only accounts with a balance greater than `10,000`.
5. **Select Columns:** Return only `name` and `balance`.

## Solution

```python
import pandas as pd


def account_summary(
    users: pd.DataFrame,
    transactions: pd.DataFrame
) -> pd.DataFrame:
    df = users.merge(transactions, on='account', how='left')

    acc_trans = (
        df.groupby(['account', 'name'], as_index=False)['amount']
        .sum()
        .rename(columns={'amount': 'balance'})
    )

    acc_trans = acc_trans[acc_trans['balance'] > 10000]

    return acc_trans[['name', 'balance']]
```

## Example Output

| name | balance |
|---|---:|
| Alice | 11000 |

## Complexity

Let \(n\) be the number of users and \(m\) the number of transactions.

- **Time:** Approximately \(O(n + m)\) for the join and grouping, on average.
- **Space:** \(O(n + m)\) for the merged DataFrame and intermediate results.

## Key Pandas Concepts

- `merge()` combines users with their transactions.
- `groupby()` groups transactions by account.
- `sum()` calculates the total balance.
- `rename()` changes the aggregated column name.
- Boolean filtering selects balances greater than `10000`.