class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.classes_taught = []

    def add_class(self, class_name):
        self.classes_taught.append(class_name)

    def display_info(self):
        print("Teacher Name:", self.name)
        print("Teacher ID:", self.teacher_id)
        print("Classes Taught:", self.classes_taught)
