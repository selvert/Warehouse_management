from django.contrib.auth.models import Group

def Role(User, GroupName):
    try:
        group = Group.objects.get(name=groupName)
        return True if group in user.groups.all() else False
    except:
        return False
