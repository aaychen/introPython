#Anna Chen
#June 2, 2019
#zyLab 12.8 Security Threat Analysis
#Reads passed file and stores information into a nested dictionary that holds IP addresses as keys and a sub-dictionary (of username lists and time lists) as values.

'''
def extract_attacks(fname):
	#Extracts all the attackers and attacks from log
	# Indexed by IP, with a list of usernames and times
	attack_dict = {}
	#"Older" way of reading in a file
	infile = open(fname) #open fname for reading, creating file object
	contents_list = infile.readlines() #read infile into a list of strings called contents_list (elements are by line in file)
	infile.close() #finished reading file into contents_list so closing infile
	for line in contents_list:
		tokens_list = line.strip().split() #strip line of file of any leading/trailing whitespace and split line into a list of tokens by whitespace
		ip = tokens_list[-1] #ip address is the last element in tokens_list
		username = tokens_list[-3] #username is the third last element in tokens_list
		time = ' '.join(tokens_list[0:3]) #join the 1st, 2nd, 3rd elements of tokens_list (which is the time) as a string
		if(ip not in attack_dict.keys()): #if ip is not a key of attack_dict, create a new entry
			attack_dict[ip] = {'usernames': [username], 'times': [time]}
			continue
		
		#if ip is a key of attack_dict, append username and time to existing lists in attack_dict
		usernames_list = attack_dict[ip]['usernames']
		usernames_list.append(username)
		times_list = attack_dict[ip]['times']
		times_list.append(time)
		attack_dict[ip] = {'usernames': usernames_list, 'times': times_list}
	return attack_dict
'''


def extract_attacks(fname):
	'''Extracts all the attackers and attacks from log'''
	# Indexed by IP, with a list of usernames and times
	attack_dict = {}
	#Modern way of reading in a file
	with open(fname, 'r') as infile: #open fname for reading only, creating a file object called infile
		for line in infile: #iterates over each line in infile
			tokens_list = line.strip().split() #strip line of file of any leading/trailing whitespace and split line into a list of tokens by whitespace
			ip = tokens_list[-1] #ip address is the last element in tokens_list
			username = tokens_list[-3] #username is the third last element in tokens_list
			time = ' '.join(tokens_list[0:3]) #join the first 3 elements of tokens_list (which is the time) as a string
			if(ip not in attack_dict.keys()): #if ip is not a key of attack_dict, create a new entry and continue to the next iteration of the loop
				attack_dict[ip] = {'usernames': [username], 'times': [time]}
				continue

			#if ip is a key of attack_dict, append username and time to existing lists in attack_dict
			attack_dict[ip]['usernames'].append(username)
			attack_dict[ip]['times'].append(time)
	return attack_dict