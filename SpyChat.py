from spy_details import spy,friends
from steganography.steganography import Steganography
import csv
from datetime import datetime
from spy_details import Spy, ChatMessage
from termcolor import colored

print (colored("Hello let\'s get started", "cyan", attrs=["dark", "bold"]))

print"Please Login"

STATUS_MESSAGES=['Sleeping','Cant Talk','At the Gym','Do not Disturb','Available','Busy']

friends=[{'name':'Logan','age':26,'rating':5.8,'is_online':True,'chats':[]},{'name':'Deadpool','age':25,'rating':5.5,'is_online':True,'chats':[]}]

#func to load frinds from csv

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader[4:]:
            if row:
                name=row[0]

                age=(row[2])
                rating = (row[3])
                is_online=[4]

            spy = Spy(name,age,rating,is_online)
            friends.append(spy)

load_friends()

#func to load chats

def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[4:]:
            if row:
                name_of_sender = row[0]
                message_sent_to = row[1]
                text = row[2]
                sent_by_me = row[4]
                new_chat = ChatMessage(name_of_sender, message_sent_to, text, sent_by_me)
                chats.append(new_chat)

#func to add status

def add_status(C_S_M):
    if C_S_M != None:
        print "Your current is :"+C_S_M
    else:
        print "You dont have any staus currently"

    user_choice=raw_input("Do ypu want to select from old Status ? Y/N:")
    if user_choice.upper() == 'Y':
        serial_no=1
        for old_status in STATUS_MESSAGES:
            print str(serial_no)+ ". "+old_status
            serial_no=serial_no+1

        user_status_selection=input("Whaich one do you want to set this time")
        new_status=STATUS_MESSAGES[user_status_selection-1]

    elif user_choice.upper()=='N':
        new_status = raw_input("Write your status: ")
        STATUS_MESSAGES.append(new_status)
    else:
        print "Invalid Entry"
    return new_status


#func to add a friend

def add_friend():
    frnd = {
        'name': '',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    frnd.name = raw_input("Write your friend's name")
    friend_sal = raw_input("Mr. or Ms.")
    frnd.name = friend_sal+" "+frnd.name
    frnd.age = input("Enter Age")
    frnd.rating = input("Enter rating of your friend")
    frnd.online = True

    if len(frnd.name)>2 and 50>=frnd.age>=12 and frnd.rating>= spy.rating:
        friends.append(frnd)
        with open('friends.csv', 'a') as friends_data:
         writer = csv.writer(friends_data)
        writer.writerow([frnd.name, frnd.rating, frnd.age, spy.is_online])
    else:
        print("Friend with these values cannot be added ")
        return  len(friends)

def select_frnd():
    serial_no=1
    for frnd in friends:
        print str(serial_no)+" "+ frnd['name']
        serial_no=serial_no+1

    user_selected_frnd=input("Whhich one u want to send msg to?")
    user_index=user_selected_frnd-1
    return user_index

def send_message():
    selected_frnd=select_frnd()
    message=raw_input("Whats your secert message")
    original_image=raw_input("Whats your original image")
    output_path="output.png"
    Steganography.encode(original_image,output_path,message)
    new_chat={
        "message":message,
        "time":datetime.now(),
        "sent_by_me":True
    }
    friends[selected_frnd]['chats'].append(new_chat)
    print "message encrypted"

def read_message():
    chosen_frnd=select_frnd()
    output_path=raw_input("Name of the image to be decoded: ")
    secret_text=Steganography.decode(output_path)
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    friends[chosen_frnd]['chats'].append(new_chat)

    print "Your message is "+ secret_text


#func to load chats



#menu

def start_chat(spy_name, spy_rating, spy_age):
    current_status_msg=None
    show_menu=True
    while show_menu:
        menu_choice=input("What do you want to do: \n 1. Add a status\n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 0. Exit")
        if menu_choice==1:
            current_status_messege= add_status(current_status_msg)
            print "Your new status is updates to "+current_status_messege

        elif menu_choice==2:
            no_of_friend = add_friend()
            print "I have "+ str(no_of_friend)+" frirnds"
        elif menu_choice==3:
            send_message()
            #print "we are going to send message to "+ friends[select_frnd()]
        elif menu_choice==4:
            read_message()
        elif menu_choice==0:
            show_menu=False
        else:
            print"Inavalid choice"

#execution starts from here

#creating login details
user="padman"
pa="pad"
username=raw_input("Enter Username:")
passsword=raw_input("Enter password:")
if username==user and passsword==pa:

    question =raw_input("Are you a new user (Y/N)?")
    if question.upper()=='N':
        print'We already have your details'
        start_chat(spy.name,spy.rating,spy.age)

    elif question.upper()=='Y':


        spy.name = raw_input("What's your name:")
        if len(spy.name)>3:
            print 'Welcome' +" " + spy.name + ".Glad to meet you"
            spy_salutation=raw_input("What should I call you Mr. or Miss.")
            spy.name= spy_salutation + " " + spy.name
            print "Alright " + spy.name + " " + "I would like to know more about you...."



            spy.age = input("What\'s your age?")

            if spy.age > 12 and spy.age < 50:
                spy_rating = input("What is your spy rating?")

                if spy.rating >= 5.0:
                    print 'Great spy!'
                elif spy.rating <5.0 and spy.rating >= 4.5:
                    print 'Nice spy.'
                elif spy.rating <= 4.5 and spy.rating >= 3.5:
                    print 'Hmmm Fine spy'
                else:
                    print "Useless spy"

                spy_is_online = True
                print"Authentication complete. Welcome %s age %d and rating of: %d Proud to have u on board" % (
                    spy.name, spy.age, spy.rating)
                start_chat(spy.name, spy.rating, spy.age)
            else:
                print 'Sorry your age is not valid to be a spy'
        else:
            print "A spy needs to have a valid name. Try again please."

    else:
        print "Invalid Entry"
else:
    print"Please enter a valid username and password"
