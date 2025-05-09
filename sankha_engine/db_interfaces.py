from programs.models import Program
from applicants.models import Applicant
class DBInterface:
    def __init__(self):
        pass

    def get_program(self,program_id):
        try:
            program = Program.objects.get(id=program_id)
            return program
        except:
            return None

    def get_applicant(self, applicant_id):
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            return applicant
        except:
            return None
        
    def get_all_programs(self):
        try:
            programs = Program.objects.all()
            return programs
        except:
            return None