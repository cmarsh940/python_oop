class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price, max_speed, init_miles=0):
		self.price = price
		self.max_speed = max_speed
		self.init_miles = 0

	def displayinfo(self):
		return "price: {} max_speed: {} init_miles {}".format(
			self.price,
			self.max_speed,
			self.init_miles
		)


	def ride(self):
		return "Riding"
		self.init_miles += 10
		return self

	def reverse(self):
		return "Reversing 5 miles"
		self.init_miles -= 5
        # if self.init_miles < 0:
	       #  print "You can't go under 0 miles!"
	       #  self.init_miles = 0



bike1 = Bike(200, "25 MPH", 0)
bike2 = Bike(10, "15 MPH", 10)
bike3 = Bike(300, "35 MPH", 5)
bike4 = Bike(200, "25 MPH", 0)


#bike1 and bike4 are equivalent after method calls, proof of chaining methods.
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike4.ride().ride().ride().reverse().displayinfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()