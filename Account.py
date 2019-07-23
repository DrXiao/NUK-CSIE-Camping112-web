import io

def register_new(account,password):
    fptr = open('OurMember.txt','a')
    print('%-20s%-20s'%(account,password),file = fptr)
    fptr.close()

def login_test(account_login,password_login):
    fptr = open('OurMember.txt','r')
    str = [] 
    str = fptr.readlines()
    for i in range(len(str)):
        account,password = str[i].split()
        if account == account_login:
            if password == password_login:
                return True
            else:
                return False
        else:
            continue
    fptr.close()
    return False