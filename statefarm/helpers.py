import numpy as np
import pandas as pd 

def create_dummy_df(df, cat_cols, dummy_na):
    for col in  cat_cols:
        try:
            # for each cat add dummy var, drop original column
            df = pd.concat([df.drop(col, axis=1),\
                            pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
        except:
            continue
    return df

def clean_day_x3_col(date):
    if date.lower() == 'tue':
        return 'Tuesday'
    elif date.lower() == 'mon':
        return 'Monday'
    elif date.lower() == 'wed':
        return 'Wednesday'
    elif date.lower() == 'thur':
        return 'Thursday'
    elif date.lower() == 'fri':
        return 'Friday'
    elif date.lower() == 'sat':
        return 'Saturday'
    elif date.lower() == 'sun':
        return 'Sunday'
    else:
        return date