# get choices

def get_choice_by_id(choices, id):
    for t in choices:
        if t[0] == id:
            return t

    raise Exception('Unknown choice: %s' % id)


# get ids

def get_ids(choices):
    return choices._display_map.keys()

def get_id_by_short_name(choices, short_name):
    try:
        return choices._identifier_map[short_name]
    except:
        raise Exception('Unknown choice: %s' % short_name)

def get_id_by_nice_name(choices, nice_name):
    for t in choices._doubles:
        if t[1] == nice_name:
            return t[0]

    raise Exception('Unknown choice: %s' % nice_name)


# get short names

def get_short_names(choices):
    return choices._identifier_map.keys()
    
def get_short_name_by_id(choices, id):
    for t in choices._triples:
        if t[0] == id:
            return t[1]

    raise Exception('Unknown choice: %s' % id)
    
def get_short_name_by_nice_name(choices, nice_name):
    for t in choices._triples:
        if t[2] == nice_name:
            return t[1]

    raise Exception('Unknown choice: %s' % nice_name)


# get nice names

def get_nice_names(choices):
    return choices._display_method.values()

def get_nice_name_by_id(choices, id):
    try:
        return choices._display_map[id]
    except:
        raise Exception('Unknown choice: %s' % id)
        
        
def get_nice_name_by_short_name(choices, short_name):
    for t in choices._triples:
        if t[1] == short_name:
            return t[2]

    raise Exception('Unknown choice: %s' % short_name)










