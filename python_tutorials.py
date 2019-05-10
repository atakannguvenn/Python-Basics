
def HelloWorld(myString):
	print ("%s" %myString)
	myName = input("What is your name?\n")
	if (myName == "Atakan"):
		print ("You are correct")
	elif(myName == "Berat"):
		print ("My name is Atakan not %s" %(myName))
	else:
		print ("Hello World")

def add(num1,num2):
	return (num1+num2)

def subs(num1,num2):
	return (num1-num2)

def multi(num1,num2):
	return (num1*num2)

def divide(num1,num2):
	return (num1/num2)

def main():
	choice = int(input("What do you want to do? 1 for + 2 for - 3 for * 4 for /\n"))
	mynum1 = int(input("Please enter a number\n"))
	mynum2 = int(input("Please enter a number\n"))
	if (choice == 1):
		print ("Result is %d" %(add(mynum1,mynum2)))
	elif (choice == 2):
		print ("Result is %d" %(subs(mynum1,mynum2)))
	elif (choice == 3):
		print ("Result is %d" %(multi(mynum1,mynum2)))
	elif (choice == 4):
		print ("Result is %d" %(divide(mynum1,mynum2)))

def ekle():
	array = [23, 28, 29]
	array = array + [39]
	print (array)

def food():
	food = ["hamburger", "pasta", "pizza", "cake", "mushroom"]
	z=0
	while z<4:
		for n in range(5):
			print (food[n])
		print(z)
		z = z + 1
#food()

def div4():
    for x in range(1,101):
        if (x%4==0):
            print (x)

def gender(sex = "Unknown"):
    if sex == 'm':
        sex = "Male"
        print (sex)
    else:
        print (sex)

def sentence(person = "Atakan", action = "ate", item = "tuna"):
    print(person,action,item)


