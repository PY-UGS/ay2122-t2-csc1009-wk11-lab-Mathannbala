class clockTime:

    def __init__(self):
        self.Hours = ""
        self.Minutes = ""
        self.Seconds =""

    def setHours(self,Hours):
        self.Hours =Hours

    def setMinutes(self,Minutes):
        self.Minutes =Minutes

    def setSeconds(self,Seconds):
        self.Seconds = Seconds

    def setTime(self,Hours, Minutes, Seconds):
        self.setHours(Hours)
        self.setMinutes(Minutes)
        self.setSeconds(Seconds)

    def showTime(self):
        print(str(self.Hours) +":" + str(self.Minutes) + ":" + str(self.Seconds))


Hours =input("Enter Hours: ")
Min = input("Enter Minutes: ")
sec = input("Enter seconds: ")
Time = clockTime()
Time.setTime(Hours,Min,sec)
print("The new time is: ")
Time.showTime()

