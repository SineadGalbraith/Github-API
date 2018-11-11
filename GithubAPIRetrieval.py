from github import Github
import matplotlib.pyplot as plot
import numpy 
print('This program will return details on the user entered.')
g = Github()
term = 'y'
check = 'y'
i = 1
j = 0
k = 0
languages = ['Python', 'Java', 'Javascript', 'C', 'C++', 'C#', 'PHP', 'HTML', 'Other']
amounts = []

user = input('\nPlease enter your username: ')

userDetails = g.get_user(user)
print('Name: ' + userDetails.name)
print('Followers: ' + str(userDetails.followers))
print('Following: ' + str(userDetails.following))
print('Public Repositories: ' + str(userDetails.public_repos))
print('Private Repositories: ' + str(userDetails.total_private_repos))
              
while check == 'y':
    checkData = input('\nDo you wish to see information about the most commonly used languages (y/n): ')
    if checkData == 'n':
        j = 0
        break
    elif checkData == 'y':
        print('\nGreat!')
        check = 'n'
        j = 1
    else:
        print('Error.')
        check = 'y'
        
def checkAnother():
    i = 1
    while i == 1:
        term = input('\nCheck another user (y/n): ')
        if term == 'n':
            i = 0
            break
        elif term == 'y':
            term = 'y'
            i = 0
        else:
            print('Error.')
            i = 1

        
def displayAmounts(amounts):
    x = 0
    while x < len(amounts):
        print(languages[x] + ":" + str(amounts[x]))
        x=x+1
            
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
  
  
if check == 'n' and j == 1:
    getLangs(userDetails)      
    displayAmounts(amounts)
    checkAnother()
    
        
    
    
    
        
        

