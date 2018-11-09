from github import Github
print('This program will return details on the user entered.')
g = Github()
term = 'y'
i = 1
while(term == 'y'):
    i = 1
    user = input('\nPlease enter your username: ')

    userDetails = g.get_user(user)
    print('Name: ' + userDetails.name)
    print('Followers: ' + str(userDetails.followers))
    print('Following: ' + str(userDetails.following))
    print('Public Repositories: ' + str(userDetails.public_repos))
    print('Private Repositories: ' + str(userDetails.total_private_repos))
    
    while(i == 1):
        term = input('\nCheck another user (y/n): ')
        if(term == 'n'):
            break
            i = 0
        elif(term == 'y'):
            term = 'y'
            i = 0
        else:
            print('Error.')
            i = 1
        
            