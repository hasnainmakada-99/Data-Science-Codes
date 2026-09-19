"""Create + execute the two Week-8 notebooks (Program 16 = PCA/2-D Plotly, Program 17 = K-means/3-D Plotly)."""
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from nbclient import NotebookClient
import os, textwrap

OUT_DIR = "/home/user/week8"
os.makedirs(OUT_DIR, exist_ok=True)

RENDERER_SETUP = '''\
import warnings
warnings.filterwarnings("ignore")

# Plotly renderer: interactive figure inside Jupyter + a static PNG copy of every chart
# (the PNG is what GitHub / PDF previews show, because they cannot run interactive Plotly)
try:
    import kaleido  # noqa: F401  (only needed for the static PNG copies)
    pio.renderers.default = "plotly_mimetype+png"
    pio.renderers["png"].width = 900
    pio.renderers["png"].height = 550
    pio.renderers["png"].scale = 2
except ImportError:
    pio.renderers.default = "plotly_mimetype+notebook"
'''

# =====================================================================================
# PROGRAM 16 - PRACTICE PROGRAM - PCA + interactive 2-D scatter
# =====================================================================================
nb16 = new_notebook()
nb16.cells = [
new_markdown_cell(textwrap.dedent('''\
    # Visualizing Clusters with scikit-learn and Plotly

    ## Week 8 Practice Program (Program S. No. 16)

    **Date:** 03/09/2026

    ### Problem Statement
    Perform Principal Component Analysis (PCA) on the Iris dataset and visualize the first two principal
    components using an interactive 2D scatter plot in Plotly.

    ### Dataset
    Built-in Iris dataset from scikit-learn (`sklearn.datasets.load_iris`): 150 samples, 4 numeric features
    (sepal length, sepal width, petal length, petal width in cm) and 3 species (setosa, versicolor, virginica).
    No external dataset URL is required.''')),

new_code_cell(textwrap.dedent('''\
    # Step 1: Import the required libraries
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.io as pio
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA

    ''') + RENDERER_SETUP),

new_code_cell(textwrap.dedent('''\
    # Step 2: Load the Iris dataset into a pandas DataFrame
    iris = load_iris(as_frame=True)

    df = iris.frame.rename(columns={
        "sepal length (cm)": "Sepal Length (cm)",
        "sepal width (cm)": "Sepal Width (cm)",
        "petal length (cm)": "Petal Length (cm)",
        "petal width (cm)": "Petal Width (cm)"
    })
    df["Species"] = df["target"].map(dict(enumerate(iris.target_names)))
    df = df.drop(columns="target")

    feature_columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"]

    df.head(10)''')),

new_code_cell(textwrap.dedent('''\
    # Step 3: Basic verification of the dataset
    print("Dataset Shape:", df.shape)

    print("\\nSpecies Counts:")
    print(df["Species"].value_counts())

    print("\\nDescriptive Statistics:")
    print(df[feature_columns].describe().round(2))''')),

new_code_cell(textwrap.dedent('''\
    # Step 4: Standardize the four features (PCA is sensitive to feature scale)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[feature_columns])

    scaled_df = pd.DataFrame(X_scaled, columns=feature_columns)

    print("Mean of each standardized feature (should be ~0):")
    print(scaled_df.mean().round(3))

    print("\\nStandard deviation of each standardized feature (should be ~1):")
    print(scaled_df.std(ddof=0).round(3))''')),

new_code_cell(textwrap.dedent('''\
    # Step 5: Apply PCA and keep the first two principal components
    pca = PCA(n_components=2, random_state=42)
    principal_components = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame(principal_components, columns=["PC1", "PC2"])
    pca_df["Species"] = df["Species"]

    # keep the original measurements next to the components (used for hover information)
    pca_df = pd.concat([pca_df, df[feature_columns]], axis=1)

    pca_df.head(10)''')),

new_code_cell(textwrap.dedent('''\
    # Step 6: Explained variance and component loadings
    explained = pca.explained_variance_ratio_ * 100

    print("Explained Variance Ratio:")
    print("PC1 :", round(explained[0], 2), "%")
    print("PC2 :", round(explained[1], 2), "%")
    print("Total variance captured by PC1 + PC2 :", round(explained.sum(), 2), "%")

    loadings = pd.DataFrame(
        pca.components_.T,
        columns=["PC1", "PC2"],
        index=feature_columns
    )
    print("\\nComponent Loadings (contribution of each feature):")
    print(loadings.round(3))''')),

new_code_cell(textwrap.dedent('''\
    # Step 7: Interactive 2D scatter plot of PC1 vs PC2 coloured by species
    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        color="Species",
        symbol="Species",
        hover_data={
            "PC1": ":.3f",
            "PC2": ":.3f",
            "Sepal Length (cm)": True,
            "Sepal Width (cm)": True,
            "Petal Length (cm)": True,
            "Petal Width (cm)": True
        },
        title="PCA of the Iris Dataset: First Two Principal Components",
        labels={
            "PC1": f"PC1 ({explained[0]:.2f}% variance)",
            "PC2": f"PC2 ({explained[1]:.2f}% variance)"
        }
    )

    fig.update_traces(marker=dict(size=10, opacity=0.85, line=dict(width=1, color="white")))

    fig.update_layout(
        legend_title_text="Species",
        width=900,
        height=550,
        template="plotly_white"
    )

    fig.show()''')),

new_code_cell(textwrap.dedent('''\
    # Step 8: Scree plot - variance explained by every component (supporting chart)
    pca_full = PCA(n_components=4, random_state=42).fit(X_scaled)

    scree_df = pd.DataFrame({
        "Principal Component": ["PC1", "PC2", "PC3", "PC4"],
        "Explained Variance (%)": (pca_full.explained_variance_ratio_ * 100).round(2)
    })
    scree_df["Cumulative Variance (%)"] = scree_df["Explained Variance (%)"].cumsum().round(2)

    print(scree_df)

    fig_scree = px.bar(
        scree_df,
        x="Principal Component",
        y="Explained Variance (%)",
        text="Explained Variance (%)",
        title="Scree Plot: Variance Explained by Each Principal Component"
    )
    fig_scree.update_traces(textposition="outside")
    fig_scree.update_layout(width=900, height=550, template="plotly_white")

    fig_scree.show()''')),

new_code_cell(textwrap.dedent('''\
    # Step 9: Analyse the clusters in the principal-component space
    centroids = pca_df.groupby("Species")[["PC1", "PC2"]].mean().round(3)
    print("Centroid of each species in PC space:")
    print(centroids)

    spread = pca_df.groupby("Species")[["PC1", "PC2"]].std().round(3)
    print("\\nSpread (standard deviation) of each species in PC space:")
    print(spread)''')),

new_code_cell(textwrap.dedent('''\
    # Step 10: Save the interactive chart, a static image and the PCA dataset
    fig.write_html("program16_pca_scatter.html")
    print("Interactive PCA scatter plot saved as program16_pca_scatter.html")

    try:
        fig.write_image("program16_pca_scatter.png", width=900, height=550, scale=2)
        fig_scree.write_image("program16_scree_plot.png", width=900, height=550, scale=2)
        print("Static images saved as program16_pca_scatter.png and program16_scree_plot.png")
    except Exception as error:
        print("Static image not saved (kaleido not available):", error)

    pca_df.to_csv("program16_iris_pca.csv", index=False)
    print("PCA dataset saved as program16_iris_pca.csv")''')),

new_code_cell(textwrap.dedent('''\
    # Step 11: Summary of the analysis
    print("PCA ANALYSIS SUMMARY")
    print("-" * 45)
    print("Total samples              :", len(pca_df))
    print("Original features          :", len(feature_columns))
    print("Components retained        : 2")
    print("Variance explained by PC1  :", round(explained[0], 2), "%")
    print("Variance explained by PC2  :", round(explained[1], 2), "%")
    print("Total variance retained    :", round(explained.sum(), 2), "%")
    print("Most influential feature   :", loadings["PC1"].abs().idxmax(), "(on PC1)")
    print("Well separated species     : setosa")
    print("Partially overlapping      : versicolor and virginica")''')),
]

