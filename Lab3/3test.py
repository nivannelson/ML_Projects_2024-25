import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = "Lab3\Iris.csv"  # Ensure this file is in your working directory
df = pd.read_csv(file_path)

# Display basic info about dataset
print("First 5 rows of dataset:\n", df.head())

# Step 1: Bar Chart for Species Frequency
plt.figure(figsize=(6, 4))
sns.countplot(x='species', data=df, palette="viridis")
plt.xlabel("Species")
plt.ylabel("Count")
plt.title("Frequency of Species")
plt.show()

# Step 2: PCA for Dimensionality Reduction
# Extracting features
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = df[features]

# Standardizing the Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA (Reducing to 2 Principal Components)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Convert to DataFrame
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['species'] = df['species']

# Scatter Plot for PCA
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PC1', y='PC2', hue='species', data=df_pca, palette="coolwarm", s=80)
plt.title("PCA: Data Distribution on First Two Principal Components")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()

# Step 3: Histograms for Each Attribute
df[features].hist(figsize=(10, 6), bins=20, color='blue', edgecolor='black')
plt.suptitle("Histogram of Each Feature", fontsize=14)
plt.show()
