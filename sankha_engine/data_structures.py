class ApplicantDS:
    def __init__(self, id, name, grades, program_choice):
        self.id = id
        self.name = name
        self.grades = grades # dictionary
        self.program_choice = program_choice
        self.is_admitted = False
        self.aggregate_score = None

    # linking student data structure with applicant database model

    @classmethod
    def from_applicantModel(cls, applicant):
        """Create a Student instance from an Applicant object"""
        # Extract grades from applicant's subjects (ManyToMany relationship)
        # and convert to dictionary format {subject_name: grade_value}
        
        grades = {grade.subject.name: grade.value for grade in applicant.subjects.all()}

        # get primary applicant program choice (first choice)
        program_choice = applicant.program.first()

        # new student data structure instance
        return cls(
            id=applicant.id,
            name=applicant.name,
            grades=grades,
            program_choice = program_choice
        )

class ProgramDS:

    # constructor 
    def __init__(self, id, name, capacity, subject_requirements):
        self.id = id 
        self.name = name 
        self.capacity = capacity
        self.subject_requirements = subject_requirements # dictionary
        self.admitted_students = []

    def __str__(self):
        return f"Program: {self.name}, Capacity: {self.capacity}, Subject Requirements: {self.subject}"

    # linking program data structure with with program database model

    @classmethod
    def from_programModel(cls, program_model, capacity=None):
        # returns new program data structure instance 

        print(f"Creating Program from model: {program_model}") # debug statement (delete afterwards)

        try:
            # get all subject requirements for this program
            requirements = program_model.subject_requirements.all()
            # convert the requirements to dictionary
            subject_requirements = {req.subject.name: req.max_grade for req in requirements}
            # new program data structure
            return cls(
                id=program_model.id,
                name=program_model.name,
                capacity=capacity if capacity is not None else 0,
                subject_requirements = subject_requirements
            )
        except Exception as e:
            print(f"Error in from_programModel: {e}")
            return None



     