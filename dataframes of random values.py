import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(0)  # For reproducibility
data = np.random.randint(1, 100, size=(10, 4))  # 10 rows and 4 columns with random integers
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Function to set background color to black and font color to yellow
def highlight_cells(val):
    return 'background-color: black; color: yellow'

# Apply the style to the entire DataFrame
styled_df = df.style.applymap(highlight_cells)

# Display the styled DataFrame
styled_df
