from flask import Flask
from templates.countdown.countdown import countdown_index

from flask import redirect, url_for
class app :
    def __init__(self) :
        self.flask = Flask(__name__)
        self.flask.add_url_rule("/", view_func=self.Index)
        self.flask.add_url_rule("/CD", endpoint="CD", view_func=countdown_index)

    def Run(self) :
        self.flask.run(debug=True, host="0.0.0.0", port=5000)

    def Destroy(self) :
        pass

    def Index(self) :
        return redirect(url_for("CD"))