from random import *
import urllib
def download_webimage(url):
    name = randrange(1,1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

download_webimage("https://i.ytimg.com/vi/7SdUB6Va7AY/maxresdefault.jpg")

def readfileyo():
    fp = open("students.txt", "r+")
    fp.write("Wow this is cool dawg!\n")
    fp.close()
    fp = open("students.txt", "r+")
    text = fp.read()
    print(text)
    fp.close()
# readfileyo()

from urllib import request
def downloadyo(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csvstring = str(csv)
    lines = csvstring.split("\\n")
    dest_url = r"goog.csv"
    fx = open(dest_url, "w")
    for z in lines:
        fx.write(z + "\n")
# downloadyo("http://chart.finance.yahoo.com/table.csv?s=GOOG&a=0&b=11&c=2017&d=1&e=11&f=2017&g=d&ignore=.csv")

def exceptyo():

    while True:
        try:
            number = int(input("What's your favorite number bro?\n"))
            print(18/number)
        except ValueError:
            print("I said number.. *sigh*")
        except ZeroDivisionError:
            print("I don't like 0 pick another one")
        finally:
            print("Loop completed")
            break
#exceptyo()

def gamingyo():

    class Enemy:
        life = 2

        def attack(self):
            print("ouch!")
            self.life -= 1

        def checklife(self):
            if self.life <= 0:
                print("RIP")
            else:
                print(str(self.life) + " life left")
    enemy1 = Enemy()
    enemy2 = Enemy()

    enemy1.attack()
    enemy1.checklife()
    enemy2.checklife()

#gamingyo()

def init():

    class Enemy:
        def __init__(self, x):
            self.energy = x
        def get_energy(self):
            print(self.energy)
    jason = Enemy(5)
    sandy = Enemy(10)
    jason.get_energy()
    sandy.get_energy()
#init()

def classvsinst():

    class girl:
        gender = "Female"
        def __init__(self, name):
            self.name = name
    r = girl("Rachel")
    z = girl("Stanky")
    print(r.gender)
    print(z.gender)
    print(r.name)
    print(z.name)
#classvsinst()

def inheritance():

    class parent():

        def print_last_name(self):
            print("Guven")
    class stranger():
        def age(self):
            print("21")
    class child(parent, stranger):
        pass

    atakan = child()
    atakan.print_last_name()
    atakan.age()
#inheritance()

import threading

def threadingyo():
    class AtakanMessenger(threading.Thread):
        def run(self):
            for _ in range(10):
                print(threading.current_thread().getName())
    x = AtakanMessenger(name = "Send out messages")
    y = AtakanMessenger(name = "Receive messages")
    x.start()
    y.start()
#threadingyo()

def unpack():
    date, me, age = ["December 23, 2016", "Atakan", 21]
    print(me)

def drop_first_and_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print("%.1f" %avg)
#drop_first_and_last([10,54,32,90,96])

def zipyo():
    first = ["Atakan", "Tom", "Roger"]
    last = ["Guven", "Marten", "Jenkins"]
    names = zip(first, last)
    for a, b in names:
        print(a, b)

def lambdayo():
    answer = lambda x: x*7
    print(answer(5))

def sorting():
    stocks = {
        'GOOG': 500.35,
        'FB': 75.76,
        'YHOO': 35.43,
        'AMZN': 369.32,
        'AAPL': 99.79
    }
    stocks = sorted(zip(stocks.values(), stocks.keys()))
    stocks.reverse()
    print(stocks)

#sorting()

def pillow():
    from PIL import Image
    from PIL import ImageFilter
    img = Image.open("Data\munamies_j120111pp_vi.jpg")
    print(img.size)
    print(img.mode)
    area = (0, 0, 658, 500)
    cropped_img = img.crop(area)
    print(cropped_img.size)
    r, g, b = img.split()
    new_img = Image.merge("RGB", (b, g, r))
    img2 = Image.open("Data\hqdefault.jpg")
    print(img2.format)
    paste_area = (0, 0, 480, 360)
    new_img.paste(img2, paste_area)
    cropped_img.save("Data\ehuahe.jpg")
    img.save("Data\ehaeuha.jpg")
    new_img = new_img.rotate(22.5)
    new_img = new_img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img = new_img.filter(ImageFilter.DETAIL)
    new_img.save("Data\ehaeuhae.jpg")
    new_img.show()

def structyo():
    import struct
    packet_data = struct.pack("iif", 4, 19, 4.73)
    print(packet_data)
    print(struct.calcsize("iif"))
    print(struct.unpack("iif", packet_data))

def mapyo():
    income = [10, 30, 75]
    double = lambda x: x*2
    new_income = list(map(double, income))
    print(new_income)

def heapqyo():
    import heapq
    grades = [
        {"name" : "Atakan", "grade" : 97},
        {"name" : "Vincent", "grade": 86},
        {"name" : "Leon", "grade": 96},
        {"name" : "Angela", "grade": 90},
        {"name" : "Kevin", "grade": 95},
        {"name" : "Jimari", "grade": 80},
        {"name" : "Andre", "grade": 70}
    ]
    largest_3 = heapq.nlargest(3, grades, key = lambda x: x["grade"])
    for x in largest_3:
        print("Name: %-15s Grade: %3d" % (x["name"], x["grade"]))
    input()
#heapqyo()

def randomnumber():
    import random
    def num_generator():
        nums = []
        for x in range(10):
            nums.append(str(random.randint(1, 99)))
        return nums

    for x in range(10):
        num = num_generator()
        num = " ".join(num)
        print(num)
#randomnumber()

def close_dat():
    import webbrowser, time, os
    webbrowser.open("calc.exe")
    time.sleep(1)
    os.system("taskkill /f /im Calculator.exe")

def utf_8():
    import sys, codecs
    from subprocess import call
    call('chcp 65001', shell=True)
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    a = sys.getdefaultencoding()
    print(a)
    call("", shell=True)
    data = "你好嗎? \n我非常好喔\n"
    print(data)
    input()