# =====================================================================================
# PROGRAM 17 - EXERCISE PROGRAM - K-means + interactive 3-D scatter
# =====================================================================================
nb17 = new_notebook()
nb17.cells = [
new_markdown_cell(textwrap.dedent('''\
    # Visualizing Clusters with scikit-learn and Plotly

    ## Week 8 Exercise Program (Program S. No. 17)

    **Date:** 03/09/2026

    ### Problem Statement
    Perform K-means clustering on the Iris dataset and visualize the clusters using an interactive 3D scatter
    plot in Plotly.

    ### Dataset
    Built-in Iris dataset from scikit-learn (`sklearn.datasets.load_iris`): 150 samples, 4 numeric features
    (sepal length, sepal width, petal length, petal width in cm) and 3 species (setosa, versicolor, virginica).
    No external dataset URL is required.''')),

new_code_cell(textwrap.dedent('''\
    # Step 1: Import the required libraries
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import plotly.io as pio
    from sklearn.datasets import load_iris
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score, adjusted_rand_score

    ''') + RENDERER_SETUP),

new_code_cell(textwrap.dedent('''\
    # Step 2: Load the Iris dataset into a pandas DataFrame
    iris = load_iris(as_frame=True)

    df = iris.frame.rename(columns={
        "sepal length (cm)": "Sepal Length (cm)",
        "sepal width (cm)": "Sepal Width (cm)",
        "petal length (cm)": "Petal Length (cm)",
        "petal width (cm)": "Petal Width (cm)"
    })
    df["Species"] = df["target"].map(dict(enumerate(iris.target_names)))
    df = df.drop(columns="target")

    feature_columns = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"]

    print("Dataset Shape:", df.shape)
    print("\\nSpecies Counts:")
    print(df["Species"].value_counts())

    df.head(10)''')),

new_code_cell(textwrap.dedent('''\
    # Step 3: Standardize the features so that every measurement has equal weight in the distance calculation
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[feature_columns])

    print("Scaled feature matrix shape:", X_scaled.shape)
    print("First 5 scaled rows:")
    print(np.round(X_scaled[:5], 3))''')),

new_code_cell(textwrap.dedent('''\
    # Step 4: Elbow method and silhouette score to choose the number of clusters (k)
    k_values = range(1, 11)
    inertia = []
    silhouette = []

    for k in k_values:
        model = KMeans(n_clusters=k, init="k-means++", n_init=10, random_state=42)
        labels = model.fit_predict(X_scaled)
        inertia.append(model.inertia_)
        silhouette.append(silhouette_score(X_scaled, labels) if k > 1 else np.nan)

    elbow_df = pd.DataFrame({
        "k": list(k_values),
        "Inertia (WCSS)": np.round(inertia, 3),
        "Silhouette Score": np.round(silhouette, 3)
    })
    print(elbow_df.to_string(index=False))

    fig_elbow = px.line(
        elbow_df,
        x="k",
        y="Inertia (WCSS)",
        markers=True,
        title="Elbow Method: Inertia vs Number of Clusters (k)"
    )
    fig_elbow.update_layout(width=900, height=550, template="plotly_white", xaxis=dict(dtick=1))

    fig_elbow.show()''')),

new_code_cell(textwrap.dedent('''\
    # Step 5: Fit K-means with k = 3 (three Iris species) and assign cluster labels
    kmeans = KMeans(n_clusters=3, init="k-means++", n_init=10, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X_scaled)
    df["Cluster"] = "Cluster " + df["Cluster"].astype(str)

    print("Number of iterations to converge:", kmeans.n_iter_)
    print("Final inertia (WCSS):", round(kmeans.inertia_, 3))

    print("\\nCluster Sizes:")
    print(df["Cluster"].value_counts().sort_index())

    df.head(10)''')),

new_code_cell(textwrap.dedent('''\
    # Step 6: Compare the discovered clusters with the actual species
    comparison = pd.crosstab(df["Cluster"], df["Species"])
    print("Cluster vs Species Cross-tabulation:")
    print(comparison)

    sil = silhouette_score(X_scaled, kmeans.labels_)
    ari = adjusted_rand_score(iris.target, kmeans.labels_)

    print("\\nSilhouette Score (k = 3)      :", round(sil, 3))
    print("Adjusted Rand Index vs species:", round(ari, 3))

    # percentage of points whose cluster matches the dominant species of that cluster
    correctly_grouped = comparison.max(axis=1).sum()
    print("Points grouped with their dominant species:", correctly_grouped, "of", len(df),
          "(", round(correctly_grouped / len(df) * 100, 2), "% )")''')),

new_code_cell(textwrap.dedent('''\
    # Step 7: Cluster centres converted back to the original units (cm)
    centers_cm = scaler.inverse_transform(kmeans.cluster_centers_)

    centers_df = pd.DataFrame(centers_cm, columns=feature_columns).round(3)
    centers_df.insert(0, "Cluster", ["Cluster 0", "Cluster 1", "Cluster 2"])

    print("Cluster Centres (original units):")
    print(centers_df.to_string(index=False))''')),

new_code_cell(textwrap.dedent('''\
    # Step 8: Interactive 3D scatter plot of the clusters (with cluster centres marked)
    fig = px.scatter_3d(
        df.sort_values("Cluster"),
        x="Sepal Length (cm)",
        y="Sepal Width (cm)",
        z="Petal Length (cm)",
        color="Cluster",
        symbol="Species",
        hover_data={"Petal Width (cm)": True},
        title="K-means Clustering of the Iris Dataset (k = 3): Interactive 3D View",
        opacity=0.8
    )
    fig.update_traces(marker=dict(size=4))

    # add the three cluster centres as large black diamonds
    fig.add_trace(go.Scatter3d(
        x=centers_df["Sepal Length (cm)"],
        y=centers_df["Sepal Width (cm)"],
        z=centers_df["Petal Length (cm)"],
        mode="markers",
        marker=dict(size=8, color="black", symbol="diamond"),
        hovertext=centers_df["Cluster"] + " centre",
        name="Cluster Centres"
    ))

    fig.update_layout(
        width=900,
        height=650,
        legend_title_text="Cluster / Species",
        margin=dict(l=0, r=0, b=0, t=60),
        scene=dict(
            xaxis_title="Sepal Length (cm)",
            yaxis_title="Sepal Width (cm)",
            zaxis_title="Petal Length (cm)",
            aspectmode="cube",
            camera=dict(eye=dict(x=1.7, y=1.5, z=0.9))
        ),
        template="plotly_white"
    )

    fig.show()''')),

new_code_cell(textwrap.dedent('''\
    # Step 9: Save the interactive chart, static images and the clustered dataset
    fig.write_html("program17_kmeans_3d_scatter.html")
    print("Interactive 3D scatter plot saved as program17_kmeans_3d_scatter.html")

    try:
        fig.write_image("program17_kmeans_3d_scatter.png", width=900, height=650, scale=2)
        fig_elbow.write_image("program17_elbow_plot.png", width=900, height=550, scale=2)
        print("Static images saved as program17_kmeans_3d_scatter.png and program17_elbow_plot.png")
    except Exception as error:
        print("Static image not saved (kaleido not available):", error)

    df.to_csv("program17_iris_kmeans_clusters.csv", index=False)
    print("Clustered dataset saved as program17_iris_kmeans_clusters.csv")''')),

new_code_cell(textwrap.dedent('''\
    # Step 10: Summary of the analysis
    print("K-MEANS CLUSTERING SUMMARY")
    print("-" * 45)
    print("Total samples               :", len(df))
    print("Features used               :", len(feature_columns), "(standardized)")
    print("Number of clusters (k)      : 3")
    print("Cluster sizes               :", df["Cluster"].value_counts().sort_index().tolist())
    print("Silhouette score            :", round(sil, 3))
    print("Adjusted Rand Index         :", round(ari, 3))
    print("Agreement with species      :", round(correctly_grouped / len(df) * 100, 2), "%")
    print("Perfectly separated species : setosa")
    print("Overlapping species         : versicolor and virginica")''')),
]

META = {
    "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}
for nb, name in ((nb16, "Week-8-PP-Program16-PCA.ipynb"), (nb17, "Week-8-EP-Program17-KMeans.ipynb")):
    nb.metadata.update(META)
    path = os.path.join(OUT_DIR, name)
    client = NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": OUT_DIR}})
    client.execute()
    nbformat.write(nb, path)
    print("executed + saved:", path)
