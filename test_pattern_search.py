from pattern_sarch import searchN, searchKMP, searchKR

def simple(func):
    """Prosty test"""
    text = "AABBCCDDEEFFGGHHIIJJ"
    assert(func("HH", text)==[14])
    assert(func("LL", text)==[])

def empty(func):
        """Test z pustymi stringami"""
        text = "AABBCCDDEEFFGGHHIIJJ"
        assert(func("", text)==[])
        assert(func("", "")==[])

def equal(func):
        """Test stringów równej długości"""
        text = "AABBCCDDEEFFGGHHIIJJ"
        assert(func(text, text)==[0])
        assert(func("AAGGCCDDEEFFGGHHLLJJ", text)==[])

def longer(func):
        """Test z dłuższym słowem niż tekstem"""
        text = "AABBCCDDEEFFGGHHIIJJ"
        word = "AABBCCDDEEFFGGHHIIJJKK"
        assert(func(word, text)==[])

class TestNaive:
    def test_simple(self):
        simple(searchN)
    
    def test_empty(self):
        empty(searchN)

    def test_equal(self):
        equal(searchN)

    def test_longer(self):
        longer(searchN)


class TestKMP:
    def test_simple(self):
        simple(searchKMP)
    
    def test_empty(self):
        empty(searchKMP)

    def test_equal(self):
        equal(searchKMP)

    def test_longer(self):
        longer(searchKMP)

class TestKR:
    def test_simple(self):
        simple(searchKR)
    
    def test_empty(self):
        empty(searchKR)

    def test_equal(self):
        equal(searchKR)

    def test_longer(self):
        longer(searchKR)
        