
def isPalindrome(aString):
    '''
    aString: a string

    Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

    This function takes in a string and returns a boolean.
    '''
    aString = list(aString)
    def letsgo(aString):

        if len(aString) == 2:
            return(aString[0] == aString[1])

        elif len(aString) == 1:
            return True

        else:
            a = aString.pop(0)
            b = aString.pop(len(aString) - 1)
            if a == b:
                return(letsgo(aString))
            else:
                return False

    return letsgo(aString)

print(isPalindrome('abba'))

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.


    If L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2] then the longest run of monotonically increasing numbers in L is [3, 4, 5, 7, 7] and the longest run of monotonically decreasing numbers in L is [10, 4, 3]. Your function should return the value 26 because the longest run of monotonically increasing integers is longer than the longest run of monotonically decreasing numbers.
    If L = [5, 4, 10] then the longest run of monotonically increasing numbers in L is [4, 10] and the longest run of monotonically decreasing numbers in L is [5, 4]. Your function should return the value 9 because the longest run of monotonically decreasing integers occurs before the longest run of monotonically increasing numbers.
    """
    # Your code here
    mono_inc = 0
    mono_longest = 0
    inc_end_idx = 0

    for idx in range(len(L)-1):
        if L[idx] <= L[idx+1]:
            mono_inc += 1
            if mono_inc > mono_longest:
                mono_longest = mono_inc
                inc_end_idx = idx+1
        else:
            mono_inc = 0

    inc_list = []
    for inc_idx in range(inc_end_idx - mono_longest, inc_end_idx+1):
        inc_list.append(L[inc_idx])

    inc = inc_list[:]
    inc_end = inc_end_idx - 0

    mono_inc = 0
    mono_longest = 0
    inc_end_idx = 0

    for idx in range(len(L)-1):
        if L[idx] >= L[idx+1]:
            mono_inc += 1
            if mono_inc > mono_longest:
                mono_longest = mono_inc
                inc_end_idx = idx+1
        else:
            mono_inc = 0

    inc_list = []
    for inc_idx in range(inc_end_idx - mono_longest, inc_end_idx+1):
        inc_list.append(L[inc_idx])

    dec = inc_list[:]
    dec_end = inc_end_idx - 0

    # print(inc_end, dec_end)

    if len(inc) > len(dec):
        return sum(inc)
    elif len(inc) < len(dec):
        return sum(dec)
    else:
        if inc_end > dec_end:
            return(sum(dec))
        else:
            return(sum(inc))

# print(longest_run([3, 2, -1, 2, 7]))


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    Problem 5

    Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

    Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

    intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
    difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
    Here are two examples:

    If f(a, b) returns a + b
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    If f(a, b) returns a > b
    d1 = {1:30, 2:20, 3:30}
    d2 = {1:40, 2:50, 3:60}
    then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
    '''
    # Your code here
    inter = {}
    diff = {}
    for key in d1:
        if key in d2:
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d1[key]

    for key in d2:
        if key not in d1:
            diff[key] = d2[key]

    return(inter, diff)

def f(a,b):
    return a > b

# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#
# print(dict_interdiff(d1, d2))

def q6():
    class Person(object):
        def __init__(self, name):
            self.name = name
        def say(self, stuff):
            return self.name + ' says: ' + stuff
        def __str__(self):
            return self.name

    class Lecturer(Person):
        def lecture(self, stuff):
            return 'I believe that ' + Person.say(self, stuff)

    class Professor(Lecturer):
        def say(self, stuff):
            return self.name + ' says: ' + self.lecture(stuff)

    class ArrogantProfessor(Professor):
        def say(self, stuff):
            return self.name + ' says: It is obvious that ' + self.name + ' says: ' + stuff

        def lecture(self, stuff):
            return 'It is obvious that ' + self.name + ' says: ' + stuff

    e = Person('eric')
    le = Lecturer('eric')
    pe = Professor('eric')
    ae = ArrogantProfessor('eric')

    e.say('the sky is blue')

    le.say('the sky is blue')

    le.lecture('the sky is blue')

    print(pe.say('the sky is blue'))

    print(pe.lecture('the sky is blue'))

    ae.say('the sky is blue')

    ae.lecture('the sky is blue')

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """

        Campus.__init__(self, center_loc)
        self.tent_loc = []
        self.tent_loc.append(tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """

        for tent in self.tent_loc:
            if new_tent_loc.dist_from(tent) < 0.5:
                return False

        self.tent_loc.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """

        try:
            self.tent_loc.remove(tent_loc)
        except ValueError:
            raise ValueError('there is not a tent at tent_loc')

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        return self.tent_loc
