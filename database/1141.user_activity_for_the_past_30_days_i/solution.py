import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    filtered = activity[
        activity['activity_date'].between('2019-06-28', '2019-07-27')
    ]

    unique_users = filtered.groupby('activity_date', as_index=False)['user_id'].nunique().rename(columns={'user_id':'active_users', 'activity_date':'day'})

    return unique_users