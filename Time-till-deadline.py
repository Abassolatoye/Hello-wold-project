from datetime import datetime

My_goal = input('enter your goal with a deadline separated by a colon? ')
My_goal_list = My_goal.split(' : ')

goal = My_goal_list[0]
Deadline = My_goal_list[1]

Deadline_date = datetime.strptime(Deadline, '%d-%m-%Y')
Today_date = datetime.today()
Time_remain = Deadline_date - Today_date




print(f'Dear user! Time remaining for {goal} is {Time_remain.days} days')
