{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # classroom_data_manager.py\
\
import pandas as pd\
\
class ClassroomDataManager:\
    def __init__(self, students_data):\
        """\
        Initialize with a dataset of student information and their scores.\
        Expected data format: A dictionary with student names and their respective scores in different subjects.\
        """\
        self.data = pd.DataFrame(students_data)\
\
    def generate_report(self):\
        """\
        Generate a class performance report with average scores per subject and overall average.\
        """\
        report = self.data.mean()\
        report['Overall Average'] = self.data.mean(axis=1).mean()\
        return report\
\
    def top_performers(self, subject, n=3):\
        """\
        Get the top 'n' performers in a specific subject.\
        """\
        return self.data.nlargest(n, subject)[[subject]]\
\
    def failing_students(self, passing_score=50):\
        """\
        Identify students failing in one or more subjects, defined by a passing score.\
        """\
        failing = self.data[self.data < passing_score].dropna(how='all')\
        return failing.index.tolist()\
\
    def assign_grades(self):\
        """\
        Assign letter grades based on student performance:\
        - A: 90 and above\
        - B: 80 - 89\
        - C: 70 - 79\
        - D: 60 - 69\
        - F: below 60\
        """\
        grade_map = \{\
            'A': (90, 100),\
            'B': (80, 89),\
            'C': (70, 79),\
            'D': (60, 69),\
            'F': (0, 59)\
        \}\
        \
        def get_grade(score):\
            for grade, (low, high) in grade_map.items():\
                if low <= score <= high:\
                    return grade\
        \
        grades = self.data.applymap(get_grade)\
        return grades\
\
# Sample usage\
if __name__ == "__main__":\
    students_data = \{\
        'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],\
        'Math': [95, 85, 78, 65, 50],\
        'English': [88, 92, 55, 73, 45],\
        'Science': [90, 82, 80, 58, 49]\
    \}\
    \
    # Initialize Classroom Data Manager\
    manager = ClassroomDataManager(students_data)\
\
    print("Class Performance Report:")\
    print(manager.generate_report())\
    \
    print("\\nTop 3 Performers in Math:")\
    print(manager.top_performers('Math', 3))\
\
    print("\\nFailing Students:")\
    print(manager.failing_students())\
\
    print("\\nAssigned Grades:")\
    print(manager.assign_grades())\
}