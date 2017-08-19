
def get_random_user():
    return 10


def get_next_person(user):
    person = get_random_user()
    while person in user['people_seen']:
        person = get_random_user()
    return person