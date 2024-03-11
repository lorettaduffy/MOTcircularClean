import pandas as pd
import matplotlib.pyplot as plt

# Initialize a DataFrame with x and y values
df = pd.DataFrame({
    'x': [1,1, 2, 3, 4, 5],
    'y': [2,3, 3, 5, 7, 11]
})

grouped_df = df.groupby(['x']).agg(
    meanY=('y', 'mean'),
    n=('y', 'count')
)
grouped_df = grouped_df.reset_index()

# Plot it using matplotlib
plt.plot(grouped_df['x'], grouped_df['meanY'], marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()