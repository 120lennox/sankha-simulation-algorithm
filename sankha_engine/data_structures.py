class Student:
    def __init__(self, id, name, grades, program_choice):
        self.id = id
        self.name = name
        self.grades = grades # dictionary
        self.program_choice = program_choice
        self.is_admitted = False
        self.aggregate_score = None

    # linking the student data structure with applicant database model

    @classmethod
    def from_applicantModel(cls, applicant):
        """Create a Student instance from an Applicant object"""
        # Extract grades from applicant's subjects (ManyToMany relationship)
        # and convert to dictionary format {subject_name: grade_value}
        
        grades = {grade.subject.name: grade.value for grade in applicant.subjects.all()}

        # get primary applicant program choice (first choice)
        program_choice = applicant.program.first()