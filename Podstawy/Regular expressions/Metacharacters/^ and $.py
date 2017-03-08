#The ^ and $ match the start and end of a string, respectively

import re

pattern = r"^gr.y$"

if re.match(pattern,"grey"):
    print("Match 1")

if re.match(pattern,"gray"):
    print("Match 2")

if re.match(pattern,"stringray"):
    print("Match 3")


#The pattern "^gr.y$" means that the string should start with gr,
#then follow with any character,except a newline, and end with y
