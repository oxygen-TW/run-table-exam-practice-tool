import logging
import toml
import random
import os

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class QuestionController():
    
    def __init__(self):
        self.dir = ""
        self.title = ""
        self.total = 0
        self.current = 0
        self.Qstack = []

    def load(self, _dir):
        self.dir = _dir
        logging.debug("change dir to " + _dir)

        self.config = toml.load(os.path.join(_dir,"config.toml"))
        self.title = self.config["title"]
        self.answer = self.config["answer"]
        self.total = len(self.answer)

    def next(self):
        if(self.current + 1 > self.total):
            self.current = 1
        else:
            self.current += 1

    def randomNext(self):
        self.current = random.randint(1, self.total)
        self.Qstack.append(self.current)

    def randomBack(self):
        if(len(self.Qstack) < 1):
            return self.current
        self.Qstack.pop()
        self.current = self.Qstack[-1]
    
    def back(self):
        if(self.current - 1 == 0):
            self.current = self.total
        else:
            self.current -= 1

    def getImage(self):
        return "{0}/{1}.jpg".format(self.dir,str(self.current))
    
    def getTitle(self):
        return self.title

    def getAns(self):
        return self.answer[str(self.current)]

    def getNo(self):
        return str(self.current)

    def setCurrentNo(self, no):
        self.current = no

if __name__ == "__main__":
    pass