def _build_park_name_and_area(park_db, pfile):
    """Takes an empty dictionary and buids the park database without any species info.
    Parameters: park_db is an empty dictionary.
                pfile is an open file that contains the park name and area.
    Returns: None
    Pre-conditions: park_db is an empty dictionary.
                    pfile is an open csv file with the park name and area.
    Post-conditions: park_db is no longer empty."""
    assert not park_db
    assert not pfile.closed
    for line in pfile:
        if line.strip()[0] != "#":
            line = line.split(',')
            line = line[0:3]
            park_db[line[0]] = (float(line[2]), [], [])
    pfile.close()
    assert park_db


def _add_species(park_db, sinfo):
    """Takes a dictionary w/ park info and adds the park species.
    Parameters: park_db is an empty dictionary.
                sfile is an open file that contains the park floara and fauna.
    Returns: None
    Pre-conditions: park_db is an dictionary w/ some park info.
                    sfile is an open csv file with the park flora and fauna.
    Post-conditions: park_db has flora and fauna."""
    flora = ("Algae", "Fungi", "Nonvascular Plant", "Vascular Plant")
    fauna = (
        "Amphibian", "Bird", "Crab/Lobster/Shrimp", "Fish", "Insect", "Invertebrate", "Mammal", "Reptile", "Slug/Snail",
        "Spider/Scorpion")
    assert park_db
    assert not sinfo.closed
    keys = park_db.keys()
    for line in sinfo:
        if line[0] != "#":
            line = line.split(',')
            line = line[0:2]
            if line[0] in keys:
                if line[1] in flora:
                    park_db[line[0]][1].append(line[1])
                elif line[1] in fauna:
                    park_db[line[0]][2].append(line[1])
    sinfo.close()


def init():
    """Initializes the park database.
    Returns: Dictionary
    Pre-conditions: program is running
    Post-conditions: A non-empty park database"""
    pinfo = open(input())
    park_db = {}
    _build_park_name_and_area(park_db, pinfo)
    sinfo = open(input())
    _add_species(park_db, sinfo)
    assert park_db
    return park_db


def _compute_per_acre(park_acre, flora_or_fauna):
    """Computes the flora or fauna per acre
    Parameters: park_acre is a number
                flora_or_fauna is a list that can be empty or not.
    Returns: float
    Pre-conditions: park_acre is a number.
                    flora_or_fauna is a list.
    Post-conditions: returns a float."""
    assert isinstance(park_acre, float)
    assert isinstance(flora_or_fauna, list)
    per_acre = len(flora_or_fauna) / park_acre
    assert isinstance(per_acre, float)
    return per_acre


def produce_output_string(park_name, park_db):
    """Generates the string to be printed for a given park.
    Parameters: park_name is a non-empty string.
                park_db is a non-empty database.
    Returns: a string in proper format.
    Pre-conditions: park_name is a non-empty string.
                    park_db is a non-empty dictionary.
    Post-conditions: a non-empty string is returned"""
    assert park_name != ""
    assert park_db
    keys = list(park_db.keys())
    ret_string = ""
    if (park_name not in keys) or (not park_db[park_name][1] and not park_db[park_name][2]):
        ret_string = "{} -- no data available".format(park_name)
    else:
        flora_per_acre = _compute_per_acre(park_db[park_name][0], park_db[park_name][1])
        fauna_per_acre = _compute_per_acre(park_db[park_name][0], park_db[park_name][2])
        ret_string = "{} -- flora: {:f} per acre; fauna: {:f} per acre".format(park_name, flora_per_acre,
                                                                               fauna_per_acre)
    assert ret_string != ""
    return ret_string


def main():
    park_db = init()
    for key in park_db:
        print(produce_output_string(key, park_db))


main()
