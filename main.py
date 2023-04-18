import os

print("My current SHELL path: ", os.environ["SHELL"])
shell_path = os.getenv("SHELL")

if shell_path == "/bin/bash":
    print("Greetings bash!")

else:
    print("HELLO {shell}!")
