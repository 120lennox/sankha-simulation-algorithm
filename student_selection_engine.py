from db_interfaces import DBInterface

class SankhaEngine:
    """
    Engine for calculating student scores and selecting students for programs
    based on their grades and program requirements.
    """
    
    def __init__(self, db_interface=None, programs=None, students=None):
        """
        Initialize the SankhaEngine.
        
        Args:
            db_interface (DBInterface, optional): Interface to the database for fetching/updating data.
            programs (list, optional): List of ProgramDS objects.
            students (list, optional): List of student objects with grades information.
        """
        self.db_interface = db_interface or DBInterface()
        self.programs = programs or []
        self.students = students or []
        
    def load_data(self, programs=None, students=None):
        """
        Load or refresh data from the database if not provided directly.
        
        Args:
            programs (list, optional): List of ProgramDS objects.
            students (list, optional): List of student objects.
        """
        if programs:
            self.programs = programs
        else:
            # This assumes your DBInterface has a method to fetch programs
            self.programs = self.db_interface.get_all_programs()
            
        if students:
            self.students = students
        else:
            # This assumes your DBInterface has a method to fetch students
            self.students = self.db_interface.get_all_students()
            
    def calculate_aggregate_score(self, student, program):
        """
        Calculate the aggregate score for a student applying to a specific program.
        
        Args:
            student: Student object with grades information.
            program: ProgramDS object with subject requirements.
            
        Returns:
            float: The calculated aggregate score.
            None: If the student doesn't meet minimum requirements.
        """
        if not program.subject_requirements:
            return 0
            
        total_score = 0
        total_subjects = len(program.subject_requirements)
        eligible = True
        
        # Iterate through each subject requirement for the program
        for subject_name, min_required_grade in program.subject_requirements.items():
            # Get the student's grade for this subject
            student_grade = self._get_student_grade(student, subject_name)
            
            # Check if student meets minimum requirement for this subject
            if student_grade is None or student_grade < min_required_grade:
                eligible = False
                break
                
            # Add the student's grade to the total score
            total_score += student_grade
        
        # Only calculate aggregate if student meets all minimum requirements
        if eligible and total_subjects > 0:
            return total_score / total_subjects
        else:
            return None  # Student doesn't qualify for this program
    
    def _get_student_grade(self, student, subject_name):
        """
        Helper method to get a student's grade for a specific subject.
        
        Args:
            student: Student object.
            subject_name: Name of the subject.
            
        Returns:
            float or None: The student's grade or None if not found.
        """
        # This implementation depends on how student grades are stored
        # Assuming student has a 'grades' attribute that is a dictionary mapping subject names to grades
        if hasattr(student, 'grades') and subject_name in student.grades:
            return student.grades[subject_name]
        return None
    
    def select_students(self):
        """
        Select students for each program based on their aggregate scores.
        
        Returns:
            dict: A dictionary mapping program IDs to lists of selected student IDs.
        """
        # Dictionary to store calculated scores for each student-program pair
        scores = {}
        
        # Calculate scores for all student-program combinations
        for program in self.programs:
            program_scores = []
            for student in self.students:
                score = self.calculate_aggregate_score(student, program)
                # Only include students who meet the minimum requirements (score is not None)
                if score is not None:
                    program_scores.append((student.id, score))
            
            # Sort by score in descending order
            program_scores.sort(key=lambda x: x[1], reverse=True)
            scores[program.id] = program_scores
        
        # Select top students for each program up to capacity
        selections = {}
        selected_students = set()  # Track selected students across all programs
        
        # First pass: assign students to their top-choice programs
        for program in self.programs:
            program_id = program.id
            selections[program_id] = []
            
            for student_id, score in scores[program_id]:
                # Skip if this student has already been selected for another program
                # or if the program is already at capacity
                if student_id in selected_students or len(selections[program_id]) >= program.capacity:
                    continue
                    
                selections[program_id].append((student_id, score))
                selected_students.add(student_id)
                
                # Update the program's admitted_students list
                program.admitted_students.append(student_id)
        
        return selections
    
    def update_selected_students(self, selections=None):
        """
        Update the database with the selected students for each program.
        
        Args:
            selections (dict, optional): A dictionary mapping program IDs to lists of selected student IDs.
                                        If not provided, uses the last selection result.
        
        Returns:
            bool: True if update was successful, False otherwise.
        """
        if selections is None:
            # Run the selection process if no selections are provided
            selections = self.select_students()
            
        try:
            # Update the database with the selections
            for program_id, selected_students in selections.items():
                # Find the program object
                program = next((p for p in self.programs if p.id == program_id), None)
                if program:
                    # Get just the student IDs (without scores)
                    student_ids = [student_id for student_id, _ in selected_students]
                    # Update the program's admitted_students
                    program.admitted_students = student_ids
                    
                    # Update in database
                    self.db_interface.update_program_admissions(program_id, student_ids)
            
            return True
        except Exception as e:
            print(f"Error updating selected students: {e}")
            return False
