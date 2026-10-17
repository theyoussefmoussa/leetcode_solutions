"""
Write a solution to report the name and balance of users with a balance higher than 10000.
The balance of an account is equal to the sum of the amounts of all transactions involving that account.
"""
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        users,
        transactions,
        on='account',
        how='left'
    )

    acc_trans = (
        df.groupby(['account', 'name'], as_index=False)['amount']
        .sum()
        .rename(columns={'amount': 'balance'})
    )

    acc_trans = acc_trans[acc_trans['balance'] > 10000]

    return acc_trans[['name', 'balance']]