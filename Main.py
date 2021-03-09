import requests
import npyscreen
from npyscreen.wgtitlefield import TitleText

# FORMS:
class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FirstForm, name="Get user name")

class FirstForm(npyscreen.ActionFormMinimal):
    def create(self):
        self.add(npyscreen.TitleText, w_id="textfield", name = "Write your name")
        self.add(npyscreen.ButtonPress, name = "Get information about your name", when_pressed_function=self.btn_press)
 
 #   BUTTON FUNCTIONALITY:

    def btn_press(self):
        userName = self.get_widget("textfield").value

        # API FOR AGE GUESS:

        url = "https://api.agify.io?name=" + userName
        response = requests.get(url=url)
        response = response.json()
        messageAge = response["age"]
        convertedMessageAge = str(messageAge)
        FianlMessageAge = userName + " is " + convertedMessageAge + " years old \n"
        
        # API FOR GENDER GUESS:

        url = "https://api.genderize.io?name=" + userName
        response = requests.get(url=url)
        response = response.json()
        messageGender = response["gender"]
        FianlMessageGender = "You are a " + messageGender + "\n" 

        #API FOR NATIONALITY GUESS:

        url = "https://api.nationalize.io?name=" + userName
        response = requests.get(url=url)
        response = response.json()
        messageNationality = response["country"][0]["country_id"]
        FinalMessageNationality = "Your country ID is: " + messageNationality
        
        npyscreen.notify_confirm(FianlMessageAge + FianlMessageGender + FinalMessageNationality, 
        title="User info", wrap=True, wide=True, editw=1)
        


# CLOSE PROGRAM:
    def on_ok(self):
        self.parentApp.switchForm(None)

app = App()
app.run()





#print (response["age"])

