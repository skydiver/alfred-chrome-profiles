#!/usr/bin/env python

import os
import json

def get_profiles(path):
  profiles = []
  if os.path.isdir(path) == False:
    return profiles
  folders = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
  for folder in folders:
    file = "{}/{}/Preferences".format(path, folder)
    if folder != 'System Profile' and os.path.isfile(file):
      with open(file) as f:
        data = json.load(f)
        profiles.append(data['profile']['name'])
  return profiles


home = os.path.expanduser("~")

browsers = [
  '/Library/Application Support/Google/Chrome',
  '/Library/Application Support/Google/Chrome Canary',
  '/Library/Application Support/Chromium'
]

for browser in browsers:
  path = "{}/{}".format(home, browser)
  profiles = get_profiles(path)
  print(profiles)
