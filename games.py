import os
import sys
import time
import random
from sys import platform

try:  
    import keyboard
except ImportError:
    print("You need to install keyboard library for python. You can do it by 'sudo pip install keyboard' or 'pip install keyboard'")
    exit(0)
os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607
 
def to_bold(text):
    return "\033[1m" + text
def to_fast_blinking(text):
    return "\033[6m" + text
def to_slow_blinking(text):
    return "\033[5m" + text
def to_italic(text):
    return "\033[3m" + text
def to_reset_eff(text):
    return "\033[0m" + text
 
def to_blue(text):
    return "\033[34m" + text
def to_red(text):
    return "\033[31m" + text
def to_turquiose(text):
    return "\033[36m" + text
def to_black(text):
    return "\033[30m" + text
def to_white(text):
    return "\033[37m" + text
def to_green(text):
    return "\033[32m" + text
def to_yellow(text):
    return "\033[33m" + text
 
def print_to_xy(x,y,s):
    print("\n"*y+" "*x+s)
def tic_tac_game():
    print_to_xy(20,15,"1. Начать новую игру")
    print_to_xy(20,2,"2. Выйти в меню")
    menu()
def print_snake():
    print(to_green(""))
    print("\033["+str(sn.head[1])+";"+str(sn.head[0])+"H @")
    for i in r(sn.body):
        if sn.direction == 'a':
            print("\033["+str(sn.body[len(sn.body)-1-i][1])+";"+str(sn.body[len(sn.body)-1-i][0])+"H o")
        else:
            print("\033["+str(sn.body[i][1])+";"+str(sn.body[i][0])+"H o")
    if sn.direction == 'a':
        print("\033["+str(sn.head[1])+";"+str(sn.head[0])+"H @") 
    print(to_white(""))
def game_over():
    clear_screen()
    sn.reset()
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=10, cols=50))
    print_to_xy(4,4,"I hope next time you show yourself better")
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=80))
    time.sleep(2)
    snake_game()
def snake_game_update_frame():
    
    clear_screen()
    print("\033["+str(apple.coord_y)+";"+str(apple.coord_x)+"H "+to_red("$"))
    print(to_white(""))
    """
    
    """
    print_snake()
    if sn.head == [apple.coord_x, apple.coord_y]:
        sn.increase_body()
        sn.increase_count()
        apple.generate_food()
        print("\033["+str(apple.coord_y)+";"+str(apple.coord_x)+"H "+to_red("$"))
        
        print(to_white(""))
    if sn.head[0] == 31 or sn.head[0] == 1 or sn.head[1] == 15 or sn.head[1] == 2:
        game_over()
    for i in r(sn.body):
        
        if [sn.head[0],sn.head[1]] == sn.body[i]:
            game_over()
        
        
def r(lst):
    return range(len(lst))
def start_snake():
    
    
    while True:  #making a loop
        print(to_bold(""))

        print("\033[1;13H SCORE:"+to_bold( to_italic( str(sn.get_count()))))
        print("\033[2;0H "+ "+"+"-"*30+"+")
        for i in range(3,15):
            print("\033["+str(i)+";0H "+ "|")
            print("\033["+str(i)+";32H "+ "|")
        print("\033[15;0H "+ "+"+"-"*30+"+")
        print(to_reset_eff(""))
        time.sleep(1/sn.get_speed())
        sn.move()
        snake_game_update_frame()
        try:  #used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("w"):
                
                if sn.direction == 's':
                    pass
                else:
                    sn.change_direction('w')                
                pass
            elif keyboard.is_pressed("a"):
                
                if sn.direction == 'd':
                    pass
                else:
                    sn.change_direction('a')
 
                pass      
 
            elif keyboard.is_pressed("s"):
                
                if sn.direction == 'w':
                    pass
                else:
                    sn.change_direction('s')
 
                pass 
            elif keyboard.is_pressed("d"):
                
                if sn.direction == 'a':
                    sn.change_direction('a')
                else:
                    sn.change_direction('d')
 
                pass   
            elif keyboard.is_pressed("esc"):
                time.sleep(0.1)
                clear_screen()
                sn.reset()
                sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=80))
                snake_game()
                time.sleep(2)
                pass
 
            else:
                pass                
        except:
            pass   
 
class food():
    def __init__(self):
        self.coord_x = 25
        self.coord_y = 9
    def generate_food(self):
            key = True
            while key:
                randx = random.randint(3,28)
                randy = random.randint(3,14)
                for i in r(sn.body):
                        if  (sn.body[i] != [randx,randy]) & (sn.head[0] != [randx,randy]):
                            key = False
            self.coord_x = randx
            self.coord_y = randy
    def print_coord_food(self):
        print(self.coord_x, self.coord_y)
 
class snake():
    def __init__(self):
        self.speed = 6
        self.direction = 'd'
        self.length = 1
        self.count = 0
        self.head = [10,11]
        self.body = [[9,11],[8,11],[7,11],[6,11]]
    def reset(self):
        self.speed = 6
        self.direction = 'd'
        self.length = 1
        self.count = 0
        self.head = [10,11]
        self.body = [[9,11],[8,11],[7,11],[6,11]]
    def get_speed_str(self):
        if self.speed == 3:
            return "SLOW"
        if self.speed == 6:
            return "MEDIUM"
        if self.speed == 9:
            return "FAST"
    def get_speed(self):
       return self.speed
    def increase_decrease_speed(self):
        if self.speed == 9:
            self.speed = 3
        else:
            self.speed += 3
    def reverse_coord_and_direction(self):
        if self.head[0] == 1:
            self.head[0] = 78
        if self.head[0] == 79:
            self.head[0] = 2
        if self.head[1] == 1:
            self.head[1] = 78
        if self.head[1] == 79:
            self.head[1] = 2
    def increase_body(self):
        self.body.append(self.body[-1])
    def get_count(self):
        return self.count
    def increase_count(self):
        self.count += 1
    def getcount():
        return self.count
    def change_direction(self,char):
        self.direction = char
    
    def move(self):
        print(len(self.body))
        for i in range(len(self.body)):
                if  i == len(self.body)-1:
                    self.body[len(self.body)-i-1] = self.head
                else:
                    self.body[len(self.body)-1-i] = self.body[len(self.body)-i-2]
        x = self.head[0]
        y = self.head[1]
        if self.direction == 'd':
            x += 1
            self.head =[x,y]
        if self.direction == 'w':
            y-=1
            self.head =[x,y]
        if self.direction == 'a':
            x-=1
            self.head =[x,y]  
        if self.direction == 's':
            y+=1
            self.head =[x,y]  
