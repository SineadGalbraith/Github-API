from github import Github
import matplotlib.pyplot as plot
import numpy 
import getpass

print('This program will return details on the user entered.')

term = 'y'
check = 'y'
i = 1
j = 0
k = 0
languages = ['Python', 'Java', 'Javascript', 'C', 'C++', 'C#', 'PHP', 'HTML', 'Other']
colours = ['firebrick', 'orangered', 'darkorange', 'goldenrod', 'gold', 'y', 'yellowgreen', 'darkseagreen', 'seagreen']


username = input('\nPlease enter your github username: ')
password = getpass.getpass('\nPlease enter your password: ', None)

g = Github(username, password)


user = input('\nPlease enter a github username: ')

userDetails = g.get_user(user)
print('Name: ' + userDetails.name)
print('Followers: ' + str(userDetails.followers))
print('Following: ' + str(userDetails.following))
print('Public Repositories: ' + str(userDetails.public_repos))
print('Private Repositories: ' + str(userDetails.total_private_repos))
              
while check == 'y':
    checkData = input('\nDo you wish to see information about the most commonly used languages (y/n): ')
    if checkData == 'n':
        print('Bye!')
        j = 0
        break
    elif checkData == 'y':
        check = 'n'
        j = 1
    else:
        print('Error.')
        check = 'y'
    
def displayAmounts(amounts):
    print('\nThe languages used by ' + userDetails.name + ":")
    x = 0
    while x < len(amounts):
        print(languages[x] + ": " + str(amounts[x]))
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

def displayBarChart():
    wedge = numpy.arange(len(languages))
    bar = plot.bar(wedge, amounts)
    plot.xlabel('Language')
    plot.ylabel('Repositories')
    plot.xticks(wedge, languages,fontsize = 8)
    bar[0].set_color(colours[0])
    bar[1].set_color(colours[1])    
    bar[2].set_color(colours[2]) 
    bar[3].set_color(colours[3]) 
    bar[4].set_color(colours[4]) 
    bar[5].set_color(colours[5]) 
    bar[6].set_color(colours[6]) 
    bar[7].set_color(colours[7]) 
    bar[8].set_color(colours[8]) 
    plot.title("Github API Interrogation")
    plot.show()
  
if check == 'n' and j == 1:
    getLangs(userDetails)      
    displayAmounts(amounts)
    displayBarChart()
    
    
        
    
    
    
        
        

