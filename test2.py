#import all necessary library to support various predefine fuction
from spy_details import *
from steganography.steganography import Steganography
from datetime import datetime


def start_chat(spy):


    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. \n\n\t\t\t\tWelcome " + spy.name + "..... Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "\n\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend\n 3. select a friend \n 4. Send a secret message \n 5. Read a secret message \n 6. Read Chats from a user \n 7. Close Application \n"
            menu_choice = raw_input(menu_choices)
            try:

                if len(menu_choice) > 0:
                    menu_choice = int(menu_choice)

                    if menu_choice == 1:
                        spy.current_status_message = add_status()

                    elif menu_choice == 2:
                        number_of_friends = add_friend()
                        print 'You have %d friends' % (number_of_friends)
                    elif menu_choice == 3:
                        select_a_friend()
                    elif menu_choice == 4:
                        send_message()
                    elif menu_choice == 5:
                        read_message()
                    elif menu_choice==6:
                        read_chats()
                    else:
                        show_menu = False

            except:
                print "this is not  valid option"
    else:
        print 'Sorry age critiria is not fulfilled'



#function for adding or displaying status of a perticular user
def add_status():

    updated_status_message = None


    if spy.current_status_message != None:
        print 'Your current status message is------> %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'


    status_choice= raw_input("Do you want to select from the older status (y/n)? ")

    if status_choice.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            status_messages.append(new_status_message)
            updated_status_message = new_status_message

    elif status_choice.upper() == 'Y':

        item_position = 1

        for message in status_messages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'


    return updated_status_message


#function for add  new spy friend
def add_friend():
    #new friend details is store here
    new_friend = details('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    #this block change the first letter of name into upper case and remain unchanged if firts letter of name is already in upper case
    first_char=new_friend.name[0]
    remove_with=first_char.upper()
    new_friend.name=new_friend.name.replace(first_char,remove_with)

    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    update=new_friend.salutation[0]
    if update=="m":
        update_char=update.upper()
        new_friend.salutation=new_friend.salutation.replace("m",update_char)



    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


#function for select a friend
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#send secret message
def send_message():
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image:>>?")
    output_path =raw_input("name of stegno file is :>> ")
    text = raw_input("What do you want to say?>> ")
    Steganography.encode(original_image, output_path, text)

    new_chat = messages(text, True)

    friends[friend_choice].chats.append(new_chat)
    print "\t*********Your secret message image is ready!***************"


#read secret message from a friend
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = messages(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


    print "\n\n\t**************Your secret message has been saved!******************"
    print "\n---->your secret message  is-- "+secret_text+"\n\n"
    raw_input('Press enter to continue: ')

#this fuction read chat history from perticuler friend
def read_chats():
    #select a friend whom chat you want to read
    friend_select=select_a_friend()
    for chat in friends[friend_select].chats:
        if chat.sent_by_me:
            print "[%s] %s: %s" %(chat.time.strftime("%d %B %Y"), 'you said-',chat.message)

        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[friend_select].name, chat.message)



#status messages which disply on spy member
status_messages = ['nothing is impossible', 'one often meet his destiny on the road he takes to avoid it.', 'you just need to believe']


print "****************welcomw to spy chat application*****************"

#variable store the user choice for account with which user want to proceed
user_choice = raw_input("Do you want to cotinue as " + spy.salutation + " " + spy.name + " (Y/N)?-->> ")

#condition for user choice
if user_choice.upper() == "Y":
    start_chat(spy)

elif user_choice.upper()=="N":

    spy =details('','',0,0.0)


    spy.name = raw_input("tell me your spy name first: ")

    if len(spy.name)>0:
        try:

            spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

            spy.age = raw_input("What is your age?")
            spy.age = int(spy.age)

            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)

            spy_is_online = True

            start_chat(spy)


        except:
            print "entry not full filled"

    else:
        print "you can not proceed without spy name"


