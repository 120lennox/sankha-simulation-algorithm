from db_interfaces import DBInterface
class SankhaEngine:
    def __init__(self, db_interface, programs, applicants):
        self.db_interface = DBInterface()
        self.programs = programs or []
        self.applicants = applicants or []

    def load_data(self, programs=None, applicants=None):
        """
        
        """
        if programs:
            self.programs = programs
        else:
            self.programs = self.db_interface.get_all_programs()
        
        if applicants:
            self.applicants = applicants
        else:
            self.applicants = self.db_interface.get_all_applicants()
    
    def _get_student_grade(self, applicant, subject_name):
        """
        applicant: applicant object
        subject_name: subject name

        we use hasattr function to check is applicant model has attribute subjects where we look for grade and subject name
        """
        if hasattr(applicant, 'subjects'):
            return applicant.subjects[subject_name]
        return None

    def calculate_aggregate_score(self, applicant, program):
        pass

    def select_students(self):
        pass

    def update_selected_students(self):
        pass