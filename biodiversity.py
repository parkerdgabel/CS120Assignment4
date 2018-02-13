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
            park_db[line[0]] = (int(line[2]), [], [])
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
    return park_db

def main():
    park_db = init()

main()