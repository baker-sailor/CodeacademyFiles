import random

name = "Simon"
question = "Is there alien life on Earth?"
answer = ""

random_number = random.randint(1,12)
#print(random_number)

if random_number == 1:
  answer="Yes - definitely."
elif random_number == 2:
  answer="It is decidedly so."
elif random_number == 3:
  answer="Without a doubt."
elif random_number == 4:
  answer="Reply hazy, try again."
elif random_number == 5:
  answer="Ask again later."
elif random_number == 6:
  answer="Better not tell you now."
elif random_number == 7:
  answer="My sources say no."
elif random_number == 8:
  answer="Outlook not so good."
elif random_number == 9:
  answer="Very doubtful."
elif random_number == 10:
  answer="I hope not."
elif random_number == 11:
  answer="If we're lucky."
elif random_number == 12:
  answer="You talking to me?"
else:
  print("Error")

if question == "":
  print("If a question is asked, but the Magic 8-Ball can't hear it - does it have an answer? No. Ask a damn question.")
elif name == "":
  print("The quesion is: ", question)
  print("Magic 8-Ball says: ", answer)
else:
  print(name, " asks: ", question)
  print("Magic 8-Ball says: ", answer)
