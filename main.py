#!/usr/bin/python
print """ __      __                     .__              ._._._.                              
/  \    /  \_____ _______  ____ |__| ____    ____| | | |                              
\   \/\/   /\__  \\_  __ \/    \|  |/    \  / ___\ | | |                              
 \        /  / __ \|  | \/   |  \  |   |  \/ /_/  >|\|\|                              
  \__/\  /  (____  /__|  |___|  /__|___|  /\___  /______                              
       \/        \/           \/        \//_____/ \/\/\/                              
_____.___.                                      __    .__                             
\__  |   | ____  __ __    _____  __ __  _______/  |_  |  |__ _____ ___  __ ____       
 /   |   |/  _ \|  |  \  /     \|  |  \/  ___/\   __\ |  |  \\__  \\  \/ // __ \      
 \____   (  <_> )  |  / |  Y Y  \  |  /\___ \  |  |   |   Y  \/ __ \\   /\  ___/      
 / ______|\____/|____/  |__|_|  /____//____  > |__|   |___|  (____  /\_/  \___  >     
 \/                           \/           \/              \/     \/          \/      
        .__  __                       .___                 __  .__                    
   ____ |__|/  |_  _____    ____    __| _/ ______ ___.__._/  |_|  |__   ____   ____   
  / ___\|  \   __\ \__  \  /    \  / __ |  \____ <   |  |\   __\  |  \ /  _ \ /    \  
 / /_/  >  ||  |    / __ \|   |  \/ /_/ |  |  |_> >___  | |  | |   Y  (  <_> )   |  \ 
 \___  /|__||__|   (____  /___|  /\____ |  |   __// ____| |__| |___|  /\____/|___|  / 
/_____/                 \/     \/      \/  |__|   \/                \/            \/  
.__                 __         .__  .__             .___                              
|__| ____   _______/  |______  |  | |  |   ____   __| _/                              
|  |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \ / __ |                               
|  |   |  \\___ \  |  |  / __ \|  |_|  |_\  ___// /_/ |                               
|__|___|  /____  > |__| (____  /____/____/\___  >____ |                               
        \/     \/            \/               \/     \/                               """


print "cheacking for updates..."
import urllib2,os
response = urllib2.urlopen('https://raw.githubusercontent.com/ZZcat/Ggolf/master/version.txt')
html = response.read()
web_vesion = html[:5]
f = open('version.txt', 'r')
vesion = f.read()
print "Your vesion is ",vesion,"\nThe newest vesion is ", web_vesion
if int(vesion) == int(web_vesion):
   print "You have the newest vesion!"
else:
   print "###You need to update this program"
   print "###Updating..."
   print "\n###Reading lines"
   folder_dir = os.popen("pwd").readlines()
   print "###Done!!!"
   print "\n###Cuting varuibal"
   folder_dir = folder_dir[:-10]
   print "###Done!!!\n\n###Cloning dicrectory"
   com = "git clone https://github.com/ZZcat/C-code.git"
   os.system(com)
   print "###Done\n\n###Moving directory"
   com = "mv C-code " , folder_dir
   print "###Done!!!"
   print "\n###Removing copy folder"
   com = "rm C-code"
   print "###Done!!!"
   





import pygame,datetime,sys,select,socket
from datetime import date
from pygame.locals import *
pygame.init()


