import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA

from .clustering_utils import SEED, cluster_with_kmeans

def preprocess_music_data(data, column):
    """
    Preprocess music data including one-hot encoding and PCA.

    Parameters:
    - data (DataFrame): The input music data.
    - column (str): The column to be one-hot encoded.

    Returns:
    - projection (DataFrame): DataFrame with PCA projection.
    - components (int): Number of principal components retained.
    - var_exp (float): Total explained variance by the retained components.
    """
    try:
        seed_value = SEED()
        
        # One-hot encode the specified column
        ohe = OneHotEncoder(dtype=int)
        ohe_columns = ohe.fit_transform(data[[column]]).toarray()
        data = data.drop(column, axis=1)
        data_dummies_music = pd.concat([data, pd.DataFrame(ohe_columns, columns=ohe.get_feature_names_out([column]))], axis=1)

        # Create a pipeline with two steps: standardization and PCA
        pipeline = Pipeline([
            ('scaler', StandardScaler()),   # Standardization step
            ('PCA', PCA(n_components=0.7, random_state=seed_value))   # PCA step with 70% of explained variance
        ])

        # Apply the pipeline to the preprocessed music data
        music_embedding_pca = pipeline.fit_transform(data_dummies_music.drop(['id','name', 'artists_song'], axis=1))

        # Create a DataFrame with the PCA projection
        projection = pd.DataFrame(data=music_embedding_pca)
        components = pipeline[1].n_components_  # Number of principal components retained
        var_exp = pipeline[1].explained_variance_ratio_.sum()  # Total explained variance
        return projection, components, var_exp 
    except Exception as e:
        print(f"An error occurred during preprocess music data: {e}")
        return None, None, None

def clustering_music_projection(data):
    """
    Cluster music data using K-Means on PCA-projected data.

    Parameters:
    - data (DataFrame): The input music data.

    Returns:
    - projection (DataFrame): DataFrame with clustered PCA projection.
    - components (int): Number of principal components retained.
    - var_exp (float): Total explained variance by the retained components.
    - projection_shape (tuple): Shape of the clustered projection DataFrame.
    """
    try:
        # Step 1: Preprocess the data and apply PCA for dimensionality reduction
        projection, components, var_exp = preprocess_music_data(data, 'artists')
        
        # Step 2: Cluster data using K-Means on PCA-projected data
        _, projection = cluster_with_kmeans(data, projection, n_clusters=50)
        
        # Step 3: Add 'artists' and 'song' columns to the projection DataFrame
        projection['song'] = data['artists_song']
        projection['artists'] = data['artists']
        projection_shape = projection.shape
        return projection, components, var_exp, projection_shape
    except Exception as e:
        print(f"An error occurred during music clustering projection: {e}")
        return None, None, None, None
