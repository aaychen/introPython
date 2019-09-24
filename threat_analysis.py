#Anna Chen
#June 2, 2019
#zyLab 12.8 Security Threat Analysis
#Models the analysis of real security log files from UC Davis.

from logreader import extract_attacks #import extract_attacks() function from logreader.py

def get_max_attacks(attack_dict):
    '''Returns the attacker with the largest number of usernames.'''
    ip = ''
    usernames_list = []
    max_count = -1
    for key, value in attack_dict.items(): #iterates over each item in attack_dict (key is IP, value is dict of usernames list and times list)
        temp = value['usernames'] #temp value is the attack_dict's current list of usernames (to compare to max)
        if(len(temp) > max_count): #if length of temp list is larger than previous max, save temp as the new max
            ip = key #update IP to IP associated with temp (key is the new IP)
            usernames_list = value['usernames'] #update usernames_list to the list of usernames associated with temp
            max_count = len(usernames_list) #update max_count to length of updated usernames_list
    return ip, usernames_list 


def get_start_time(ip_str, attack_dict):
    '''Given an attacker ip, return the earliest (min) time of attack.'''
    times_list = attack_dict[ip_str]['times'] #save the list of times in attack_dict associated with the IP address
    return min(times_list) #using min() function to find min time and returning that

def get_end_time(ip_str, attack_dict):
    '''Given an attacker ip, return the latest (max) time of attack.'''
    times_list = attack_dict[ip_str]['times'] #save the list of times in attack_dict associated with the IP address
    return max(times_list) #using max() function to find max time and returning that

def print_hacker_info(ip_str, attack_dict):
    '''Print out the hacker's info (usernames, start, end) as specified.'''
    print('Usernames:', end=' ') #print header "Usernames: "
    sub_dict = attack_dict[ip_str] #sub_dict is the dict of usernames list and times lsit
    usernames_list = sub_dict['usernames'] #save list of usernames associated with ip_str
    start = get_start_time(ip_str, attack_dict) #find start time of given attacker
    end = get_end_time(ip_str, attack_dict) #find end time of given attacker
    for username in usernames_list: #iterates over each username in usernames_list and prints each username
        print(username, end=' ') #print usernames on same line separated by a single space
    print()
    print('Start Time:', start) #print start time
    print('End Time:', end) #print end time
    return sub_dict #bc zyLab said so


def print_ips_by_username(username_str, attack_dict):
    '''Find me all the IPs using a given username. Print them as specified.'''
    ips_list = [] #create ip_list variable to store IPs in later
    for ip, sub_dict in attack_dict.items(): #iterate over each key-value pair in attack_dict (key is IP, value is sub_dict)
        usernames_list = sub_dict['usernames'] #save list of usernames from sub_dict
        if(username_str in usernames_list): #if username_str is in the list of usernames, append the IP associated with that list of usernames to ips_list
            ips_list.append(ip)
    
    if(len(ips_list) == 0): #if length of ips_list is 0 after searching for username_str, then username_str is not found
        raise ValueError('Username not found') #creates the new exception of type ValueError with string argument "Username not found" (if created, rest of function is ignored)
    
    #actual printing part
    for ip in ips_list: #iterate over each IP address in ips_list
        print(ip, end=' ') #print IP addresses on same line separated by a single space
    print()
    return ips_list #bc zyLab said so

def main():
    # Call extract_attacks here for both files; Get me a dict of attacks.
    attacks_dict = extract_attacks("hackers1.log") #get dict of attacks for hackers1.log
    attacks_dict.update(extract_attacks("hackers2.log")) #get dict of attacks for hacker2.log and add to dict of attacks for hackers1.log
    while True:
        option = input('MENU\n'
                       'm - Get the attacker with the max attacks\n'
                       'i - Get the attacker by IP address\n'
                       'u - Get the attackers by username\n'
                       'q - Quit\n')
        if(option=='q'):
            break
        if(option=='m'): 
            ip, usernames_list = get_max_attacks(attacks_dict) #call get_max_attacks() function
            print(ip) #print IP address with max attacks
            for username in usernames_list: #print each username associated with the IP address
                print(username, end=' ') #print usernames on same line separated by a single space
            print()
        elif(option=='i'):
            try: #try the code in the following block
                ip_in = input('Enter the IP address:\n') #prompt user for IP address
                print_hacker_info(ip_in, attacks_dict) #print hacker info associated with user-entered IP address by calling print_hacker_info() function
            except KeyError: #if a KeyError is raised by the interpreter from previous block of code, print "IP not found"
                print('IP not found')
        elif(option=='u'):
            try: #try the code in the following block
                username_in = input('Enter the username:\n') #prompt user for username
                print_ips_by_username(username_in, attacks_dict) #print IP addresses associated with the user-entered username by calling print_ips_by_username() function
            except ValueError as e: #if a ValueError is raised, print the string argument passed to the exception when raised
                print(e)

if __name__ == '__main__': #module check
    main()