class Button:
   def __init__(self, text):
      self.text = text
      self.is_hover = False
      self.default_color = (100,100,100)
      self.hover_color = (255,255,255)
      self.font_color = (0,0,0)
      self.obj = None
      
   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)
      
   def color(self):
      '''change color when hovering'''
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
   def draw(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      screen.blit(self.label(), labelcoord)
      
      #change color if mouse over button
      self.check_hover(mouse)
      
   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True 
      else:
         self.is_hover = False


if __name__ == '__main__':
   # Define some colors
   BLACK = (0, 0, 0)
   WHITE = (255, 255, 255)
   RED = (255, 0, 0)
   GREEN = (0, 255, 0)
   BLUE = (0, 0, 255)
   

   # Set up screen and clock
   screen = pygame.display.set_mode((1000,700))
   clock = pygame.time.Clock()
   pygame.display.set_caption('Encrypted text sender')
   

   # Set up vars
   run = True
   DATE_clicked = 0
   TIME_clicked = 0
   OS_sys = "win"
   typing = False
   text = ""
   host = "192.168.253.166"
   port = 9010

   # chat vars
   t1 = ""
   t2 = ""
   t3 = ""
   t4 = ""
   t5 = ""
   t6 = ""
   t7 = ""
   t8 = ""
   t9 = ""
   

   # Set up buttons
   DATE = Button('Date')
   TIME = Button('Time')
   OS = Button('WIN')
   TEXT = Button("Type here:")

   ## Setup text
   font = pygame.font.SysFont("monospace", 15)


   ## load images
   pointer = pygame.image.load("cat_pointer.gif")
   pointerrect = pointer.get_rect()

   while run:
    
      pygame.mouse.set_visible(False)      
      (mouseX, mouseY) = pygame.mouse.get_pos()
      mouse = pygame.mouse.get_pos()
      for event in pygame.event.get():
         
         if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.quit()
            print "quit"
         elif typing == True and event.type == KEYDOWN:
            if event.unicode.isalpha():
                text += event.unicode
                TYPE_TEXT = font.render(text, True, (0, 128, 0))
            elif event.key == K_BACKSPACE:
                text = text[:-1]
                TYPE_TEXT = font.render(text, True, (0, 128, 0))
            elif event.key == K_RETURN:
                s.send(text)
                print "sent: " + text
                t9 = t8
                t8 = t7
                t7 = t6
                t6 = t5
                t5 = t4
                t4 = t3
                t3 = t2
                t2 = t1
                t1 = "[You]:"+text
                text = ""
                TYPE_TEXT = font.render(text, True, (0, 128, 0))
            elif event.key == pygame.K_1:
                
               text = text + str(1)
            elif event.key == pygame.K_2:
               text = text + str(2)
            elif event.key == pygame.K_3:
               text = text + str(3)
            elif event.key == pygame.K_4:
               text = text + str(4)
            elif event.key == pygame.K_5:
               text = text + str(5)
            elif event.key == pygame.K_6:
               text = text + str(6)
            elif event.key == pygame.K_7:
               text = text + str(7)
            elif event.key == pygame.K_8:
               text = text + str(8)
            elif event.key == pygame.K_9:
               text = text + str(9)
            elif event.key == (pygame.K_0):
               text = text + str(0)


              
         elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load("click.wav")
            pygame.mixer.music.play()
            if not TEXT.obj.collidepoint(mouse):
               typing = False
            if DATE.obj.collidepoint(mouse):
################################################################################################
               if DATE_clicked == 0:
                   
                  if OS_sys == "mac":
                     os.system("say Enabling date")
                     DATE_clicked = 1
                  else:
                     DATE_clicked = 1
               else:
                  if OS_sys == "mac":
                     os.system("say Disabling date")
                     DATE_clicked = 0
                  if OS_sys == "win":
                     DATE_clicked = 0
####################################################################################################
            elif TIME.obj.collidepoint(mouse):
                if TIME_clicked == 0:
                  if OS_sys == "mac":
                     os.system("say Enabling time")
                     TIME_clicked = 1
                  else:
                     TIME_clicked = 1
                else:
                   if OS_sys == "mac":
                     os.system("say Disabling time")
                     TIME_clicked = 0
                   if OS_sys == "win":
                      TIME_clicked = 0
####################################################################################################
            elif OS.obj.collidepoint(mouse):
                if OS_sys == "win":
                   OS_sys = "mac"
                   os.system("Turn on mac mode")
                   OS = Button('mac')
                elif OS_sys == "mac":
                   os.system("Turning off mac mode")
                   OS_sys = "win"
                   OS = Button('WIN')
####################################################################################################

####################################################################################################
            elif TEXT.obj.collidepoint(mouse):
               if typing == False:
                  typing = True
                  TYPE = Button("Typing")
               else:
                  typing = False
                  TYPE = Button("Type")




               
      if DATE_clicked == 1:
          DATE = Button(str(date.today()))
      if TIME_clicked == 1:
         TIME = Button(str(datetime.datetime.now().time()))
      
      if typing == True:
          TEXT_text = ("Typing...:"+str(text))
      else:
          TEXT_text = ("Type here:"+str(text))


      T1 = font.render(t1, 1, (255,255,0))
      T2 = font.render(t2, 1, (255,255,0))
      T3 = font.render(t3, 1, (255,255,0))
      T4 = font.render(t4, 1, (255,255,0))
      T5 = font.render(t5, 1, (255,255,0))
      T6 = font.render(t6, 1, (255,255,0))
      T7 = font.render(t7, 1, (255,255,0))
      T8 = font.render(t8, 1, (255,255,0))
      T9 = font.render(t9, 1, (255,255,0)) 
      screen.blit(T9, (30, 515))
      screen.blit(T8, (30, 530))
      screen.blit(T7, (30, 545))
      screen.blit(T6, (30, 560))
      screen.blit(T5, (30, 575))
      screen.blit(T4, (30, 590))
      screen.blit(T3, (30, 605))
      screen.blit(T2, (30, 620))
      screen.blit(T1, (30, 635))
      
      
      TEXT = Button(TEXT_text)
      screen.blit(pointer,((mouseX-25),(mouseY-25)))
      
      TIME.draw(screen, mouse, (850,15,100,20), (875,18))
      DATE.draw(screen, mouse, (700,15,100,20), (724,18))
      OS.draw(screen, mouse, (100,160,100,20), (125,163))
      TEXT.draw(screen, mouse, (30, 650,660,20), (55,654))
      
      pygame.display.update()
      screen.fill(BLACK)
