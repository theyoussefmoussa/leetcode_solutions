# 1164. Product Price at a Given Date

<div align="center">

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-FFA116?style=for-the-badge)](https://leetcode.com/problems/product-price-at-a-given-date/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Problem_1164-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/product-price-at-a-given-date/)

</div>

<div align="center">

![Runtime](https://img.shields.io/badge/Runtime-305_ms-9B59B6?style=for-the-badge)
![Performance](https://img.shields.io/badge/Beats-93.53%25-3498DB?style=for-the-badge)

</div>

## Problem

Given the `Products` DataFrame, find the price of every product on **2019-08-16**.

Initially, all products have a price of `10`. Each row records a product's new price and the date it took effect.

Return a DataFrame containing `product_id` and `price`. Products without any price changes on or before the target date must retain the initial price of `10`.

## Approach

1. **Filter by Date:** Keep price changes that occurred on or before `2019-08-16`.
2. **Sort Changes:** Sort by `change_date` so the latest eligible change appears last for each product.
3. **Group by Product:** Group by `product_id` and use `last()` to retrieve each product's most recent price change.
4. **Include All Products:** Reindex the result using all product IDs from the original DataFrame, including products without eligible price changes.
5. **Apply Initial Price:** Fill missing prices with `10`.
6. **Format Output:** Reset the index and rename `new_price` to `price`.

## Solution

```python
import pandas as pd


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    filtered = products[
        products['change_date'] <= '2019-08-16'
    ]

    grouped = (
        filtered.sort_values('change_date')
        .groupby('product_id')
        .last()
    )

    grouped = grouped.reindex(products['product_id'].unique())
    grouped['new_price'] = grouped['new_price'].fillna(10)

    result = grouped[['new_price']].reset_index()
    result.columns = ['product_id', 'price']

    return result
```

## Example Output

| product_id | price |
|---:|---:|
| 2 | 50 |
| 1 | 35 |
| 3 | 10 |

## Complexity

Let \(n\) be the number of rows in the `Products` DataFrame and \(p\) the number of distinct products.

- **Time:** \(O(n \log n)\), dominated by sorting the eligible price changes.
- **Space:** \(O(n + p)\) for the filtered, grouped, and reindexed DataFrames.

## Key Pandas Concepts

- Boolean filtering selects records before a specified date.
- `sort_values()` orders price changes chronologically.
- `groupby().last()` retrieves the last non-null value in each group.
- `reindex()` restores product IDs that have no qualifying changes.
- `fillna(10)` applies the initial price to those products.
- `reset_index()` converts the grouped index back into a column.