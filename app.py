from flask import Flask
from templates.countdown.countdown import countdown_index
from templates.prompt.prompt import PromptInput
from ai import AI

from flask import redirect, url_for
class app :
    def __init__(self) :
        self.flask : Flask = Flask(__name__)
        self.AI : AI = AI()

        self.AI.Initialize()

        self.flask.add_url_rule("/", view_func=self.Index)
        self.flask.add_url_rule("/CD", endpoint="CD", view_func=countdown_index)
        #self.flask.add_url_rule("/Prompt", endpoint="Prompt", view_func=PromptInput, methods=["GET","POST"])
        self.flask.add_url_rule("/Prompt", endpoint="Prompt", view_func=lambda:PromptInput(self.AI.Update), methods=["GET","POST"])

    def Run(self) :
        self.flask.run(debug=True, host="0.0.0.0", port=5000)

    def Destroy(self) :
        pass

    def Index(self) :
        return redirect(url_for("Prompt"))