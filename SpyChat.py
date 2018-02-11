from spy_details import spy
print 'Let\'s get started'

STATUS_MESSAGES=['Sleeping','Cant Talk','At the Gym','Do not Disturb','Available','Busy']

friends=[{'name':'logan','age':26,'rating':5.8,'is_online':True},{'name':'padman','age':25,'rating':5.5,'is_online':True}]

def add_status(C_S_M):
    if C_S_M!=None:
        print "Your current is :"+C_S_M
    else:
        print "You dont have any staus currently"

    user_choice=raw_input("Do ypu want to select from old Status ? Y/N:")
    if user_choice.upper()=='Y':
        serial_no=1
        for old_status in STATUS_MESSAGES:
            print str(serial_no)+ ". "+old_status
            serial_no=serial_no+1

        user_status_selection=input("Whaich one do you want to set this time")
        new_status=STATUS_MESSAGES[user_status_selection-1]

    elif user_choice.upper()=='N':
        new_status=raw_input("Write your status: ")
        STATUS_MESSAGES.append(new_status)
    else:
        print "Invalid Entry"
    return new_status

def add_friend():
    frnd = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    frnd['name']=raw_input("Write your friend's name")
    friend_sal=raw_input("Mr. or Ms.")
    frnd['name']=friend_sal+" "+frnd['name']
    frnd['age']=input("Enter Age")
    frnd['rating']=input("Enter rating of your friend")

    if len(frnd['name'])>2 and 50>=frnd['age']>=12 and frnd['rating']>= spy['rating']:
        friends.append(frnd)
    else:
        print("Friend with these values cannot be added ")
    return  len(friends)

def select_frnd():
    serial_no=1
    for frnd in friends:
        print str(serial_no)+" "+ frnd['name']
        serial_no=serial_no+1

    user_selected_frnd=input("Whhich one u want to send msg to?")
    user_index=friends[user_selected_frnd-1]
    return user_index

def start_chat(spy_name, spy_rating, spy_age):
    current_status_msg=None
    show_menu=True
    while show_menu:
        menu_choice=input("What do you want to do: \n 1. Add a status\n 2. Add a friend \n 3. Send a message \n 0. Exit")
        if menu_choice==1:
           current_status_messege= add_status(current_status_msg)
           print "Your new status is updates to "+current_status_messege

        elif menu_choice==2:
            no_of_friend=add_friend()
            print "I have "+ str(no_of_friend)+" frirnds"
        elif menu_choice==3:
            selected_frnd=select_frnd()
            #print "we are going to send message to "+ friends[select_frnd()]

        elif menu_choice==0:
            show_menu=False
        else:
            print"Inavalid choice"


question =raw_input("Are you a new user (Y/N)?")
if question.upper()=='N':
    print'We already have your details'
    start_chat(spy['name'],spy['rating'],spy['age'])

elif question.upper()=='Y':
    spy = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }


    spy_name = raw_input("What's your name:")
    if len(spy['name'])>3:
        print 'Welcome' +" " + spy['name'] + ".Glad to meet you"
        spy_salutation=raw_input("What should i call you Mr. or Miss.")
        spy['name']= spy_salutation + " " + spy['name']
        print "Alright " + spy['name'] + " " + "I would like to know more about you."



        spy['age'] = input("What is your age?")

        if spy['age'] > 12 and spy['age'] < 50:
            spy_rating = input("What is your spy rating?")

            if spy['rating'] >= 5.0:
                print 'Great spy!'
            elif spy['rating'] <5.0 and spy['rating'] >= 4.5:
                print 'NIce spy.'
            elif spy['rating'] <= 4.5 and spy_['rating'] >= 3.5:
                print 'Fine spy'
            else:
                print "useless spy"

            spy_is_online = True
            print"Authentication complete. Welcome %s age %d and rating of: %d Proud to have u on board" % (
            spy['name'], spy['age'], spy['rating'])
            start_chat(spy['name'], spy['rating'], spy['age'])
        else:
           print 'Sorry your age is not valid to be a spy'
    else:
        print "A spy needs to have a valid name. Try again please."

else:
    print "Invalid Entry"
