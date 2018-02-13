import biodiversity


class Bio_acadia_only_test():
    def setUp(self):
        self.pinfo = open("./test-a4/parks-acadia.csv")
        self.sinfo = open("./test-a4/species-acadia.csv")
        self.flora = ("Algae", "Fungi", "Nonvascular Plant", "Vascular Plant")
        self.fauna = (
        "Amphibian", "Bird", "Crab/Lobster/Shrimp", "Fish", "Insect", "Invertebrate", "Mammal", "Reptile", "Slug/Snail",
        "Spider/Scorpion")
        self.test_db = {}

    def test_buid_parks_info(self):
        biodiversity._build_park_name_and_area(self.test_db, self.pinfo)
        assert list(self.test_db.keys())[0] == "Acadia National Park"
        assert list(self.test_db.values())[0][0] == 47390

    def test_add_species(self):
        biodiversity._build_park_name_and_area(self.test_db, self.pinfo)
        biodiversity._add_species(self.test_db, self.sinfo)
        for val in self.test_db.values():
            if val[1]:
                for elem in val[1]:
                    assert elem in self.flora
            elif val[2]:
                for elem in val[2]:
                    assert elem in self.fauna

    def tearDown(self):
        self.pinfo.close()


class Bio_large_test():
    def setUp(self):
        self.pinfo = open("./test-a4/parks.csv")
        self.sinfo = open("./test-a4/species.csv")
        self.test_db = {}
        self.flora = ("Algae", "Fungi", "Nonvascular Plant", "Vascular Plant")
        self.fauna = (
        "Amphibian", "Bird", "Crab/Lobster/Shrimp", "Fish", "Insect", "Invertebrate", "Mammal", "Reptile", "Slug/Snail",
        "Spider/Scorpion")

    def test_buid_parks_info(self):
        biodiversity._build_park_name_and_area(self.test_db, self.pinfo)
        assert "Acadia National Park" in list(self.test_db.keys())
        assert 47390 == self.test_db["Acadia National Park"][0]

    def test_add_species_info(self):
        biodiversity._build_park_name_and_area(self.test_db, self.pinfo)
        biodiversity._add_species(self.test_db, self.sinfo)
        for val in self.test_db.values():
            if val[1]:
                for elem in val[1]:
                    assert elem in self.flora
            elif val[2]:
                for elem in val[2]:
                    assert elem in self.fauna

    def tearDown(self):
        self.pinfo.close()
