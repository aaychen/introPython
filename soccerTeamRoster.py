#Anna Chen
#May 17, 2019
#zyLab 8.17 Ch 8 Program: Soccer team roster (Dictionaries)
#Prompts user for soccer team roster's jersey numbers and ratings and allows user to choose
#what they would like to do with the team roster.

def main(): #"main" method
	roster_dict, jersey_list = get_roster() #calls get_roster() function and unpacks returned values into roster_dict, jersey_list
	print_roster(roster_dict) #calls print_roster() and passes roster_dict as an argument
	menu_options(roster_dict, jersey_list) #calls menu_options and passes roster_dict, jersey_list as arguments

#Prompts user to enter jersey number and associated rating and stores them into a dictionary
def get_roster():
	player_dict = {} #dictionary to store jersey numbers (keys) and ratings (values)
	jersey_list = [] #list to store jersey numbers (dictionary keys) for easy sorting
	for player_num in range(1, 6): #loops 5 times from player_num=1 to player_num=5 inclusive
		jersey_num = int(input("Enter player %d's jersey number:\n" % (player_num))) #prompts user to enter jersey number
		jersey_list.append(jersey_num) #adds the entered jersey number to jersey number lsit
		player_dict[jersey_num] = int(input("Enter player %d's rating:\n" % (player_num))) #prompts user to enter rating associated with previously entered jersey number
		#stores jersey number as key and rating as value in the dictioanry of players
		print()
	#jersey_list = sorted(jersey_list) #get a copy of sorted jersey_list 
	player_dict, jersey_list = sort_players(player_dict, jersey_list) #sort the dictionary of players
	#unpacks returned values to player_dict (sorted dictionary of players), jersey_list (sorted list of jersey numbers)
	return player_dict, jersey_list #returns tuple of player_dict, jersey_list

#Sorts the dictionary of players using the list of jersey numbers
def sort_players(unsorted_dict, jersey_list):
	jersey_list = sorted(jersey_list) #makes copy of jersey_list and sorts jersey_list into ascending order
	ord_player_dict = {} #this will be the sorted player dict
	for jersey_key in jersey_list: #iterates over each jersey number element (ascending order) which will be treated as a key of the dict
		ord_player_dict[jersey_key] = unsorted_dict[jersey_key] #adds jersey numbers (keys) and ratings (values) into new sorted dict from old unsorted dict 
	return ord_player_dict, jersey_list #returns sorted dict of players and jersey_list

#Outputs the soccer team roster with the jersey numbers in ascending order and includes ratings
def print_roster(roster_dict):
	print("ROSTER")
	for jersey_num, rating in roster_dict.items(): #iterates over each item in roster_dict
		print("Jersey number: %d, Rating: %d" % (jersey_num, rating)) #prints jersey number and rating associated with it
	print() #prints extra line
	return #return to where function was called and continue executing rest of program

#Outputs a menu of options the user can choose from and executes chosen option
def menu_options(roster_dict, jersey_list):
	while(True): #infinite loop until user chooses to quit
		print("MENU\n"
			"a - Add player\n"
			"d - Remove player\n"
			"u - Update player rating\n"
			"r - Output players above a rating\n"
			"o - Output roster\n"
			"q - Quit\n")
		option = input("Choose an option:\n") #prompts user to choose an option
		if(option=='q'): #if user chooses to quit, exit the loop
			break
		if(option=='o'): #if choose 'o', output the roster
			print_roster(roster_dict) #calls print_roster() function and passes roster_dict as argument
		elif(option=='a'): #if choose 'a', add a player
			roster_dict, jersey_list = add_player(roster_dict, jersey_list) #calls add_player() and passes roster_dict, jersey_list as arguments
			#assignments to roster_dict, jersey_list are the updated ones from adding a player
		elif(option=='d'): #if choose 'd', delete a player
			roster_dict, jersey_list = delete_player(roster_dict, jersey_list) #calls delete_player() and passes roster_dict, jersey_list as arguments
			#assignments to roster_dict, jersey_list will be new ones from deleting a player
		elif(option=='u'): #if choose 'u', update the player's rating
			roster_dict = update_rating(roster_dict) #calls update_rating() function and passes roster_dict as argument
			#assignment to roster_dict will be updated roster_dict (with new rating)
		elif(option=='r'): #if choose 'r', outputs players with ratings above some specified number
			above_rating(roster_dict) #call above_rating() function and passes roster_dict as argument
	return

#Adds a new player (jersey number and rating) to the data
def add_player(roster_dict, jersey_list):
	new_jnum = int(input("Enter a new player's jersey number:\n")) #prompts for jersey number of player to add
	jersey_list.append(new_jnum) #adds entered jersey number to jersey_list
	#jersey_list will be unsorted at this point
	roster_dict[new_jnum] = int(input("Enter the player's rating:\n")) #adds entered rating (associated with entered jersey number) into roster_dict
	#roster_dict will be unsorted at this point
	roster_dict, jersey_list = sort_players(roster_dict, jersey_list) #sort roster_dict and jersey_list and assign them as the newly sorted ones
	return roster_dict, jersey_list #returns newly sorted roster_dict, jersey_list for use later on

#Deletes a player from the data (jersey number and rating)
def delete_player(roster_dict, jersey_list):
	jnum = int(input("Enter a jersey number:\n")) #prompts for jersey number of player to delete
	jersey_list.remove(jnum) #removes the entered jersey number from jersey_list
	del roster_dict[jnum] #removes the entered jersey number and its associated rating from roster_dict
	#jersey_list and roster_dict already sorted, so no need to sort again
	return roster_dict, jersey_list #returns new versions of roster_dict, jersey_list

#Updates the rating a specified player
def update_rating(roster_dict):
	jnum = int(input("Enter a jersey number:\n")) #prompts for jersey number of player to update the rating for
	roster_dict[jnum] = int(input("Enter a new rating for player:\n")) #prompts for new rating of player and updates roster_dict
	#jersey_list and roster_dict already sorted, just updating (no need to sort again)
	return roster_dict #returns roster_dict with updated rating

#Outputs the players with ratings above a specified number
def above_rating(roster_dict):
	req = int(input("Enter a rating:\n")) #prompts for minimum rating requirement (will not inclusive)
	print("ABOVE", req)
	for jnum, rating in roster_dict.items(): #iterates over each item in roster_dict
		if(rating > req): #if the player's rating is greater than the minimum rating, output the player's jersey number and rating
			print("Jersey number: %d, Rating: %d" % (jnum, rating))
	return

if(__name__ == "__main__"): #call main function if this script is directly passed to the interpreter
	main()