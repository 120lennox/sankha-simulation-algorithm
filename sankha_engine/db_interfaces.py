from programs.models import Program
from applicants.models import Applicant
from subjects.models import Subject
from .data_structures import Applicant, Program

class DBInterface:
    def __init__(self):
        pass

    def get_program(self,program_id):
        try:
            prog = Program.objects.get(id=program_id)
            program = Program.from_programModel(prog)
            return prog
        except:
            return f'failed to get program with id {program_id}'

    def get_applicant(self, applicant_id):
        try:
            applic = Applicant.objects.get(id=applicant_id)

            # create new program in a datastructure
            applicant = Applicant.from_applicantModel(applic)
            return applicant
        except:
            return None
        
    def get_all_programs(self):
        try:
            programs = Program.objects.all()
            return programs
        except:
            return None
    
    def get_all_applicants(self):
        try:
            applicants = Applicant.objects.all()
            return applicants
        except:
            return None
    
    def get_subjects(self, subject_id):
        try:
            subject = Subject.objects.all(id=subject_id)
            return subject
        except:
            return None
    
    def get_all_subjects(self, subject_id):
        try:
            subjects = Subject.objects.all()
            return subjects
        except:
            return None
    
    def get_student(self, student_id):
        pass

    def get_all_students(self):
        pass