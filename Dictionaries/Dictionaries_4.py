courses = {}
searched_course = None
while True:
    command = input()

    if ":" not in command:
        searched_course = command
        break

    command_arg = command.split(":")
    name = command_arg[0]
    id = command_arg[1]
    course = command_arg[2]

    if course not in courses:
        courses[course] = {}

    courses[course][name] = id

searched_course = searched_course.replace("_", " ")

current_course = courses[searched_course]
for (name, id) in current_course.items():
    print(f"{name} - {id}")

