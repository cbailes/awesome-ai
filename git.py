import os

print('Preparing to push local files to remote repository. Enter GitHub password.')
pw = input()

if len(pw) > 5:

    print('Enter a description for your changes')
    message = input()
    os.system('git add -A')
    os.system('git commit -m ' + '"' + message +'"')
    os.system('git push https://cbailes:' + str(pw) + '@github.com/cbailes/awesome-ai.git')
