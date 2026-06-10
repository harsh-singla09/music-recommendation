from sklearn.cluster import KMeans

import numpy as np

def SEED():
    SEED = 42
    np.random.seed(SEED)
    return SEED

seed_value = SEED()

def cluster_with_kmeans(data, projection, n_clusters=5):
    """
    Cluster data using K-Means on PCA-projected data.

    Parameters:
    - data (DataFrame): The input data.
    - projection (DataFrame): DataFrame with PCA projection.
    - n_cluster: The number of clusters to form as well as the number of centroids to generate.

    Returns:
    - data (DataFrame): Original data with cluster labels.
    - projection (DataFrame): PCA projection with cluster labels.
    """
    try:
        # Unsupervised method
        kmeans = KMeans(n_clusters=n_clusters, verbose=False, random_state=seed_value, n_init=10)
        kmeans.fit_transform(projection)
        data['cluster_pca'] = kmeans.predict(projection)
        projection['cluster_pca'] = kmeans.predict(projection)
        return data, projection

    except Exception as e:
        print(f"An error occurred during clustering with k_means: {e}")
        return None, None







