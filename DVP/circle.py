import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("1BI22IS31.csv")
x = data["Total"]
y = data["Subject"]

# Calculate the total for the blank wedge
total = sum(x)

# Create new data with a blank wedge
new_x = x.tolist() + [total]
new_y = y.tolist() + [""]

# Assign colors
colors = ['red', 'blue', 'green', 'k']

# Plot the pie chart
plt.figure(figsize=(8, 6), dpi=100)

wedges, labels = plt.pie(new_x,
                        wedgeprops=dict(width=0.4, edgecolor='w'),
                        labels=new_y,
                        colors=colors,
                        startangle=90)  # Adjust start angle if needed

# Get autotexts directly
autotexts = plt.gca().texts

# Customize the blank wedge
wedges[-1].set_color('white')  # Set the color to white
autotexts[-1].set_text("")  # Remove the label

plt.show()
