from flask import Flask

class AI :
    def __init__(self) :
        pass

    def Initialize(self) :
        pass

    def Update(self, passthru_prompt : str | None) :
        
        if passthru_prompt == None :
            return
        
        return passthru_prompt + " (ai process)"
        # do something with passthru_prompt...
        
