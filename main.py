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
        \/     \/            \/               \/     \/                               
Warning!!!!
You must have git and python installed"""

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
   screen = pygame.display.set_mode((1000,1000))
   clock = pygame.time.Clock()
   pygame.display.set_caption('GGolf')
   

   # Set up vars
   run = True
   DATE_clicked = 1
   TIME_clicked = 1
   typing = False
   text = ""
   TEXT_text = "Type your rule here:"
   ctrl = False
   shift = False
   

   # Set up buttons
   DATE = Button('Date')
   TIME = Button('Time')
   TEXT = Button("")

   ## Setup text
   font = pygame.font.SysFont('monospace',100) #SysFont creates a font object from available pygame fonts


   ## load images
   pointer = pygame.image.load("cat_pointer.gif")
   pointerrect = pointer.get_rect()
   grid = pygame.image.load("grid.png")

   shifted = False
   sr = '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\\'()*+,-./:;<=>?@[\]^_`{|}~\''
   while run:
       

      
      pygame.mouse.set_visible(False)      
      (mouseX, mouseY) = pygame.mouse.get_pos()
      mouse = pygame.mouse.get_pos()
      
      events = pygame.event.get()
      for event in events:
            if event.type == KEYUP and typing == True:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: shifted = False
            if event.type == KEYDOWN and typing == True:
                if event.key == K_BACKSPACE: text = text[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: shifted = True
                elif event.key == K_SPACE: text += ' '
                if not shifted:
                    if event.key == K_a and 'a' in sr: text += 'a'
                    elif event.key == K_b and 'b' in sr: text += 'b'
                    elif event.key == K_c and 'c' in sr: text += 'c'
                    elif event.key == K_d and 'd' in sr: text += 'd'
                    elif event.key == K_e and 'e' in sr: text += 'e'
                    elif event.key == K_f and 'f' in sr: text += 'f'
                    elif event.key == K_g and 'g' in sr: text += 'g'
                    elif event.key == K_h and 'h' in sr: text += 'h'
                    elif event.key == K_i and 'i' in sr: text += 'i'
                    elif event.key == K_j and 'j' in sr: text += 'j'
                    elif event.key == K_k and 'k' in sr: text += 'k'
                    elif event.key == K_l and 'l' in sr: text += 'l'
                    elif event.key == K_m and 'm' in sr: text += 'm'
                    elif event.key == K_n and 'n' in sr: text += 'n'
                    elif event.key == K_o and 'o' in sr: text += 'o'
                    elif event.key == K_p and 'p' in sr: text += 'p'
                    elif event.key == K_q and 'q' in sr: text += 'q'
                    elif event.key == K_r and 'r' in sr: text += 'r'
                    elif event.key == K_s and 's' in sr: text += 's'
                    elif event.key == K_t and 't' in sr: text += 't'
                    elif event.key == K_u and 'u' in sr: text += 'u'
                    elif event.key == K_v and 'v' in sr: text += 'v'
                    elif event.key == K_w and 'w' in sr: text += 'w'
                    elif event.key == K_x and 'x' in sr: text += 'x'
                    elif event.key == K_y and 'y' in sr: text += 'y'
                    elif event.key == K_z and 'z' in sr: text += 'z'
                    elif event.key == K_0 and '0' in sr: text += '0'
                    elif event.key == K_1 and '1' in sr: text += '1'
                    elif event.key == K_2 and '2' in sr: text += '2'
                    elif event.key == K_3 and '3' in sr: text += '3'
                    elif event.key == K_4 and '4' in sr: text += '4'
                    elif event.key == K_5 and '5' in sr: text += '5'
                    elif event.key == K_6 and '6' in sr: text += '6'
                    elif event.key == K_7 and '7' in sr: text += '7'
                    elif event.key == K_8 and '8' in sr: text += '8'
                    elif event.key == K_9 and '9' in sr: text += '9'
                    elif event.key == K_BACKQUOTE and '`' in sr: text += '`'
                    elif event.key == K_MINUS and '-' in sr: text += '-'
                    elif event.key == K_EQUALS and '=' in sr: text += '='
                    elif event.key == K_LEFTBRACKET and '[' in sr: text += '['
                    elif event.key == K_RIGHTBRACKET and ']' in sr: text += ']'
                    elif event.key == K_BACKSLASH and '\\' in sr: text += '\\'
                    elif event.key == K_SEMICOLON and ';' in sr: text += ';'
                    elif event.key == K_QUOTE and '\'' in sr: text += '\''
                    elif event.key == K_COMMA and ',' in sr: text += ','
                    elif event.key == K_PERIOD and '.' in sr: text += '.'
                    elif event.key == K_SLASH and '/' in sr: text += '/'
                elif shifted:
                    if event.key == K_a and 'A' in sr: text += 'A'
                    elif event.key == K_b and 'B' in sr: text += 'B'
                    elif event.key == K_c and 'C' in sr: text += 'C'
                    elif event.key == K_d and 'D' in sr: text += 'D'
                    elif event.key == K_e and 'E' in sr: text += 'E'
                    elif event.key == K_f and 'F' in sr: text += 'F'
                    elif event.key == K_g and 'G' in sr: text += 'G'
                    elif event.key == K_h and 'H' in sr: text += 'H'
                    elif event.key == K_i and 'I' in sr: text += 'I'
                    elif event.key == K_j and 'J' in sr: text += 'J'
                    elif event.key == K_k and 'K' in sr: text += 'K'
                    elif event.key == K_l and 'L' in sr: text += 'L'
                    elif event.key == K_m and 'M' in sr: text += 'M'
                    elif event.key == K_n and 'N' in sr: text += 'N'
                    elif event.key == K_o and 'O' in sr: text += 'O'
                    elif event.key == K_p and 'P' in sr: text += 'P'
                    elif event.key == K_q and 'Q' in sr: text += 'Q'
                    elif event.key == K_r and 'R' in sr: text += 'R'
                    elif event.key == K_s and 'S' in sr: text += 'S'
                    elif event.key == K_t and 'T' in sr: text += 'T'
                    elif event.key == K_u and 'U' in sr: text += 'U'
                    elif event.key == K_v and 'V' in sr: text += 'V'
                    elif event.key == K_w and 'W' in sr: text += 'W'
                    elif event.key == K_x and 'X' in sr: text += 'X'
                    elif event.key == K_y and 'Y' in sr: text += 'Y'
                    elif event.key == K_z and 'Z' in sr: text += 'Z'
                    elif event.key == K_0 and ')' in sr: text += ')'
                    elif event.key == K_1 and '!' in sr: text += '!'
                    elif event.key == K_2 and '@' in sr: text += '@'
                    elif event.key == K_3 and '#' in sr: text += '#'
                    elif event.key == K_4 and '$' in sr: text += '$'
                    elif event.key == K_5 and '%' in sr: text += '%'
                    elif event.key == K_6 and '^' in sr: text += '^'
                    elif event.key == K_7 and '&' in sr: text += '&'
                    elif event.key == K_8 and '*' in sr: text += '*'
                    elif event.key == K_9 and '(' in sr: text += '('
                    elif event.key == K_BACKQUOTE and '~' in sr: text += '~'
                    elif event.key == K_MINUS and '_' in sr: text += '_'
                    elif event.key == K_EQUALS and '+' in sr: text += '+'
                    elif event.key == K_LEFTBRACKET and '{' in sr: text += '{'
                    elif event.key == K_RIGHTBRACKET and '}' in sr: text += '}'
                    elif event.key == K_BACKSLASH and '|' in sr: text += '|'
                    elif event.key == K_SEMICOLON and ':' in sr: text += ':'
                    elif event.key == K_QUOTE and '"' in sr: text += '"'
                    elif event.key == K_COMMA and '<' in sr: text += '<'
                    elif event.key == K_PERIOD and '>' in sr: text += '>'
                    elif event.key == K_SLASH and '?' in sr: text += '?'
         
            if event.type == pygame.QUIT:
               run = False
               pygame.quit()
               sys.quit()
               print "quit"
##         elif typing == True and event.type == KEYDOWN:
##            if ctrl == True:
##               ctrl = False
##               if event.key == 48:
##                  text = text + str("*")
##            elif shift == True:
##               shift = False
##               
##               if event.key == 47:
##                  text = text + str("/")
##               if event.key == 57:
##                  text = text + str("(")
##               if event.key == 48:
##                  text = text + str(")")
##               if event.key == 47:
##                  text = text + str("/")
##               if event.key == 61:
##                  text = text + str("+")
##               
##               
##            else:                 
##               print event.key,"-",(pygame.K_KP_PLUS)
##               if event.unicode.isalpha():
##                   text += event.unicode
##                   TYPE_TEXT = font.render(text, True, (0, 128, 0))
##               elif event.key == K_BACKSPACE:
##                   text = text[:-1]
##                   TYPE_TEXT = font.render(text, True, (0, 128, 0))
##               elif event.key == K_RETURN: 
##                   text = ""
##                   TYPE_TEXT = font.render(text, True, (0, 128, 0))
##               elif event.key == pygame.K_1:
##                   
##                  text = text + str(1)
##               elif event.key == pygame.K_2:
##                  text = text + str(2)
##               elif event.key == pygame.K_3:
##                  text = text + str(3)
##               elif event.key == pygame.K_4:
##                  text = text + str(4)
##               elif event.key == pygame.K_5:
##                  text = text + str(5)
##               elif event.key == pygame.K_6:
##                  text = text + str(6)
##               elif event.key == pygame.K_7:
##                  text = text + str(7)
##               elif event.key == pygame.K_8:
##                  text = text + str(8)
##               elif event.key == pygame.K_9:
##                  text = text + str(9)
##               elif event.key == (pygame.K_0):
##                  text = text + str(0)
##               elif event.key == (pygame.K_LEFTPAREN):
##                  text = text + str("(")
##               elif event.key == (pygame.K_RIGHTPAREN):
##                  text = text + str(")")
##               elif event.key == (pygame.K_COMMA):
##                  text = text + str(",")
##               elif event.key == (pygame.K_KP_DIVIDE):
##                  text = text + str("/")
##               elif event.key == (pygame.K_KP_MULTIPLY):
##                  text = text + str("*")
##               elif event.key == 45:
##                  text = text + str("-")
##               elif event.key == (pygame.K_KP_PLUS):
##                  text = text + str("+")
##               elif event.key == (pygame.K_0):
##                  text = text + str("")
##               if event.key == 306:
##                  ctrl = True
##               elif event.key == 304:
##                  shift = True
               
            
            


              
            if event.type == pygame.MOUSEBUTTONDOWN:
               pygame.mixer.music.load("click.wav")
               pygame.mixer.music.play()
               if not TEXT.obj.collidepoint(mouse):
                  typing = False
               if DATE.obj.collidepoint(mouse):
################################################################################################
                  if DATE_clicked == 0: DATE_clicked = 1
                  else: DATE_clicked = 0
####################################################################################################
               elif TIME.obj.collidepoint(mouse):
                   if TIME_clicked == 0: TIME_clicked = 1
                   else: TIME_clicked = 0
####################################################################################################
            
####################################################################################################

####################################################################################################
               elif TEXT.obj.collidepoint(mouse):
                  typing = True

      


               
      if DATE_clicked == 1:
          DATE = Button(str(date.today()))
      if TIME_clicked == 1:
         TIME = Button(str(datetime.datetime.now().time()))
      
      if typing == True:
         TEXT_text = "Typing rule:"+str(text)
         TEXT = Button("")
      else:
         TEXT_text = "Type your rule here:"+str(text)

      
      
      # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
      myfont = pygame.font.SysFont("monospace", 15)

      # render text
      label = myfont.render(TEXT_text, 1, (0,0,0))
      
      
      TIME.draw(screen, mouse, (850,15,120,20), (875,18))
      DATE.draw(screen, mouse, (700,15,100,20), (724,18))
      TEXT.draw(screen, mouse, (30, 980,660,40), (34,983))
      screen.blit(label, (30, 980))
      
      screen.blit(pointer,((mouseX-30),(mouseY-30)))
      pygame.display.update()
      screen.fill(BLACK)
      screen.blit(grid,(0,0))
      
