

def prePrcessLcoal(local):
    newLocal = local.replace(".", "")
    if (newLocal.find('+') == -1):
        return newLocal
    else:
        plusindex = newLocal.find('+')
        return newLocal[:plusindex]

emails = ["a@gmail.com", "b+@gmail.com", "b/3@gmail.com" , "b@gmail..com", "b@gmail.com.com", "b@gmail"]
#emails = ['a.b@example.com', 'x@example.com', 'ab+1@example.com', 'y@example.com', 'y@example.com', 'y@example.com', ]

local_list = []
domain_list = []
newEmails = []
for email in emails:
    local, domain = email.split("@")
    local = prePrcessLcoal(local)
    newEmails.append(local+"@"+domain)

my_dict = {i:newEmails.count(i) for i in newEmails}

counter  = 0
for k,v in my_dict.items():
    if v > 1:
        counter = counter +1
print(counter)
