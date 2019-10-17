# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    a = 35
    b = 3
    p = 10000019
    m = 10000
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [[] for i in range(m)]

    for cur_query in queries:
        cur_num_hashed = ((a * cur_query.number + b) % p) % m

        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts[cur_num_hashed]:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts[cur_num_hashed].append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts[cur_num_hashed])):
                if contacts[cur_num_hashed][j].number == cur_query.number:
                    contacts[cur_num_hashed].pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts[cur_num_hashed]:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

"""
Sample Inputs:

12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213

8
find 3899442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0

"""
