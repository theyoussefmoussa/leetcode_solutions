import pandas as pd

activities = pd.DataFrame({
    'sell_date': [
        '2020-05-30',
        '2020-06-01',
        '2020-06-02',
        '2020-05-30',
        '2020-06-01',
        '2020-06-02',
        '2020-05-30'
    ],
    'product': [
        'Headphone',
        'Pencil',
        'Mask',
        'Basketball',
        'Bible',
        'Mask',
        'T-Shirt'
    ]
})



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