sn = snake()
apple = food()
def snake_game(): 
    print_to_xy(20,13,to_white("New game -> press S "))
    print_to_xy(20,1,"[INFO] -- Speed ->" + sn.get_speed_str())
    print_to_xy(20,1,"Change speed -> press C")
    print_to_xy(20,2,"Exit to menu -> press Esc")
    print_to_xy(20,3,to_turquiose(to_italic(to_bold("USE 'WASD' TO CONTROL SNAKE."))))
    print_to_xy(24,1,to_turquiose(to_italic(to_bold("Maybe you need to push keys more than one time for"))))
    print_to_xy(34,1," switch direction of the snake.")
    print("\n"*4)
    while True:  #making a loop
        time.sleep(0.1)
        try:  #used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("s"):
                clear_screen()
                sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=17, cols=33))
                start_snake()
                break
            if keyboard.is_pressed("c"):
                clear_screen()
                print("SPEED IS CHANGED!",end="")
                time.sleep(0.3)
                sn.increase_decrease_speed()
                snake_game()
            if keyboard.is_pressed("esc"):
                clear_screen()
                menu()
                time.sleep(0.4)
                pass
 
            else:
                pass
        except:
            break
 
 
def clear_screen():
    ts = os.get_terminal_size()
    print("\033[H", end = "")
    for i in range(1,ts.lines):
        print(" "*ts.columns)
    print("\033[H", end = "") 
 
def goto_last_string():
    print("b'\x1b[A'")
def hello():
    print(to_white("   d    d d sss   d      d        sSSSs   "))
    print(to_white("   S    S S       S      S       S     S  "))
    print(to_blue("   S    S S       S      S      S       S "))
    print(to_blue("   S sSSS S sSSs  S      S      S       S "))
    print(to_blue("   S    S S       S      S      S       S "))
    print(to_red("   S    S S       S      S       S     S "))
    print(to_red('   P    P P sSSss P sSSs P sSSs   "sss" '))
    print(to_white("\n\n\n"))
    print(to_red("                                  ,,                             "))
    print(to_red("                                `7MM                             "))
    print(to_red("                                  MM                             "))
    print(to_red("`7Mb,od8  .g''Ya   ,6'Yb.    ,M''bMM  `7MMpMMMb.pMMMb.   .gP'Ya  ")) 
    print(to_red("  MM' '' ,M'   Yb 8)   MM  ,AP    MM    MM    MM    MM  ,M'   Yb ")) 
    print(to_red("  MM     8M''''''  ,pm9MM  8MI    MM    MM    MM    MM  8M'''''' "))  
    print(to_red("  MM     YM.    , 8M   MM  `Mb    MM    MM    MM    MM  YM.    , "))  
    print(to_red(".JMML.    `Mbmmd' `Moo9^Yo. `Wbmd'MML..JMML  JMML  JMML. `Mbmmd' "))  
  
    print(to_white("\n\n\n"))                 
    print("If you run program on linux without sudo keyboard library cant work, please run program with SUDO!!")
    print("Make sure that the program run with sudo and console is not in full screen mode and press ENTER:\n")
    print("For exit program print 'e'")
    print("\n\n\n*Console will be cleared!")
    y = input()
    if y == 'e':
        exit()
    clear_screen()
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=80))
def print_menu():
    print("\n"*4)
    print(to_turquiose(to_fast_blinking(" "*24+" _______  _______  _                ")))
    print(" "*24+"(       )(  ____ \( (    /||\     /|")
    print(" "*24+"| () () || (    \/|  \  ( || )   ( |")
    print(" "*24+"| || || || (__    |   \ | || |   | |")
    print(" "*24+"| |(_)| ||  __)   | (\ \) || |   | |")
    print(" "*24+"| |   | || (      | | \   || |   | |")
    print(" "*24+"| )   ( || (____/\| )  \  || (___) |")
    print(" "*24+"|/     \|(_______/|/    )_)(_______)")
    print(to_reset_eff(to_green("\n"*4+" "*35+"1. SNAKE GAME")))
    
    print_to_xy(35,2,"2. EXIT")
    print("\n"*12)


def menu():
 
    print_menu()
    while True: 
        time.sleep(0.1)#making a loop
        try:  #used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("1"):
                clear_screen()
                snake_game()
                break
            if keyboard.is_pressed("2"):
                clear_screen()
                print(to_white("GOODBYE!"))
                if platform == "linux" or platform == "linux2":
                    print(os.popen('pkill python').read())
                elif platform == "win32":
                    print(os.popen('taskkill /f /im cmd.exe').read())
                
                break
            else:
                pass
        except:
            pass  
print(to_white("\n\n\n"))
 
#row_s, columns = os.popen('stty size', 'r').read().split()
 
hello()
 
 
menu()
 
