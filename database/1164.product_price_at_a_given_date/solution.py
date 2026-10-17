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

    # Include all products, even those with no price changes before the date
    grouped = grouped.reindex(products['product_id'].unique())

    # Set the initial price for products with no previous changes
    grouped['new_price'] = grouped['new_price'].fillna(10)

    # Format the result
    result = grouped[['new_price']].reset_index()
    result.columns = ['product_id', 'price']

    return result