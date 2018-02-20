from  datetime import datetime
class Spy:
  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

spy=Spy("Shivam","Mr.",25,5.0)
#frnd=Spy(frnd_name,frnd_sal,frnd_age,frnd_rating)

friend_one = Spy('Thapa', 'Mr.', 27, 4.9)
friend_two = Spy('Mavil Gupta', 'Ms.', 21, 4.39)
friend_three = Spy('Hunny Nagpal', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]


class ChatMessage:

    def __init__(self, message, sent_by_me):
        #self.name_of_sender = sender
        #self.message_sent_to = message_sent_to
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

cm=ChatMessage("messege","sent_by_me")

chat_one=ChatMessage("messege","sent_by_me")
chat_two=ChatMessage("messege","sent_by_me")
chat_three=ChatMessage("messege","sent_by_me")

chats=[chat_one,chat_two,chat_three]
