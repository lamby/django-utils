def get_id_by_nice_name(choices, nice_name):
    for t in choices:
        if t[1] == nice_name:
            return t[0]

    raise Exception('Unknown choice: %s' % nice_name)


def get_choice_by_id(choices, id):
    for t in choices:
        if t[0] == id:
            return t

    raise Exception('Unknown choice: %s' % id)


def get_nice_name_by_id(choices, id):
    for t in choices:
        if t[0] == id:
            return t[1]

    raise Exception('Unknown choice: %s' % id)


def get_short_name_by_id(choices, id):
    for t in choices._choice_dict.keys():
        if id == choices.__getattr__(t) and not id == 99:
            return t

    raise Exception('Unknown choice: %s' % id)


def get_id_by_short_name(choices, short_name):
    return choices._identifier_map[short_name]

def get_short_name_by_nice_name(choices, nice_name):
    for t in choices._triples:
        if t[2] == nice_name:
            return t[1]

    raise Exception('Unknown choice: %s' % nice_name)

def get_short_names(choices):
    return choices._identifier_map.keys()
