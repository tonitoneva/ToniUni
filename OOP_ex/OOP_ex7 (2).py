class Programmer:

    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills
        self.previous_language = 0
    def watch_course(self, course_name, new_language, skills_earned):
        if self.language == new_language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name} "
        else:
            return f"{self.name} does not know {new_language}"

    def change_language(self, new_new_language, skills_needed):
        if self.skills >= skills_needed and new_new_language != self.language:
            self.previous_language = self.language
            self.language = new_new_language
            return f"{self.name} switched from {self.previous_language} to {new_new_language}"
        elif self.skills >= skills_needed and new_new_language == self.language:
            return f"{self.name} already knows {self.language}"
        else:
            skills_needed -= self.skills
            return f"{self.name} needs {skills_needed} more skills"

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))



