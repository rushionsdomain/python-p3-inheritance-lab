from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Mathematics", "Science", "History"]  # Example knowledge base

    def teach(self):
        return self.knowledge[0]  # Example method to return a subject taught
