import pandas as pd
import numpy as np

# Task 11: Create a DataFrame with NaN Values and Highlight NaNs
df_nan = pd.DataFrame(np.random.rand(10, 4))
df_nan.iloc[0, 0] = np.nan
df_nan.iloc[1, 2] = np.nan

# Highlight NaN values
def highlight_nan(x):
    return 'background-color: yellow' if pd.isna(x) else ''

styled_nan_df = df_nan.style.applymap(lambda x: 'background-color: yellow' if pd.isna(x) else '')
print("DataFrame with highlighted NaN values:\n", styled_nan_df)
