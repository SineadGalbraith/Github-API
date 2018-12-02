from github import Github
from github import GithubException
import matplotlib.pyplot as plot
import numpy
import getpass
import json

username = input('\nPlease enter your github username: ')
password = getpass.getpass('\nPlease enter your password: ', None)

g = Github(username,password)


user = input('\nPlease enter a github username: ')
userDetails = g.get_user(user)

languages = ['Python', 'Java', 'Javascript', 'C', 'C++', 'C#', 'PHP', 'HTML', 'Other']

def getLangs(userDetails):
    
    py = 0
    java = 0
    javas = 0
    c = 0
    cpp = 0
    cs = 0
    php = 0
    html = 0
    other = 0

    repos = userDetails.get_repos()
    for repo in repos:
        if repo.language == languages[0]:
            py = py+1
        elif repo.language == languages[1]:
            java = java+1
        elif repo.language == languages[2]:
            javas = javas+1
        elif repo.language == languages[3]:
            c = c+1
        elif repo.language == languages[4]:
            cpp = cpp+1
        elif repo.language == languages[5]:
            cs = cs+1
        elif repo.language == languages[6]:
            php = php+1
        elif repo.language == languages[7]:
            html = html+1
        else:
            other = other+1
            
    global amounts
    amounts = [py,java,javas,c,cpp,cs,php,html,other]

getLangs(userDetails)

with open('Languages.json', 'w') as output:
    json.dump(languages,output)
with open('Amounts.json', 'w') as output2:
    json.dump(amounts,output2)

