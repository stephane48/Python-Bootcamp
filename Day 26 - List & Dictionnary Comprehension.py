#List comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]

#Dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
student_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:score for (student, score) in student_scores.items() if score > 50}