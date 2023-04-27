from pattern_sarch import searchN, searchKMP, searchKR

class TestNaive:
    def test_simple(self):
        text = "AABBCCDDEEFFGGHHIIJJ"
        word = "HH"
        assert(searchN(word, text)==14)

class TestKMP:
    def test_simple(self):
        text = "AABBCCDDEEFFGGHHIIJJ"
        word = "HH"
        assert(searchKMP(word, text)==14)

class TestKR:
    def test_simple(self):
        text = "AABBCCDDEEFFGGHHIIJJ"
        word = "HH"
        assert(searchKR(word, text)==14)