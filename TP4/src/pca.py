import numpy as np
import pandas as pd
import seaborn as sns
from adjustText import adjust_text
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

from TP4.src.standarize import standardize


def boxplot(data, title):
    name = ['Area', 'GDP', 'Inflation', 'Life Expect', 'Military', 'Pop Growth', 'Unemployment']
    color = [(1, 0.7, 0.7, 0.5),
             (0.7, 1, 0.7, 0.5),
             (0.7, 0.7, 1, 0.5),
             (1, 0.85, 0.5, 0.5),
             (0.5, 1, 1, 0.5),
             (1, 0.5, 1, 0.5),
             (1, 0.9, 0.7, 0.5)]

    plt.figure(figsize=(12, 8))
    box = plt.boxplot(data, patch_artist=True, labels=name)

    for patch, color in zip(box['boxes'], color):
        patch.set_facecolor(color)
    plt.title('Boxplot')
    plt.grid(True, axis='y')

    plt.title(title)
    plt.xticks(rotation=30)

    plt.show()


def pca_per_country(data, countries):
    pca = PCA(n_components=1)
    pca_fitted = pca.fit_transform(np.transpose(data))
    plt.figure(figsize=(15, 15))
    plt.bar(countries, pca_fitted.flatten(), color=(0.7, 0.7, 1, 0.5))
    plt.xticks(rotation=90, fontsize=14)
    plt.title('PC1 Index', fontsize=20)
    plt.ylabel('PC1', fontsize=14)
    plt.grid(axis='y')

    plt.show()


def biplot(data, countries):
    pca = PCA(n_components=2)
    pca_fitted = pca.fit_transform(np.transpose(data))
    print(pca.components_[0])

    pc1 = pca_fitted[:, 0]
    pc2 = pca_fitted[:, 1]

    df = {"pc1": pc1, "pc2": pc2, "country": countries}
    plt.figure(figsize=(15, 15))
    sns.scatterplot(x="pc1", y="pc2", data=df, s=100)
    for i, name in enumerate(['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']):
        plt.arrow(0, 0, pca.components_[0][i], pca.components_[1][i], alpha=0.5)
        plt.text(pca.components_[0][i], pca.components_[1][i], name, ha='center', va='center', fontweight='bold')

    plt.title('PCA Scatter Plot', fontsize=25)
    plt.xlabel('PC1', fontsize=20)
    plt.ylabel('PC2', fontsize=20)
    plt.grid(True)
    texts = []
    for i in range(len(df['country'])):
        texts.append(plt.text(df['pc1'][i], df['pc2'][i], df['country'][i], fontsize=10, color='#336699'))

    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))
    plt.show()


def main():
    csv_data = pd.read_csv('/Users/nicolastordomar/Desktop/SIA-TP-S/TP4/data/europe.csv')
    input_data = csv_data[
        ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values
    countries = csv_data['Country'].values

    boxplot(input_data, 'Boxplot of variables not standardized')

    standarized_data = standardize(input_data)

    boxplot(standarized_data, 'Boxplot of variables standardized')

    pca_per_country(standarized_data, countries)

    biplot(standarized_data, countries)


if __name__ == '__main__':
    main()
