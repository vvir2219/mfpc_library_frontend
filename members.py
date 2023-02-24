from api import api_members

def member_repr(member):
    return f"\nId: {member['id']}\nName: {member['name']}"

def create_member(name):
    return api_members.post(
        body={
            'name': name
        })

