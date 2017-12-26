


def auth_user(username, email):
    print "OK"




data = {'username' : 'monkey', 'email' : 'monkey@gmail.com'}

#auth_user(data['username'], data['email'])
auth_user(**data)
