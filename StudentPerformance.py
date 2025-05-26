import pandas as pd
from ucimlrepo import fetch_ucirepo

# This data approach student achievement in secondary education of two Portuguese schools.
# collected by using school reports and questionnaires.
# fetch dataset
student_performance = fetch_ucirepo(id=320)

# data (as pandas dataframes)
X = student_performance.data.features
y = student_performance.data.targets

# metadata
print(student_performance.metadata)

df = pd.read_csv('https://archive.ics.uci.edu/static/public/320/data.csv')
print(df.info())