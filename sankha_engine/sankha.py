from db_interfaces import DBInterface
class SankhaEngine:
    def __init__(self, db_interface, programs, applicants):
        self.db_interface = DBInterface()
        self.programs = programs or []
        self.applicants = applicants or []

    def load_data(self, programs=None, applicants=None):
        """
        programs: if available in a constructor
        applicants:fetch from ApplicantDS
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
        if not program.subject_requirements:
            return 0
        
        eligible = True
        total_score = 0
        total_grades = len(program.subject_requirements)

        # 
        for subject_name, min_requirement_grade in program.subject_requirements.items():
            student_grade = self._get_student_grade(applicant, subject_name)
            if student_grade is None or student_grade < min_requirement_grade:
                eligible = False
                break

            total_score += student_grade
        
        # student meets all minimum requirements
        if eligible and total_grades > 0:
            return total_score
        
        else:
            return None

    def _get_program_choices(self, applicant):
        # gets specific program choice of an applicant
        if hasattr(applicant, "program"):
            return [applicant.id for program in applicant.program.all()]
        return []

    def select_applicants(self):
        """
        select_applicant: Select applicants for each program based on their aggregate scores   and preferences
        return: dictionary mapping program IDs to student IDs
        NB: an applicant becomes a student once they're enrolled into a program
        """

        applicant_scores = {}

        # 
        for applicant in self.applicants:
            applicant_scores[applicant.id] = []
            program_choices = self._get_program_choices(applicant)

            for program_id in program_choices:
                #
                program = next((p for p in self.programs if p.id == program.id), None)
                if program:
                    score = self.calculate_aggregate_score(applicant, program)
                    if score is not None: #
                        applicant_scores[applicant.id].append((program_id, score))




    def update_selected_students(self):
        pass