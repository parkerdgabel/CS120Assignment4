def _build_species_db(species_db, sinfo):
    """Takes an empty dictionary and buids the species database.
    Parameters: species_db is an empty dictionary.
                sinfo is an open file that contains the park name and area.
    Returns: None
    Pre-conditions: species_db is an empty dictionary.
                    sinfo is an open csv file with the park name and area.
    Post-conditions: species_db is no longer empty."""
    assert not species_db
    assert not sinfo.closed
    for line in sinfo:
        if line[0] != "#":
            line = line.split(",")[0:3]
            if line[2].lower() not in species_db:
                species_db[line[2]] = set()
            species_db[line[2]].add(line[0].lower())
    sinfo.close()
    assert species_db
