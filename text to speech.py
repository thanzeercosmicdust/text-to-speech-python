import pyttsx3
friend=pyttsx3.init()
#print(friend.getProperty("rate"))
friend.setProperty("rate",130)
speech = ""
while True:
    speech =input("input the word")
    if speech == "r":
        #--> you can change the voice spped by given input as 'r'
        change_rate=int(input("enter to change the rate of voice:"))
        friend.setProperty("rate",change_rate)
    elif speech=="":
        break
    else:
        friend.say(speech)
        friend.runAndWait()
