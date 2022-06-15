
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Canvas, Toplevel, ttk
from threading import Thread, Event
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from external import comment, send_delayed_password, send_delayed_user, acc, passw
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep


 
class Bot_app(ttk.Frame):
    #Ventana root
    def __init__(self, master = None):
        super().__init__(master)

        self.t1 = None
        self.stop_bot_full = Event()

        self.t2 = None
        self.stop_bot_stories = Event()

        self.t3 = None
        self.stop_bot_feed = Event()

        self.master = master
        self.pack()
        self.container()

        self.close_app = ttk.Button(text="Exit", command=root.destroy)
        self.close_app.place(x=250, y=200)

    #Container frames RRSS
    def container(self):
        self.containerFrame = tk.Frame(self)
        self.containerFrame.pack()
        self.create_widget_root()
        
    #Frames RRSS
    def create_widget_root(self):

        #Open comment and like boot
        self.frame1 = ttk.Frame( self.containerFrame, width=110, height=100)
        self.frame1.pack(side="left", padx=20, pady=20)
        self.btnInstaOpen = ttk.Button(self.frame1, text="Like&Comment", command=self.window_comment_like)
        self.btnInstaOpen.pack(side="bottom", padx=20, pady=10)
        self.canvas1 = Canvas(self.frame1, width=90, height=90)
        self.canvas1.pack(pady=5)
        self.img1 = Image.open("/Users/javiermartin/Desktop/mibot/material/comment.png")
        self.resized_image1 = self.img1.resize((85,85), Image.Resampling.LANCZOS) 
        self.new_image1= ImageTk.PhotoImage(self.resized_image1)
        self.canvas1.create_image(45,45, image=self.new_image1)

        #Open feed bot
        self.frame3 = ttk.Frame( self.containerFrame, width=110, height=150)
        self.frame3.pack(side="right", padx=40, pady=20)
        self.btnLinkOpen = ttk.Button(self.frame3, text="Feed", command=self.window_feed)
        self.btnLinkOpen.pack(side="bottom", padx=20, pady=10)
        self.canvas3 = Canvas(self.frame3, width=90, height=90)
        self.canvas3.pack(pady=5)
        self.img3 = Image.open("/Users/javiermartin/Desktop/mibot/material/feed.png")
        self.resized_image3 = self.img3.resize((70,85), Image.Resampling.LANCZOS) 
        self.new_image3 = ImageTk.PhotoImage(self.resized_image3)
        self.canvas3.create_image(45,45, image=self.new_image3)

        #Open stories bot
        self.frame2 = ttk.Frame( self.containerFrame, width=110, height=150)
        self.frame2.pack(side="right", padx=20, pady=20)
        self.btnLinkOpen = ttk.Button(self.frame2, text="Stories", command=self.window_stories)
        self.btnLinkOpen.pack(side="bottom", padx=20, pady=20)
        self.canvas2 = Canvas(self.frame2, width=90, height=90)
        self.canvas2.pack(pady=5)
        self.img2 = Image.open("/Users/javiermartin/Desktop/mibot/material/stories.png")
        self.resized_image2 = self.img2.resize((85,85), Image.Resampling.LANCZOS) 
        self.new_image2 = ImageTk.PhotoImage(self.resized_image2)
        self.canvas2.create_image(45,45, image=self.new_image2)


