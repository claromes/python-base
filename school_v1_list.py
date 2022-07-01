#!/usr/bin/env python3
"""Report of student by activities

Print list of students grouped by class in each activity.
"""

__version__ = "0.1.0"

class_1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
class_2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

act_eng = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
act_music = ["Erik", "Carlos", "Maria"]
act_dance = ["Gustavo", "Sofia", "Joana", "Antonio"]

activities = [
    ("English", act_eng),
    ("Music", act_music),
    ("Dance", act_dance),
]

for activity_name, activity in activities:

    print(f"\nEnrolled students in {activity_name} classes")
    print("." * 10)
    print()
    
    act_class_1 = []
    act_class_2 = []

    for student in activity:
        if student in class_1:
            act_class_1.append(student)
        elif student in class_2:
            act_class_2.append(student)

    print("class 1:", act_class_1)
    print("class 2:", act_class_2)
    print()
    print("_" * 50)