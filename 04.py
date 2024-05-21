class Schedule:
    def __init__(self):
        self.days = []

    def add_day(self, day):
        self.days.append(day)


class Day:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_class(self, class_instance):
        self.classes.append(class_instance)


class Class:
    def __init__(self, day, start_time, end_time, subject, classroom, teacher):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.subject = subject
        self.classroom = classroom
        self.teacher = teacher


class Subject:
    def __init__(self, number, name, type_name, hours_per_week):
        self.number = number
        self.name = name
        self.type = type_name
        self.hours_per_week = hours_per_week

    def count_hours(self):
        hours_per_week = 0
        hours_per_week += self.hours_per_week

    def __repr__(self):
        return f'{self.name}, {self.type}, {self.hours_per_week}'


class Classroom:
    def __init__(self, room, number, building):
        self.room = room
        self.number = number
        self.building = building

    def __repr__(self):
        return f'Аудитория {self.room}, этаж {self.number}, блок {self.building}'


class Group:
    def __init__(self, name):
        self.name = name
        self.schedule = Schedule()

class Teacher:
    def __init__(self, name):
        self.name = name

def parse_schedule_file(file):
    with open(file, encoding='utf-8') as schdl:
        current_day = None
        current_schedule = Schedule()

        for line in schdl:
            line = line.strip()
            if line in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']:
                current_day = Day(line)
                current_schedule.add_day(current_day)
            else:
                parts = line.split(',')
                class_info = parts[0].split(';')
                class_number = int(class_info[0])
                subject_name = class_info[1]
                class_type = parts[1]
                classroom_info = parts[2].split(': ')[1]
                if classroom_info[0] == 'т':
                    classroom_floor = classroom_info[1]
                    classroom_build = classroom_info[2]
                elif 'спорт' in classroom_info:
                    classroom_floor = 2
                    classroom_build = 'гимнастический зал'
                else:
                    classroom_floor = classroom_info[0]
                    classroom_build = classroom_info[1]
                start_time, end_time = parts[3], parts[4]
                teacher_name = parts[5].split(': ')[1]
                subject = Subject(class_number, subject_name, class_type, 2)
                classroom = Classroom(classroom_info, classroom_floor, classroom_build)
                teacher = Teacher(teacher_name)

                class_instance = Class(current_day, start_time, end_time, subject, classroom, teacher)
                current_day.add_class(class_instance)
    return current_schedule

def print_group_schedule(group):
    print(f"Расписание группы {group.name}:")
    subjects = {}
    for day in group.schedule.days:
        print(day.name)
        for class_instance in day.classes:
            if class_instance.subject.name in subjects:
                if class_instance.subject.type in subjects[class_instance.subject.name]:
                    subjects[class_instance.subject.name][class_instance.subject.type] += 2
                else:
                    subjects[class_instance.subject.name] = {class_instance.subject.type : 2}
            else:
                subjects[class_instance.subject.name] = {class_instance.subject.type : 2}
            print(f"{class_instance.subject.number} пара:\n {class_instance.start_time} -{class_instance.end_time}: "
                  f"{class_instance.subject.name} ({class_instance.subject.type})\n "
                  f" Аудитория {class_instance.classroom.room}, этаж: {class_instance.classroom.number}, "
                  f"блок: {class_instance.classroom.building} \n  "
                  f"Преподаватель: {class_instance.teacher.name}")
    for subject, values in subjects.items():
        for value, time in values.items():
            print(f'Количесвто часов в неделю {subject} ({value}): {time}')

filename = "schedule.txt"
my_group = Group("22704.1")
my_group.schedule = parse_schedule_file(filename)
print_group_schedule(my_group)
