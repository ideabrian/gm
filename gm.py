#!/usr/bin/env python
import clipboard
import webbrowser
import requests
import json
from subprocess import check_call
import sys

def openURL(url=''):
  ''' Open a URL if there's any on your clipboard'''
  print(sys.platform)
  webbrowser.open(clipboard.paste().strip())
  print(f'on clipboard: {clipboard.paste().strip()}')

def copy2clip(txt):
  ''' Put something on your Mac OS clipboard '''
  cmd='echo '+txt.strip()+'|pbcopy'
  return check_call(cmd, shell=True)

def get_menu_item():
  menu_choice = input("\nWhat would you like to do?")
  print(f"You chose item: {menu_choice}")
  return menu_choice

def menu():
  ''' Show a list of menu items '''
  
  
  menu_items = [
    'Write something!',
    'Code something!',
    'Tweet something!',
    'DM somebody!',
    'See a Trello Board',
    'Distract / Inspire / Chill',
    'CRM Something',
  ]
  # put URLs in the second field of each array
  action_links = [
    ['Write something', 'https://750words.com/auth'],
    ['Code something', 'code_action_link'],
    ['Tweet something!', "tweet_action_link"],
    ['DM somebody!', 'https://twitter.com/messages'],
    ['See a Trello Board', 'trello_action_link'],
    ['Inspire / Chill', 'chill_action_link'],
    ['CRM something', 'https://crowdtamers.com/your-first-cold-email-crm-should-be-google-sheets-really/'],
  ]
  
  for idx, item in enumerate(menu_items):
    print(f'{idx}. {item}')
  
  choice = int(get_menu_item())
  print(f"Click here to {menu_items[choice]}")
  print("Check your clipboard!")
  action_link = action_links[choice][1]
  copy2clip(action_link)
  openURL()

def main():
  print("gm! " )
  menu()

if __name__ == "__main__":
  main()
