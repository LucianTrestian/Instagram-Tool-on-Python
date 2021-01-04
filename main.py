from instabot import Bot
from PIL import Image
import os
import time
import random

bot = Bot()

bot.login(username=input("Username="),
          password=input("Password="))


def upload_image():
    bot.upload_photo(path + r'\\' + image,
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
        images = input('Select mode: Solo, Multi, or Back for chose another mode\n').lower()
        if images == 'solo':
            image = input(r'Select image, for example C:\images\image.png -> ')
            comment = input('Comment -> ')
            upload_image()
            choice = input('Continue to upload images ? Yes / No\n').title()
            if choice == "Yes":
                upload_image()
            elif choice == 'No':
                break
        elif images == 'multi':
            print('For start choice folder(path)')
            path = input('Path = ')
            file_list = os.listdir(path)
            print(f'I find {len(file_list)} images.')
            mod = input("Post all images (all) or only a certain number of pictures(certain)\n")
            if mod == "all":
                print(' WARNING, if you have many images, time for post all images can be long')
                comment = input('You chose "all", wanna post all images instance or wait some time\n for chose enter,instance or wait\n').lower()
                if comment == 'instance':
                    sleep = 0
                    n = 0
                    while n != len(file_list):
                        image = file_list[n]
                        upload_image()
                        time.sleep(sleep)
                        n += 1
                elif comment == 'wait':
                    sleep = int(input('Write time in seconds: '))
                    n = 0
                    while n != len(file_list):
                        image = file_list[n]
                        upload_image()
                        time.sleep(sleep)
                        n += 1
            elif mod == 'certain':
                chose_mod = input('You choice "certain" mod, you can chose it with position(for ex. 1 - 10) or named, chose mod\n')
                if chose_mod == 'position':
                    pos = input('Choice position, split it with space( ): ').split(' ')
        elif images == 'back':
            break

    if command == "exit":
        exit()

    if command == 'logout':
        bot.logout()
        bot.login(username=input("Username="),
                  password=input("Password="))
