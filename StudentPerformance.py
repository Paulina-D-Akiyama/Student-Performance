import pandas as pd
from ucimlrepo import fetch_ucirepo

# This data approach student achievement in secondary education of two Portuguese schools.
# collected by using school reports and questionnaires.
# fetch dataset
student_performance = fetch_ucirepo(id=320)

# data (as pandas dataframes)
X = student_performance.data.features
y = student_performance.data.targets

df = pd.read_csv('https://archive.ics.uci.edu/static/public/320/data.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

students = df.copy()

categorical_columns = [
    'school','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob',
    'reason','guardian','failures','famrel','freetime','goout','Dalc','Walc','health'
]
bool_columns = [
    'schoolsup','famsup','paid','activities','nursery','higher','internet','romantic'
]
small_int_columns = [
    'age','traveltime','studytime','absences','G1','G2','G3'
]

students[categorical_columns] = students[categorical_columns].astype('category')
students[bool_columns] = students[bool_columns].astype('bool')
students[small_int_columns] = students[small_int_columns].astype('int32')

students.rename(columns={
    'famsize':'fam_size','Pstatus':'parent_cohabit' ,'Medu':'mother_ed',
    'Fedu':'father_ed','Mjob':'mother_job','Fjob':'father_job','failures':'class_failures',
    'schoolsup':'school_sup','famsup':'fam_sup','paid':'extra_paid','higher':'wants_uni',
    'famrel':'fam_relationship','goout':'go_out','Dalc':'daily_alc','Walc':'weekend_alc',
    'traveltime':'travel_time','studytime':'study_time','freetime':'free_time'
}, inplace=True)

students['school'] = students['school'].cat.rename_categories({
    'GP':'Gabriel Pereira','MS':'Mousinho da Silveira'
})
students['address'] = students['address'].cat.rename_categories({
    'U':'urban','R':'rural'
})
students['parent_cohabit'] = students['parent_cohabit'].cat.rename_categories({
    'T':'together','A':'apart'
})
#Old size: 642.66 KB
#New size: 38.81 KB
#94% decrease
print(students.info())



