from pattern_sarch import searchN, searchKMP, searchKR
from random import choice

def simple(func):
    """Prosty test"""
    text = "AABBCCDDEEFFGGHHIIJJ"
    assert(func("HH", text)==[14])
    assert(func("LL", text)==[])
    text = "my uncle's favorite pastime was building cars out of noodles. \
    flying fish flew by the space station. \
    i met an interesting turtle while the song on the radio blasted away. \
    he found a leprechaun in his walnut shell. \
    she only paints with bold colors; she does not like pastels."
    assert(func("my", text)==[0])
    assert(func("interesting", text)==[118])
    assert(func("pastels", text)==[282])

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

def multiple(func):
    """Test z wieloma wystąpnieniami"""
    text = "AABBAACCDDEEFFGGHHAAIIJJ"
    assert(func("AA", text)==[0, 4, 18])
    text = "my uncle's favorite fish pastime was building cars out of noodles. \
    flying fish flew by the space station. \
    i met an interesting turtle fish while the song on the radio blasted away. \
    he found a leprechaun fish in his walnut shell. \
    she only paints with bold colors; she does not like fish pastels."
    assert(func(".", text)==[65, 108, 187, 239, 309])
    assert(func("fish", text)==[20, 78, 142, 215, 297])

def test_random():
    for __ in range(10):
        alphabet = ['a', 'b']
        text = ""
        for _ in range(200):
            text+=(choice(alphabet))
        assert(searchKMP("ab", text)==searchN("ab", text))


class TestNaive:
    def test_simple(self):
        simple(searchN)
    
    def test_empty(self):
        empty(searchN)

    def test_equal(self):
        equal(searchN)

    def test_longer(self):
        longer(searchN)
    
    def test_multiple(self):
        multiple(searchN)


class TestKMP:
    def test_simple(self):
        simple(searchKMP)
    
    def test_empty(self):
        empty(searchKMP)

    def test_equal(self):
        equal(searchKMP)

    def test_longer(self):
        longer(searchKMP)
    
    def test_multiple(self):
        multiple(searchKMP)

class TestKR:
    def test_simple(self):
        simple(searchKR)
    
    def test_empty(self):
        empty(searchKR)

    def test_equal(self):
        equal(searchKR)

    def test_longer(self):
        longer(searchKR)
    
    def test_multiple(self):
        multiple(searchKR)
        