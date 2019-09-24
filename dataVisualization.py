#Anna Chen
#May 20, 2019
#zyLab 7.7 Ch 7 Program: Data visualization (Python 3)
#Outputs a table and histogram of user-entered data.

#main method
def main():
	title = get_title()
	col1_name, col2_name = get_column_header()
	col1_data, col2_data = get_data()
	print()
	output_table(title, col1_name, col2_name, col1_data, col2_data)
	print()
	output_histogram(col1_data, col2_data)

#Prompts user for the title of their data.
def get_title():
	title = input("Enter a title for the data:\n")
	print("You entered: %s\n" % title)
	return title

#Prompts user for the names of their two column headers for the data.
def get_column_header():
	col1 = input("Enter the column 1 header:\n")
	print("You entered: %s\n" % col1)
	col2 = input("Enter the column 2 header:\n")
	print("You entered: %s\n" % col2)
	return col1, col2

#Prompts user for the data (format must be "String, integer").
def get_data():
	str_data_list = []
	int_data_list = []
	while(True):
		user_in = input("Enter a data point (-1 to stop input):\n")
		if(user_in == '-1'): #if user enters -1, stop getting input (exit the loop)
			break
		if(',' not in user_in): #if no comma, print an error message and continues prompting for input
			print("Error: No comma in string.\n")
			continue
		if(user_in.count(',') > 1): #if comma count > 1, print error message and continues prompting for input
			print("Error: Too many commas in input.\n")
			continue
		
		#Check if input after string is an integer.
		token_list = user_in.split(',')
		token2 = token_list[1].strip() #gets rid of any leading/trailing whitespace to check if it's an integer
		if(not token2.isdigit()): #if not an integer, print error message and continue prompting for input
			print("Error: Comma not followed by an integer.\n")
			continue

		str_token = token_list[0].strip()
		print("Data string: %s" % str_token)
		str_data_list.append(str_token)

		int_token = int(token2)
		print("Data integer: %d\n" % int_token)
		int_data_list.append(int_token)

	return str_data_list, int_data_list

#Outputs the table with the title, column headers, and data.
def output_table(title, col1, col2, data1, data2):
	print('%33s' % title)
	print('%-20s' % col1, end='')
	print('|%23s' % col2)
	print('-'*44)
	for i in range(len(data1)):
		print('%-20s' % data1[i], end='')
		print('|%23s' % data2[i])
	return

#Outputs a histogram of the data.
def output_histogram(data1, data2):
	for i in range(len(data1)):
		print('%20s' % data1[i], end=' ')
		print('*'*data2[i])
	return

if(__name__ == "__main__"):
	main()