#Bot windows
    #Comment and like window(w1)
    def window_comment_like(self):

        self.w1 = Toplevel(app)
        self.w1.wm_title("Bot Like&comment")
        self.w1.iconbitmap('/Users/javiermartin/Desktop/mibot/material/ico/comment.ico')
        self.w1.geometry("500x200")
        self.w1.resizable(0, 0)
        self.labelHashtag = ttk.Label(self.w1, text="Enter # to use:")
        self.labelHashtag.place(x=30, y=30)
        self.entryHashtag = ttk.Entry(self.w1)
        self.entryHashtag.place(x=125, y=30)
        self.labelSpinbox = ttk.Label(self.w1, text="Number of pics for each # (1, 3 or 5):")
        self.labelSpinbox.place(x=30, y=70)
        self.spinbox = ttk.Spinbox(self.w1, from_=1, to=5, increment=2, state='readonly')
        self.spinbox.place(x=30, y=100, width=70)
        self.btnLaunch = ttk.Button(self.w1, text="Launch bot", command=self.thread_bot_full)
        self.btnLaunch.place(x=30, y=150)
        self.btnStop = ttk.Button(self.w1, text="Stop bot", command=self.stop_thread_bot_full)
        self.btnStop.place(x=150, y=150)

    #Stories window(w2)        
    def window_stories(self):

        self.w2 = Toplevel(app)
        self.w2.wm_title("Bot Stories")
        self.w2.iconbitmap('/Users/javiermartin/Desktop/mibot/material/ico/stories.ico')
        self.w2.geometry("300x180")
        self.w2.resizable(0, 0)
        self.label_spinbox = ttk.Label(self.w2, text="Number of stories (15 to 30):")
        self.label_spinbox.place(x=30, y=30)
        self.spinbox = ttk.Spinbox(self.w2, from_=15, to=30, state='readonly')
        self.spinbox.place(x=30, y=60, width=70)
        self.btn_launch = ttk.Button(self.w2, text="Launch bot", command=self.thread_bot_stories)
        self.btn_launch.place(x=30, y=120)
        self.btn_stop = ttk.Button(self.w2, text="Stop bot", command=self.stop_thread_bot_stories)
        self.btn_stop.place(x=150, y=120)

    #Feed window(w3)
    def window_feed(self):

        self.w3 = Toplevel(app)
        self.w3.wm_title("Bot Feed")
        self.w3.iconbitmap('/Users/javiermartin/Desktop/mibot/material/ico/feed.ico')
        self.w3.geometry("300x180")
        self.w3.resizable(0, 0)
        self.label_spinbox = ttk.Label(self.w3, text="Number of articles (5 to 10):")
        self.label_spinbox.place(x=30, y=30)
        self.spinbox = ttk.Spinbox(self.w3, from_=5, to=10, state='readonly')
        self.spinbox.place(x=30, y=60, width=70)
        self.btn_launch = ttk.Button(self.w3, text="Launch bot", command=self.thread_bot_feed)
        self.btn_launch.place(x=30, y=120)
        self.btn_stop = ttk.Button(self.w3, text="Stop bot", command=self.stop_thread_bot_feed)
        self.btn_stop.place(x=150, y=120)


    def bot_stories(self):

        if self.stop_bot_stories == False:

            n_stories = self.spinbox.get()
            
            #Set Driver
            chrome_path = r'/usr/local/bin/chromedriver'
            driver = webdriver.Chrome(executable_path=chrome_path)

            #Go to instagram
            driver.get('https://www.instagram.com/')
            sleep(10)

            #cookies
            button_cookies = driver.find_element(By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm')
            button_cookies.click()
            sleep(3)

            #Login
            username = driver.find_element(By.NAME,'username')
            send_delayed_user(username, acc)
            password = driver.find_element(By.NAME,'password')
            send_delayed_password(password, passw)
            button_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
            sleep(5)
            print('Login successfully')

            if self.stop_bot_stories == True:
                driver.close()
                driver.quit()
                exit()

            #cookies
            try:
                button_cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
                sleep(3)
            except:
                pass

            # Remember username
            remember_user_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            sleep(5)

            #notifications
            button_notifications = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
            button_notifications.click()
            sleep(3)

            #Select stories
            first_history = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[2]/div/div/div/div/ul/li[4]/div/button')
            first_history.click()
            sleep(3)

            if self.stop_bot_stories == True:
                driver.close()
                driver.quit()
                exit()
                
            for n in range(int(n_stories)): # Like on history 
                try:
                    try:
                        # Like buttons:
                        like_button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div[2]/span/button')
                        like_button1.click()                               
                        sleep(1)
                    except:
                        like_button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div/span/button')
                        like_button2.click()
                        sleep(1)
                        
                except: #Next story
                    print('Story delete Next story')
                    if n<int(n_stories) - 1:
                        print('Next story')
                        button_next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]')
                        
                        button_next.click()
                        sleep(1)
                

                if self.stop_bot_stories == True:
                    driver.close()
                
                print('Story finished')

                if n<int(n_stories) - 1:
                    print('Next story')
                    button_next = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]')
                    button_next.click()
                    sleep(1)
            
            print(' All stories complete')
            sleep(3)


    def bot_full(self):

        if self.stop_bot_full == False:

            hashtag = self.entryHashtag.get().split(", ")
            n_hashtag = self.spinbox.get()

            contador = 0

            n_post = 1

            print('Hashtag list: ' + str(hashtag))
            print('Number of #: ' + str(int(n_hashtag)))
            

            #Set Driver
            chrome_path = r'/usr/local/bin/chromedriver'
            driver = webdriver.Chrome(executable_path=chrome_path)

            #Go to instagram
            driver.get('https://www.instagram.com/')
            sleep(10)

            #cookies
            button_cookies = driver.find_element(By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm')
            button_cookies.click()
            sleep(3)

            #Login
            username = driver.find_element(By.NAME,'username')
            send_delayed_user(username, acc)
            password = driver.find_element(By.NAME,'password')
            send_delayed_password(password, passw)
            button_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
            sleep(5)
            print('Login successfully')

            if self.stop_bot_full == True:
                driver.close()
                driver.quit()

            #cookies
            try:
                button_cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
                sleep(3)
            except:
                pass
            # Remember username
            remember_user_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

            # search Hashtags
            for h in hashtag:
                driver.get('https://www.instagram.com/explore/tags/'+ str(hashtag[contador]))
                sleep(7)
                
                #Select first thumbnail
                first_post = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div['+ str(n_post) +']/a/div').click()
                sleep(5)

                if self.stop_bot_full == True:
                    driver.close()
                    driver.quit()
                    
                for n in range(int(n_hashtag)): # Like and Comment on post
                    # Like
                    button_like = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]').click()
                    sleep(3)

                    # Post Comment
                    try:
                        post_comment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
                        post_comment.click()
                    except:
                        pass
                    post_comment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
                    post_comment.send_keys(random.choice(comment))
                    post_comment.send_keys(Keys.ENTER)
                    sleep(3)

                    if self.stop_bot_full == True:
                        driver.close()
                        driver.quit()
                    
                    print('Post ' + str(n) + ' en #' + str(hashtag[contador]))

                    close_thumbnail = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div')
                    close_thumbnail.click()
                    sleep(3)

                    #Next post
                    if n<int(n_hashtag) - 1:
                        print('Next post')
                        n_post += 1
                        next_post = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div['+ str(n_post) +']/a/div')
                        next_post.click()                          
                        sleep(3)

                print('#' + str(hashtag[contador]) + ' complete')
                contador += 1
                n_post = 1
                sleep(3)


    def bot_feed(self):

        if self.stop_bot_feed == False:

            n_likes = self.spinbox.get()

            n_article = 1

            print('Number of likes: ' + str(int(n_likes)))
            

            #Set Driver
            chrome_path = r'/usr/local/bin/chromedriver'
            driver = webdriver.Chrome(executable_path=chrome_path)

            #Go to instagram
            driver.get('https://www.instagram.com/')
            sleep(10)

            #cookies
            button_cookies = driver.find_element(By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm')
            button_cookies.click()
            sleep(3)

            #Login
            username = driver.find_element(By.NAME,'username')
            send_delayed_user(username, acc)
            password = driver.find_element(By.NAME,'password')
            send_delayed_password(password, passw)
            button_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
            sleep(5)
            print('Login successfully')

            if self.stop_bot_feed == True:
                driver.close()
                driver.quit()

            #cookies
            try:
                button_cookies = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
                sleep(3)
            except:
                pass
            # Remember username
            remember_user_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

            #notifications
            button_notifications = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
            button_notifications.click()
            sleep(3)

            print('First article')

            for n in range(int(n_likes)): # Like and Comment on post

                #Select article
                next_article = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[3]/div[1]/div/article['+ str(n_article) +']/div/div[3]/div/div/section[1]')
                actions = ActionChains(driver)                
                actions.move_to_element(next_article).perform()
                sleep(2)

                # Like
                button_like = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[3]/div[1]/div/article['+ str(n_article) +']/div/div[3]/div/div/section[1]/span[1]/button').click()
                sleep(2)

                #Post Comment
                try:
                    #Select textarea
                    textarea = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[3]/div[1]/div/article['+ str(n_article) +']/div/div[3]/div/div/section[3]/div/form/textarea')
                    actions = ActionChains(driver)
                    actions.move_to_element(textarea).perform()                    
                    sleep(3)
                
                    post_comment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[3]/div[1]/div/article['+ str(n_article) +']/div/div[3]/div/div/section[3]/div/form/textarea')
                    post_comment.click()
                except:
                    pass
                post_comment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[3]/div[1]/div/article['+ str(n_article) +']/div/div[3]/div/div/section[3]/div/form/textarea')
                post_comment.send_keys(random.choice(comment))
                post_comment.send_keys(Keys.ENTER)
                sleep(5)

                if self.stop_bot_feed == True:
                    driver.close()
                    driver.quit()
                
                #Next article
                if n<int(n_likes) - 1:
                    print('Next article')
                    n_article += 1
                    sleep(3)
                        
#Threads
    #This thread executes bot full
    def thread_bot_full(self):
        self.stop_bot_full=False
        self.t1=Thread(target=self.bot_full)
        self.t1.start()

    #This thread stops bot full
    def stop_thread_bot_full(self):
        self.stop_bot_full=True
        self.t1.join()
        print('Thread killed')

    #This thread executes bot stories
    def thread_bot_stories(self):
        self.stop_bot_stories=False
        self.t2=Thread(target=self.bot_stories)
        self.t2.start()

    #This thread stops bot stories
    def stop_thread_bot_stories(self):
        self.stop_bot_stories=True
        self.t2.join()
        print('Thread killed')

    #This thread executes bot feed
    def thread_bot_feed(self):
        self.stop_bot_feed=False
        self.t3=Thread(target=self.bot_feed)
        self.t3.start()

    #This thread stops bot feed
    def stop_thread_bot_feed(self):
        self.stop_bot_feed=True
        self.t3.join()
        print('Thread killed')
        

if __name__== "__main__":
#window root
    root = tk.Tk()
    root.wm_title("The Good Bot v1.0")
    root.geometry("600x270")
    root.resizable(0, 0)
    app = Bot_app(root)
    root.iconbitmap('/Users/javiermartin/Desktop/mibot/bot.ico')
    root.mainloop()