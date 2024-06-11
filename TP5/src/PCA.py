import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns


from TP5.src.utils import get_letters


def main():
    letters = get_letters()
    pca = PCA(n_components=2)
    pca_fitted = pca.fit_transform(letters)

    pc1 = pca_fitted[:, 0]
    pc2 = pca_fitted[:, 1]
    labels = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
              "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL"]
    df = {"pc1": pc1, "pc2": pc2, "country": labels}
    plt.figure(figsize=(15, 15))
    sns.scatterplot(x="pc1", y="pc2", data=df, s=100)

    plt.title('PCA Scatter Plot', fontsize=25)
    plt.xlabel('PC1', fontsize=20)
    plt.ylabel('PC2', fontsize=20)
    plt.grid(True)
    texts = []
    for i in range(len(df['country'])):
        texts.append(plt.text(df['pc1'][i], df['pc2'][i], df['country'][i], fontsize=30, color='#336699'))

    # adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))
    plt.show()

if __name__ == '__main__':
    main()