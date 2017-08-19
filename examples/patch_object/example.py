class Application:
    def get_random_user(self):
        return 10

    def get_next_person(self, user):
        person = self.get_random_user()
        while person in user['people_seen']:
            person = self.get_random_user()
        return person