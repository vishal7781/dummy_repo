from datetime import datetime

class details:

    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class messages:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = details('satyajeet', 'Mr.', 24, 4.7)

friend_one = details('Radhe', 'Mr.', 22, 4.2)
friend_two = details('Shivam', 'Ms.',21, 4.39)
friend_three = details('rahul', 'Dr.', 37, 4.95)


friends = [friend_one, friend_two, friend_three]