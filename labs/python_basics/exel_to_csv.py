
import pandas as pd

df = pd.read_excel('D:/ML_Pyton_course/ML_Python/project/datasets/ames_datapreprocessing_knime.xlsx', encoding='utf-8', index=False);
df.to_csv('ames_datapreprocessing_knime.csv', encoding='utf-8')