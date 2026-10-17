# 1141. User Activity for the Past 30 Days I

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-2ea44f?style=for-the-badge)](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1141-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-309_ms-9B59B6?style=for-the-badge)
![Performance](https://img.shields.io/badge/Beats-72.88%25-3498DB?style=for-the-badge)

</div>

## Problem

Given the `Activity` DataFrame, find the number of daily active users during the 30-day period ending on **2019-07-27**, inclusive.

A user is considered active on a day if they performed at least one activity on that day. Return the date as `day` and the number of distinct active users as `active_users`.

Days with zero active users should not be included, and the result can be returned in any order.

## Approach

1. **Filter Dates:** Use `between()` to select activities from `2019-06-28` through `2019-07-27`, inclusive.
2. **Group by Day:** Group the filtered records by `activity_date`.
3. **Count Unique Users:** Use `nunique()` to count distinct users for each day, avoiding duplicate counts when a user performs multiple activities.
4. **Rename Columns:** Rename `activity_date` to `day` and `user_id` to `active_users`.

## Solution

```python
import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    filtered = activity[
        activity['activity_date'].between('2019-06-28', '2019-07-27')
    ]

    unique_users = (
        filtered.groupby('activity_date', as_index=False)['user_id']
        .nunique()
        .rename(columns={
            'activity_date': 'day',
            'user_id': 'active_users'
        })
    )

    return unique_users
```

## Example Output

| day | active_users |
|---|---:|
| 2019-07-20 | 2 |
| 2019-07-21 | 2 |

## Complexity

Let \(n\) be the number of rows in the `Activity` DataFrame.

- **Time:** Approximately \(O(n)\) for filtering and grouping, on average.
- **Space:** \(O(n)\) in the worst case for the filtered data and intermediate results.

## Key Pandas Concepts

- `between()` filters values within an inclusive range.
- `groupby()` groups activity records by date.
- `nunique()` counts distinct users and handles duplicate activity rows.
- `rename()` changes column names to match the required output.