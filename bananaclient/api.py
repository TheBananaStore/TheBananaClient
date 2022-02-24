from urllib.request import urlopen
import json
import random

class Appbase():
    def __init__(self,  baseurl: str):
        if not baseurl.endswith("/"):
            baseurl = self.baseurl+"/"
            
        self.baseurl = baseurl
        self.index = None
        
    def get_index(self):

        self.index = json.loads(urlopen(self.baseurl+"index.json").read())
        
        
    def get_applist(self):
        if self.index == None:
            return 
        elif type(self.index) == dict:
            self.applist = self.index["apps"]
            random.shuffle(self.apps) # ALWAYS shuffle
            
