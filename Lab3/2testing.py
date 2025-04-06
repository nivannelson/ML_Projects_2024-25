import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create Sample Data
np.random.seed(42)
X = np.array([[2.5, 2.4], 
              [0.5, 0.7], 
              [2.2, 2.9], 
              [1.9, 2.2], 
              [3.1, 3.0], 
              [2.3, 2.7], 
              [2, 1.6], 
              [1, 1.1], 
              [1.5, 1.6], 
              [1.1, 0.9]])

# Step 2: Compute the Mean Vector
mean_vector = np.mean(X, axis=0)

# Step 3: Mean Adjusted Matrix (Centering the data)
X_centered = X - mean_vector

# Step 4: Compute the Covariance Matrix
cov_matrix = np.cov(X_centered.T)

# Step 5: Compute Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 6: Sort Eigenvectors by Eigenvalues (Descending Order)
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Step 7: Choose Top k Eigenvectors (Here k=1 for 1D projection)
k = 1
top_eigenvectors = eigenvectors[:, :k]

# Step 8: Project Data onto the Principal Component
X_pca = X_centered @ top_eigenvectors

# Plotting the original data and the transformed data
plt.scatter(X[:, 0], X[:, 1], label="Original Data")
plt.scatter(X_pca, np.zeros_like(X_pca), label="Projected Data", color="red")
plt.axhline(0, color='black', linestyle='--')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.title("PCA Projection onto First Principal Component")
plt.show()