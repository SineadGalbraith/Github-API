from github import Github

g = Github()
term = 'y'

while(term == 'y'):
    user = input('\nPlease enter your username: ')

    userDetails = g.get_user(user)
    print('Name: ' + userDetails.name)
    
    term = input('\nCheck another user (y/n):')
    if(term == 'n'):
        break;
    else:
        term = 'y'