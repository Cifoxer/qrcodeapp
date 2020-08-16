from kivymd.app import MDApp
import qrcode
import random
import barcode
from barcode.writer import ImageWriter
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from  kivy.uix.boxlayout import BoxLayout
import webbrowser
from plyer import storagepath
from plyer import email
from kivy.core.clipboard import Clipboard
from kivymd.uix.button import MDRoundFlatIconButton
class InfoAboutDevelopers(BoxLayout):
    pass

class ReportBug(BoxLayout):
    pass       
        

class MainApp(MDApp):
    dialog = None
    info = None

    def build(self):
        pass

    def random_choise(self):
        global choise
        choise = random.random()

    def get_qrcode(self):
        #generate yours qrcode
        global store


        user_qrcode = self.root.ids.qrcode
        '''take ids

        '''
        my_text = self.root.ids.inp
        img = qrcode.make(my_text.text)#take url or text 
        self.random_choise()
        png = '.png'
        path_save_image = storagepath.get_pictures_dir()
        slash = "\\"
        #print(slash)
        path = path_save_image + slash
        forsave = path + str(choise) + png
        
        img.save(forsave)
        show_qr = forsave 
        user_qrcode.source = show_qr

    #----------------------------------------------------------------------------DIALOGS
    def show_confirmation_dialog(self):
            if not self.dialog:
                self.dialog = MDDialog(
                    title="Address:",
                    type="custom",
                    content_cls=Content(),
                    buttons=[
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color
                        ),
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color
                        ),
                    ],
                )
            self.dialog.open()

    def info_about_developer(self):
        my_dialog = MDDialog(title="List of developers:", size_hint= [.8, .4], type= "custom", content_cls= InfoAboutDevelopers(), buttons = [MDRoundFlatIconButton(text ="Facebook", icon = "facebook-box", on_press = self.face)])
        my_dialog.open()

    def info_about_new_funck(self):
        my_dialog_2 = MDDialog(title="About Project:" ,text= "My project is built using a buildozer based on python and kivymd (kivy, plyer). In the future, features such as qrcode reader and barcode will be added to the project. The rest of the information and updates can be found on github.",
            size_hint= [.8, .3],
            buttons =[
                MDRoundFlatIconButton(text= "GITHUB",icon = "github-circle", on_press = self.github, width = 160)
            ] 
            )

        my_dialog_2.open()
    def list_udpate(self):
        my_dialog_3 = MDDialog(title= "List of Updates :",text = "no updates now", size_hint = [.8, .2])
        my_dialog_3.open()

    #send_________________________________________________EMAIL__________________________________________________________
    def face(self,instance):

        webbrowser.open('https://www.facebook.com/jar.sin.54/')

        
    def paste(self):
        self.root.ids.inp.text = Clipboard.paste() 
        
    def github(self,instance):
        webbrowser.open('https://github.com/Cifoxer/qrcodeapp')
    #_____________________________________SEND____BUG___________________________________________________________________________________________--

    def send_email(self):
        text_email = self.root.ids.text_bug.text
        subject_email = self.root.ids.subject_bug.text
        email.send(recipient="jarsin09@gmail.com", subject=subject_email, text=text_email, create_chooser=False)



        
    












if __name__ == "__main__":


    MainApp().run()