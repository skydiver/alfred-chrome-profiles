#!/usr/bin/env python

import os
import json

def get_profiles(path):
  profiles = []
  folders = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
  for folder in folders:
    file = "{}/{}/Preferences".format(path, folder)
    if folder != 'System Profile' and os.path.isfile(file):
      with open(file) as f:
        data = json.load(f)
        profiles.append(data['profile']['name'])
  return profiles


home = os.path.expanduser("~")
path = "{}/Library/Application Support/Google/Chrome".format(home)


profiles = get_profiles(path)
print(profiles)