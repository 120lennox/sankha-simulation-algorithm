# short notes and example code snippets

## data structure usages 
1. Student data structure 
    ```python
    # Example usage
    def get_student_from_applicant(applicant_id):
        try:
            applicant = Applicant.objects.get(id=applicant_id)
            student = Student.from_applicant(applicant)
            return student
        except Applicant.DoesNotExist:
            return None

    # Or to convert multiple applicants
    def get_all_students():
        applicants = Applicant.objects.all()
        students = [Student.from_applicant(applicant) for applicant in applicants]
        return students

