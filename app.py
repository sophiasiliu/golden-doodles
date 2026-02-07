from flask import Flask

class app :
    def __init__(self) :
        self.flask = Flask(__name__)

    def Run(self) :
        self.flask.run()

    def Destroy(self) :
        pass