import pandas as pd

visits = pd.DataFrame({
    'visit_id': [1, 2, 4, 5, 6, 7, 8],
    'customer_id': [23, 9, 30, 54, 96, 54, 54]
})

transactions = pd.DataFrame({
    'transaction_id': [2, 3, 9, 12, 13],
    'visit_id': [5, 5, 5, 1, 2],
    'amount': [310, 300, 200, 910, 970]
})



def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame):
    merged = visits.merge(transactions, on='visit_id', how='left')

    result = (
        merged[merged['transaction_id'].isna()]
        .groupby('customer_id')
        .size()
        .reset_index(name='count_no_trans')
    )

    return result
