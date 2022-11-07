import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

students_df = pandas.DataFrame(student_dict)
for index, row in students_df.iterrows():
    print(row.student)
