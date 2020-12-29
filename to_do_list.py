from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///file_name.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'table_name'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user_input = ''
while user_input != '0':

    print('1) Today\'s tasks\n2) Week\'s tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit')

    user_input = input()

    if user_input == '1':
        print()
        today = datetime.today()
        today_date = today.day
        month = today.strftime('%b')
        rows = session.query(Table).filter(Table.deadline == today.date()).all()

        if len(rows) == 0:
            print('Today', today_date, month+':')
            print("Nothing to do!")
        else:
            print('Today', today_date, month + ':')
        for i,task in enumerate(rows):
            print(str(i+1)+'.',task.task)

        print()

    elif user_input == '2':
        today = datetime.today()
        today_date = today.date()
        month = today.strftime('%b')
        seventh_day = today + timedelta(days=6)
        seventh_day_date = seventh_day.date()
        index_of_seventh_day = seventh_day_date.weekday()
        sixth_day = today + timedelta(days=5)
        sixth_day_date = sixth_day.date()
        index_of_sixth_day = sixth_day_date.weekday()
        fifth_day = today + timedelta(days=4)
        fifth_day_date = fifth_day.date()
        index_of_fifth_day = fifth_day_date.weekday()
        fourth_day = today + timedelta(days=3)
        fourth_day_date = fourth_day.date()
        index_of_fourth_day = fourth_day_date.weekday()
        third_day = today + timedelta(days=2)
        third_day_date = third_day.date()
        index_of_third_day = third_day_date.weekday()
        second_day = today + timedelta(days=1)
        second_day_date = second_day.date()
        index_of_second_day = second_day_date.weekday()
        index_of_day = today.weekday()
        days = {'0': 'Monday', '1': 'Tuesday', '2': 'Wednesday', '3': 'Thursday', '4': 'Friday', '5': 'Saturday',
                '6': 'Sunday'}

        day_1 = session.query(Table).filter(Table.deadline == today_date).order_by(Table.deadline).all()
        if len(day_1) == 0:
            print(days['0'], today_date.day, today_date.strftime('%b') + ":")
            print("Nothing to do!")
            print()
        else:
            print(days['0'], today_date.day, today_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_1):
                print(str(i + 1)+".", tasks.task)
            print()

        day_2 = session.query(Table).filter(Table.deadline == second_day_date).order_by(Table.deadline).all()
        if len(day_2) == 0:
            print(days['1'], second_day_date.day, second_day_date.strftime('%b') + ":")
            print("Nothing to do!")
            print()
        else:
            print(days['1'], second_day_date.day, second_day_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_2):
                print(str(i + 1)+".", tasks.task)
            print()

        day_3 = session.query(Table).filter(Table.deadline == third_day_date).order_by(Table.deadline).all()
        if len(day_3) == 0:
            print(days['2'], third_day_date.day, third_day_date.strftime('%b') + ":")
            print("Nothing to do!")
            print()
        else:
            print(days['2'], third_day_date.day, third_day_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_3):
                print(str(i + 1)+".", tasks.task)
            print()

        day_4 = session.query(Table).filter(Table.deadline == fourth_day_date).order_by(Table.deadline).all()
        if len(day_4) == 0:
            print(days['3'], fourth_day_date.day, fourth_day_date.strftime('%b') + ":")
            print("Nothing to do!")
            print()
        else:
            print(days['3'], fourth_day_date.day, fourth_day_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_4):
                print(str(i + 1)+".", tasks.task)
            print()

        day_5 = session.query(Table).filter(Table.deadline == fifth_day_date).order_by(Table.deadline).all()
        if len(day_5) == 0:
            print(days['4'], fifth_day_date.day, fifth_day_date.strftime('%b') + ":")
            print("Nothing to do!")
            print()
        else:
            print(days['4'], fifth_day_date.day, fifth_day_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_5):
                print(str(i + 1)+".", tasks.task)
            print()

        day_6 = session.query(Table).filter(Table.deadline == sixth_day_date).order_by(Table.deadline).all()
        if len(day_6) == 0:
            print(days['5'], sixth_day_date.day, sixth_day_date.strftime('%b') + ":")
            print("Nothing to do!")
            print()
        else:
            print(days['5'], sixth_day_date.day, sixth_day_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_6):
                print(str(i + 1)+".", tasks.task)
            print()
        day_7 = session.query(Table).filter(Table.deadline == seventh_day_date).order_by(Table.deadline).all()
        if len(day_7) == 0:
            print(days['6'], seventh_day_date.day, seventh_day_date.strftime('%b')+":")
            print("Nothing to do!")
            print()
        else:
            print(days['6'], seventh_day_date.day, seventh_day_date.strftime('%b') + ":")
            for i, tasks in enumerate(day_7):
                print(str(i + 1)+".", tasks.task)
            print()

    elif user_input == "5":
        print()
        print("Enter task")
        user = input()
        print("Enter deadline")
        dead_line = input()
        a = datetime.strptime(dead_line, '%Y-%m-%d')
        b = a.date()

        new_row = Table(task=user, deadline=b)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
        print()

    elif user_input == '3':
        today = datetime.today()
        today_date = today.day
        month = today.strftime('%b')
        print('All tasks: ')

        rows = session.query(Table).order_by(Table.deadline).all()
        if rows:
            for i, task in enumerate(rows):
                print('{}. {}. {} {}'.format(i + 1, task, task.deadline.day, task.deadline.strftime('%b')))
        else:
            print('Nothing to do!')
        print()

    elif user_input == '6':
        print()
        today = datetime.today()
        today_date = today.day
        month = today.strftime('%b')
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('No tasks!')
            print()
        else:
            print("Choose the number of the task you want to delete: ")
            for i, task in enumerate(rows):
                print('{}. {}. {} {}'.format(i + 1, task, task.deadline.day, task.deadline.strftime('%b')))

            task_to_delete = int(input())
            specific_task = task_to_delete - 1
            #rows = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
            rows2 = session.query(Table).order_by(Table.deadline).all()
            specific_row = rows2[specific_task]
            session.delete(specific_row)
            session.commit()
            print("The task has been deleted!")
            print()

    elif user_input == '4':
        print()
        print("Missed tasks: ")
        rows = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
        if len(rows) == 0:
            print("Nothing is missed!")
            print()
        else:
            for i, task in enumerate(rows):
                print('{}. {}. {} {}'.format(i + 1, task, task.deadline.day, task.deadline.strftime('%b')))
            print()
print('Bye!')




