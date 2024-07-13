'''
school_catalogue.py: defines a superclass and a number of inheriting infraclasses; assigns attributes of validated values;
and defines a number of getter and setter methods

Author: Yesahel Scicluna 

Source: Codecademy. Intermediate Python 3: Object-Oriented Programming. Practice Project - School Catalogue

Task Description: see README.md
'''

# Defines superclass School
class School:

  # Initialises school object with attr values
  def __init__(self, name, level, numberOfStudents):
    '''
    Args:
      name(str): name to assign the school
      level('primary'|'middle'|'high'): education level to assign the school
      numberOfStudents(int >= 0): number of students to assign the school
    
    - Legal args:
        ('adams', 'high', 120)

    - Illegal args:
        (adams, 'high', 120)
        ('adams', 'elementary', 120)
        ('adams', 'high', thirty)
    '''

    # Assigns name arg to .name attr
    if type(name) == str:
      self.name = name.capitalize()
    else:
      raise Exception('name must be a string')

    # Assigns level arg to .level attr
    if type(level) == str and level.lower() in ('primary', 'middle', 'high'):
      self.level = level.capitalize()
    else:
      raise Exception("level must be 'primary', 'middle', or 'high'")

    # Assigns numberOfStudents arg to .numberOfStudents attr
    if type(numberOfStudents) == int:
      if numberOfStudents > -1:
        self.numberOfStudents = numberOfStudents
      else:
        raise Exception('numberOfStudents must be >= 0')
    else:
      raise Exception('numberOfStudents must be a numeric integer')

    
  # Assigns school info to display when obj is printed
  def __repr__(self):
    return '{} {} School | {} students'.format(self.name, self.level, self.numberOfStudents)

  # Gets .name attr
  def getname(self):
    return self.name.capitalize()

  # Gets .level attr
  def getlevel(self):
    return self.level.capitalize()

  # Gets .numberOfStudents attr
  def getnumberOfStudents(self):
    return self.numberOfStudents

  # Assigns new_number arg to .numberOfStudents attr
  def setnumberOfStudents(self, new_number):
    if type(new_number) == int:
      if new_number > -1:
        self.numberOfStudents = new_number
      else:
        raise Exception('numberOfStudents must be >= 0')
    else:
      raise Exception('numberOfStudents must be a numeric integer')



# Defines PrimarySchool, infraclass of School
class PrimarySchool(School):

  # Initialises primary school object with attr values
  def __init__(self, name, numberofStudents, pickupPolicy):
    '''
    Args:
      name(str): name to assign the primary school
      numberOfStudents(int >= 0): number of students to assign the primary school
      pickupPolicy(str): pickup policy to assign the primary school
    '''

    # Passes args to superclass constructor
    # Assigns 'primary' to .level superclass attr
    super().__init__(name, 'primary', numberofStudents)

    # Assigns pickupPolicy arg to .pickupPolicy attr
    if type(pickupPolicy) == str:
      self.pickupPolicy = pickupPolicy
    else:
      raise Exception('pickupPolicy must be a string')

  # Assigns additional info to display when obj is printed
  def __repr__(self):
    return super().__repr__() + ' | ' + self.pickupPolicy

  # Gets .pickupPolicy attr.
  def getpickupPolicy(self):
    return self.pickupPolicy



# Defines HighSchool, infraclass of School   
class HighSchool(School):

  # Initialises high school object with attr values
  def __init__(self, name, numberofStudents, sportsTeams):
    '''
    Args:
      name(str): name to assign the high school
      numberOfStudents(int >= 0): number of students to assign the high school
      sportsTeams(list of str obj): list of sports teams to assign the high school
    '''

    # Passes args to superclass constructor
    # Assigns 'high' to .level superclass attr
    super().__init__(name, 'high', numberofStudents)

    # Assigns sportsTeams arg to .sportsTeams attr
    self.sportsTeams = []
    if type(sportsTeams) == list:
      for team in sportsTeams:
        if type(team) == str:
          self.sportsTeams.append(team)
        else:
          raise Exception('sportsTeams list must only contain strings')
    else:
      raise Exception('sportsTeams must be a list')


  # Assigns additional info to display when obj is printed
  def __repr__(self):
    return super().__repr__() + ' | Sports Teams: ' + ', '.join(self.sportsTeams)

  # Gets .sportsTeams attr.
  def getsportsTeams(self):
    return self.sportsTeams



# TESTS:

s1 = School('abbott', 'middle', 120)
s1.setnumberOfStudents(125)
print(s1, s1.getname(), s1.getlevel(), s1.getnumberOfStudents(), sep = '\n', end = '\n\n')

p1 = PrimarySchool('washington', 150, 'Pickup after 3pm')
print(p1, p1.getname(), p1.getlevel(), p1.getnumberOfStudents(), p1.getpickupPolicy(), sep = '\n', end = '\n\n')

h1 = HighSchool('Lafayette', 175, ['football', 'basketball', 'hockey'])
print(h1, h1.getname(), h1.getlevel(), h1.getnumberOfStudents(), h1.getsportsTeams(), sep = '\n', end = '\n\n')
