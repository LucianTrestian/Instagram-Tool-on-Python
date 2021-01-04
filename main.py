from instabot import Bot
from PIL import Image
import os
import time
import random

bot = Bot()

bot.login(username=input("Username="),
          password=input("Password="))



def upload_image():
    bot.upload_photo(image,
                     caption=comment)


while True:
    command = input("What you wanna do ?, For help type 'help'\n").lower()
    if command == 'help' or command == '!help':
        print("""
        upload - for upload image
        exit - to shutdown program
        logout - to logout from account
        """)

    while command == 'upload':
        images = input('Select mode: Solo, Multi)\n').lower()
        if images == 'solo':
            image = input(r'Select image, for example C:\images\image.png -> ')
            comment = input('Comment -> ')
            upload_image()
            choice = input('Continue to upload images ? Yes / No\n').title()
            if choice == "Yes":
                upload_image()
            elif choice == 'No':
                break
        elif images == 'Multi':
            print('For start choice folder(path)')
            file_list = os.listdir(input('Path = '))
            mod = input("Post all images (all) or only a certain number of pictures(certain)")
            if mod == "all":
                print(' WARNING, if you have many images, time for post all images can be long')
                comment = input('You chose "all", now select comment for all images\n')
                n = 0
                while n != len(file_list):
                    image = file_list[n]
                    upload_image()
                    n += 1
            elif mod == 'certain':
                chose_mod = input('You choice "certain" mod, you can chose it with position(for ex. 1 - 10) or named, chose mod\n')
                if chose_mod == 'position':
                    pos = input('Choice position, split it with space( ): ').split(' ')
                    while (int(pos[0]) - 1) < 0 and int(pos[1]) - 1 > len(file_list):


    if command == "exit":
        exit()

    if command == 'logout':
        bot.logout()
        bot.login(username=input("Username="),
                  password=input("Password="))
