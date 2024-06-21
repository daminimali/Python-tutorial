import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

titanic = pd.read_csv("D:/python/pandas/titanic.csv")

titanic.head()

print(titanic.columns)

plt.figure(figsize=(10, 6))
sns.countplot(x='Survived', data=titanic, palette='viridis')
plt.title('Count of Survivors')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Survived', hue='Sex', data=titanic, palette='viridis')
plt.title('Count of Survivors by Gender')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(titanic['Age'].dropna(), bins=30, kde=True, color='purple')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Pclass', y='Survived', data=titanic, palette='viridis')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Pclass', y='Survived', data=titanic, palette='viridis')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='Survived', y='Age', data=titanic, palette='viridis')
plt.title('Survival Rate by Age')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()
