    # -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:19:01 2020

@author: Kirsch
"""

from __init__ import create_app



#Run the application

application = create_app()

if __name__ == "__main__":
    # Execute only if run as a script
    application.run()


