from instabot import Bot
from PIL import Image
import glob
import time
import random

bot = Bot()

bot.login(username=input("Username="),
          password=input("Password="))


def upload_image():
    bot.upload_photo(image_list[int(input('Chosen image: ')) - 1],
                     caption=input('Comment: '))


while True:
    command = input("What you wanna do ?, For help type 'help'\n").lower()
    if command == 'help' or command == '!help':
        print("""
        upload - for upload image
        exit - to shutdown program
        logout - to logout from account
        """)

    while command == 'upload':
        print('From where you wanna post images ? (one the end write *.format, format for example jpg, png, gif)')
        print('For example "F:/Photoshop/Wallpapers/*.jpg"')
        path = input('Path = ')
        image_list = []
        for filename in glob.glob(path):
            im = Image.open(filename)
            image_list.append(im)
        images = input('One images or more ? (one - for one images, more - for more)\n').lower()
        if images == 'one':
            upload_image()
            choice = input('Continue to upload images ? Yes / No\n').title()
            if choice == "Yes":
                upload_image()
            elif choice == 'No':
                break
        elif images == 'more':
            upload_image()

    if command == "exit":
        exit()

    if command == 'logout':
        bot.logout()
        bot.login(username=input("Username="),
                  password=input("Password="))
