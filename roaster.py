# import all modules
from datetime import *
import csv
import argparse
import os


# main class to handle all functions 
class cp_roaster :

	# make complete file for current year
	def make_for_complete_year(self):
		today = date.today()
		current_year = today.year
		teams = self.get_teams_dictionary()
		with open('complete_year_detail.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])
		l=len(teams)-1
		for i in range(1,53):
			d = "{}-W{}-1".format(current_year , str(i).rjust(2,'0'))
			r = datetime.strptime(d , "%Y-W%W-%w")
			contest = r.strftime("%d/%m")
			end = r+ timedelta(days=6)
			end = end.strftime("%d/%m")
			days = contest + " - " + end
			upsolving = r+ timedelta(days=4)
			upsolving = upsolving.strftime("%d/%m")
			find = str(i%l)
			team = teams[find]
			with open('complete_year_detail.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow([i,team,days,contest,upsolving])

	# convert team list in csv into dictionary
	def get_teams_dictionary(self):
		with open('team_list.csv', newline='') as csvfile:
			rows = list(csv.reader(csvfile, delimiter=','))
		d=dict()
		for row in rows:
			d[row[0]]=row[1]
		return d

	# check if members are in same list
	def is_in_same_team(self,member1,member2):
		with open('team_list.csv', newline='') as csvfile:
			rows = list(csv.reader(csvfile, delimiter=','))
		for row in rows :
			team = row[1]
			if team.find(member2)!=-1 and team.find(member1)!=-1:
				return 0
		return 1


	def get_between_particular_weeks(self,w1,w2):
		# handling errors 
		if w1<1 or w2>52 or w1>w2:
			print("wrong")
			return
		with open('complete_year_detail.csv',newline='') as csvfile :
			rows = list(csv.reader(csvfile , delimiter=','))
		with open('between_two_weeks_data.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])	
		for i in range(w1,w2+1):
			with open('between_two_weeks_data.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow(rows[i])
		# open the file in windows 
		os.startfile(r'C:\Users\DELL\Desktop\python_tut\project\cp_roaster\between_two_weeks_data.csv')


	def swap_members_permanently(self ,member1, member2):
		# no need to swap
		if self.is_in_same_team(member1,member2):
			print("wrong")
			return
		# open and save in list 
		with open('complete_year_detail.csv', newline= "") as file:
			rows = list(csv.reader(file , delimiter=','))
		for row in range(1,len(rows)) :
			team = rows[row][1]

			if team.find(member1)!=-1:
				team = team.replace(member1 , member2)
				rows[row][1]=team
				continue
			if team.find(member2)!=-1:
				team = team.replace(member2 , member1)
				rows[row][1]=team
		with open('complete_year_detail.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])
		for i in range(1,len(rows)):
			with open('complete_year_detail.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow(rows[i])	


	# replace name with other name
	def replace_for_sigle_week(self,week,to_replace,replace_with):
		with open('complete_year_detail.csv', newline= "") as file:
			rows = list(csv.reader(file , delimiter=','))
		row = rows[week]
		team = row[1]
		team = team.replace(to_replace , replace_with)
		rows[week][1] = team
		with open('complete_year_detail.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])
		for i in range(1,len(rows)):
			with open('complete_year_detail.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow(rows[i])	

	# change contest date
	def change_contest_date(self,week,day):
		# handling error
		if week<1 or week>52 :
			return 
		with open('complete_year_detail.csv', newline= "") as file:
			rows = list(csv.reader(file , delimiter=','))
		row = rows[week]
		current = row[3]
		current = datetime.strptime(current , "%d/%m")
		current+=timedelta(days=day)
		current = current.strftime("%d/%m")
		rows[week][3]=current
		with open('complete_year_detail.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])
		for i in range(1,len(rows)):
			with open('complete_year_detail.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow(rows[i])	
		print("Date updated successfully !! {}".format(current))


	def change_upsolving_date(Self,week,day):
		if week<1 or week>52 :
			return 
		with open('complete_year_detail.csv', newline= "") as file:
			rows = list(csv.reader(file , delimiter=','))
		row = rows[week]
		current = row[4]
		print("previous date -> {}".format(current))
		current = datetime.strptime(current , "%d/%m")
		current+=timedelta(days=day)
		current = current.strftime("%d/%m")
		rows[week][4]=current
		with open('complete_year_detail.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])
		for i in range(1,len(rows)):
			with open('complete_year_detail.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow(rows[i])
		print("Date updated successfully !! {}".format(current))


	def change_after_current_week(self):
		week = datetime.today().isocalendar()[1]
		with open('complete_year_detail.csv', newline= "") as file:
			rows = list(csv.reader(file , delimiter=','))
		teams = self.get_teams_dictionary()
		l = len(teams) - 1
		today = date.today()
		current_year = today.year
		for i in range(week,53):
			d = "{}-W{}-1".format(current_year , str(i).rjust(2,'0'))
			r = datetime.strptime(d , "%Y-W%W-%w")
			contest = r.strftime("%d/%m")
			end = r+ timedelta(days=6)
			end = end.strftime("%d/%m")
			days = contest + " - " + end
			upsolving = r+ timedelta(days=4)
			upsolving = upsolving.strftime("%d/%m")
			find = str(i%l)
			team = teams[find]
			rows[i] = [i,team,days,contest,upsolving]
		with open('complete_year_detail.csv','w',newline='') as file :
			writer = csv.writer(file)
			writer.writerow(['WEEK','TEAM','DAYS','CONTEST','UPSOLVING'])
		for i in range(1,53):
			with open('complete_year_detail.csv','a+',newline='') as file :
				writer = csv.writer(file)
				writer.writerow(rows[i])
		

	def add_team(self,member1,member2):
		with open('team_list.csv',newline='') as file:
			rows = list(csv.reader(file,delimiter=','))
		l = len(rows)-1
		team = member1 + ' ' + member2
		with open('team_list.csv' , 'a+' , newline='') as file:
			writer =csv.writer(file)
			writer.writerow([l,team])
		self.change_after_current_week()
		print("Team Added successfully !!")

	def show_teams(self):
		os.startfile(r'C:\Users\DELL\Desktop\python_tut\project\cp_roaster\team_list.csv')



# main function call
if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument("--start",type=int,help="starting week")
	parser.add_argument("--end",type=int,help="end week")

	args = parser.parse_args()
	obj = cp_roaster()


	# check if complete year detail exists
	try:
		open(r'C:\Users\DELL\Desktop\python_tut\project\cp_roaster\complete_year_detail.csv')
	except FileNotFoundError :
		obj.make_for_complete_year()


	if args.start!=None and args.end!=None :
		obj.get_between_particular_weeks(args.start , args.end)

	if args.start == None and args.end == None :
		print("-- What do you want to do ?")
		print("1. swap members permanently")
		print("2. swap members for particular week")
		print("3. change contest date ")
		print("4. change upsolving date")
		print("5. get between particular weeks")
		print("6. Add new team")
		print("7. Show teams")

		choice = input('Enter choice')
		if choice=='1':
			member1 = input('Enter member 1 ')
			member2 = input('Enter member 2 ')
			if member1!=member2:
				obj.swap_members_permanently(member1,member2)
				print("Members swapped successfully")

		if choice=='2':
			member1 = input('Enter member 1   ')
			member2 = input('Enter member 2   ')
			week = int(input('Enter week'))
			if member1!=member2:
				obj.replace_for_sigle_week(week,member1,member2)
				print('updated successfully !! ')

		if choice =='3':
			week = int(input('Enter week number  '))
			days = int(input('number of days to shift by --    '))
			obj.change_contest_date(week,days)

		if choice=='4':
			week = int(input('Enter week number  '))
			days = int(input('number of days to shift by --    '))
			obj.change_upsolving_date(week,days)	
			print('updated successfully')
			
		if choice == '5':
			start = int(input("Enter starting week  "))
			end = int(input("Enter ending week  "))
			obj.get_between_particular_weeks(start , end )

		if choice=='6':
			member1 = input('Enter member 1 ')
			member2 = input('Enter member 2 ')
			if member1!=member2:
				obj.add_team(member1,member2)
				print("Team added successfully !! ")

		if choice == '7':
			obj.show_teams()
