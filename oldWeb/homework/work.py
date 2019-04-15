from course import Course
class Work(Course):

    def __init__(self, course_name, course_code, work_type, completion_status, description, blocked_time):
        super().__init__(self, course_name, course_code, work_type, completion_status)
        self.description = description
        self.blocked_time = blocked_time 

    def __str__(self):
        return super().__str__() + "/n" + self.get_description + "/n" + self.get_blocked_time

    def get_description()
        return self.get_description() 

    def get_blocked_time()
        return self.get_blocked_time
        