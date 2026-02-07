
from flask import request, render_template
from ai import AI

def PromptInput(ai_callback) :
    passout_prompt : str | None = None
    if request.method == "POST" :
        passout_prompt = request.form.get("passout_prompt")
        passout_prompt = ai_callback(passout_prompt)

    return render_template("prompt/prompt.html", prev_attempt = passout_prompt)