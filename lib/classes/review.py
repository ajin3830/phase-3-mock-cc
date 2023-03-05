from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        # with every review created
        self.add_customer_to_restaurant()
        self.add_review_to_restaurant()
        self.add_review_to_customer()
        self.add_restaurant_to_customer()

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else: 
            print('Customer is not an instance of class Customer!')
            raise Exception('Customer is not an instance of Customer!')
    
    def get_restaurant(self):
        return self._restaurant
    def set_restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            print('Restaurant is not an instance of class Restaurant!')
            raise Exception('Restaurant is not an instance of class Restaurant!')
        
    restaurant = property(get_restaurant, set_restaurant)

    # def get_rating(self):
    #     return self._rating
    # def set_rating(self, rating):
    #     if 0< rating <6:
    #         self._rating = rating
    #     else:
    #         print('Your rating must be a number between 1 and 5, inclusive')
    #         raise Exception('Your rating must be a number between 1 and 5, inclusive')
        
    # rating = property(get_rating, set_rating)

    @property
    def rating(self):
        return  self._rating
    @rating.setter
    def rating(self, rating):
        if 0< rating <6:
            self._rating = rating
        else:
            print('Your rating must be a number between 1 and 5, inclusive')
            raise Exception('Your rating must be a number between 1 and 5, inclusive')

    def add_customer_to_restaurant(self):
        if self.customer not in self._restaurant.customers:
            self._restaurant.customers.append(self.customer)
            # inside review, grab single restaurant, then its customers list 
            # initialized in class Restaurant

    def add_review_to_restaurant(self):
        self._restaurant.reviews.append(self)

    def add_restaurant_to_customer(self):
        if self._restaurant not in self._customer.restaurants:
            self._customer.restaurants.append(self._restaurant)

    def add_review_to_customer(self):
        self._customer.reviews.append(self)
