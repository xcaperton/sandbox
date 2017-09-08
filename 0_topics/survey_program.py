import unittest
from survey import AnonymousSurvey

test = AnonymousSurvey("What is your favorite song?")

print(test.question)
while True:
    song = input("Song: ")
    if song == 'q':
        break
    test.store_response(song)

print("Thanks for your participation!")
test.show_results()
