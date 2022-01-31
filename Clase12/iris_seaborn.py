#%%

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
iris_dataset = load_iris()
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
iris_dataframe = iris_dataframe.assign(target = iris_dataset['target'])
iris_dataframe['target'] = iris_dataset['target']
sns.pairplot(data=iris_dataframe,hue='target',diag_kind='hist',diag_kws= {"bins":20, "hue":None, "linewidth":0})
