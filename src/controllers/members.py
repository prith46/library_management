from src.models.models import Library


class Members:
    def __init__(self):
        self.member = Library()

    def add_member(self, member_id, name, phone):
        query = (f'INSERT INTO members (member_id, name, phone) '
                 f'VALUES ({member_id}, \'{name}\', {phone} );')
        self.member.add_member_db(query)

    def get_all_members(self):
        return self.member.get_all_members_db()

    def delete_member(self, name):
        self.member.delete_members_db(name)


mem = Members()
mem.add_member(1, 'prith', 263587)
print(mem.get_all_members())
mem.delete_member('prith')
