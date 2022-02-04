robots_data = input().split(";")
process_time_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split("-")
    process_time_by_robot[name] = int(process_time)
