'''
Write a program that converts score into grades.
'''

def scrore_to_grade(score):
  if score < 71:
    return "Fail"
  elif score < 81:
    return "Acceptable"
  elif score < 91:
    return "Exceeds Expectations"
  else:
    return "Outstanding"

students_score = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

students_grade = {}

for name in students_score:
  students_grade[name] = scrore_to_grade(students_score[name])
  print(f'{name} got {students_grade[name]}')
