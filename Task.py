from DBHandler import *


class Task:
    def __init__(self, title, desc, date, time):
        self.title = title
        self.desc = desc
        self.date = date
        self.time = time

    def __str__(self):
        return (self.title + " : " + self.desc + " : " + self.date + " : " + self.time)


# if __name__ == '__main__':
#    t = Task("Lecture Notes", "Takedown lecture notes for JAVA", "30-05-2022", "07:45:00 AM")
#    db = DBHandler()
#    db.insertTask(t)
#    print(t)
