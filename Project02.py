# Isaac Hartzell
# July 26, 2019
# This program demonstrates the basics of message passing using a dictionary.
# ----------------------------------------------------------------------------
# Serialization: The first step for implementing serialization would be to use the pickle
# library, at least in python. Whatever library is needed for serialization importing that
# would be the first step. Now lets use the argument for my like function which is a text or the returned liked text.
# This information could be serialized and then that data which is in a binary format could be sent to some server
# that stores texts. All this information could then be displayed in a database. For example, I may have
# a database/server where it would be nice to see the list of liked messages. The list of liked messages could
# possibly be even used for machine learning purposes where a developer would want AI to give the likely
# hood of some specific user liking type of text messages. Maybe based on content from texts that a user likes
# adds that may be more likely to pertain to that user could be shown.
# --------------------------------------------------------------------------------------------------------------
# Approach extended: Looking at the definition of asynchronous messaging, it's a communication method
# where a system puts a message in a queue and there doesn't need to be an immediate response.
# I could extend my current approach to enable distributed messages by adding a queue structure. Lets
# use my display_data function as an example. This function performs its task, the result of this function could be
# stored in a queue and then based on if the client responds immediately or not, lets say the client is a server.
# The system can continue processing other display_data calls.
# To recap, I could extend my message passing approach by implementing a queue data structure. Function calls
# could be put into the queue, and based on if the client responds immediately or not continual processing would occur
# for the other items in the queue.
import time
import datetime


class Message(object):

    def like(self, text):
        liked_message = "Liked: " + text
        return liked_message

    def display_date(self):
        time_stamp = time.time()
        time_stamp_changed_to_string = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        return time_stamp_changed_to_string
    # global so that it has access to current methods and any new ones added.
    methods_of_responding = {'like':like, 'display_date':display_date}


def main():
    msg0 = Message()
    msg1 = Message()
    msg2 = Message()
    msg3 = Message()
    # I'm showing test cases for different messages.
    print(msg0.methods_of_responding["like"](msg0, "Hey Joe, what's going on?"))
    print(msg0.methods_of_responding["display_date"](msg0))
    print('\n')
    # I only have these sleep calls so there's a slight difference in the time of the messages.
    time.sleep(1)

    print(msg1.methods_of_responding["like"](msg1, "Sally, what's for dinner?"))
    print(msg1.methods_of_responding["display_date"](msg1))
    print('\n')
    time.sleep(1)

    print(msg2.methods_of_responding["like"](msg2, "Jon, I like that beer."))
    print(msg2.methods_of_responding["display_date"](msg2))
    print('\n')
    time.sleep(1)

    print(msg3.methods_of_responding["like"](msg3, "Duck typing is neat!"))
    print(msg3.methods_of_responding["display_date"](msg3))
    print('\n')
    time.sleep(1)


if __name__ == '__main__':
    main()

