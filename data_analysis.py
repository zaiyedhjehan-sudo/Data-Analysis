import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_data.csv")

# Display the dataset
print("Student Dataset")
print(df)

# Calculate average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nAverage Marks")
print(df[["Name", "Average"]])

# Find the top student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Student")
print(top_student)

# Display summary statistics
print("\nSummary Statistics")
print(df.describe())

# Create a bar chart
plt.bar(df["Name"], df["Average"])

plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.show()