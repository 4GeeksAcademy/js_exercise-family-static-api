from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random member IDs when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_data = {
            "id": self._generateId(),
            "first_name": member.get("first_name"),
            "last_name": self.last_name,
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers")
        }
        self._members.append(member_data)

    def delete_member(self, id):
        empty_list = []
        for member in self._members:
            if member["id"] != id:
                empty_list.append(member)
        self._members = empty_list

    def update_member(self, member):
        for i, existing_member in enumerate(self._members):
            if existing_member["id"] == member["id"]:
                self._members[i] = member
                break

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done; it returns a list with all the family members
    def get_all_members(self):
        return self._members
