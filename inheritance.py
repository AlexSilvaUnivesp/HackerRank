class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
        def __init__(self, firstName, lastName, idNumber, scores):
              super().__init__(firstName, lastName, idNumber)
              self.scores = scores

        def calculate(self):
            average = int(sum(self.scores) / len(self.scores))
            match average:
                case average if average in range(90, 101):
                    return "O"
                case average if average in range(80, 90):
                    return "E"
                case average if average in range(70, 80):
                    return "A"
                case average if average in range(55, 70):
                    return "P"
                case average if average in range(40, 55):
                    return "D"
                case average if average in range(0, 40):
                    return "T"
			

firstName = 'Sancho'
lastName = 'Panza'
ID = 4847677
scores = [41, 42, 43, 44, 45, 46, 48]

s = Student(firstName, lastName, ID, scores)
s.printPerson()
print('Grade:', s.calculate())

