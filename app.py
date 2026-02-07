from flask import Flask

class app :
    def __init__(self) :
        self.flask = Flask(__name__)
        self.flask.add_url_rule("/", view_func=self.Index)

    def Run(self) :
        self.flask.run(debug=True, host="0.0.0.0", port=5000)

    def Destroy(self) :
        pass

    def Index(self) :
        return "<h1>Home Page</h1>"