class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and 1<= len(first_name)<= 25:
            self._first_name = first_name
        else:
            print('Your first name must be a string and contain between 1 and 25 letters, inclusive!')
            
            raise Exception('Your first name must be a string and contain between 1 and 25 letters, inclusive!')

    # @property
    # def last_name(self):
    #     return self._last_name
    # @last_name.setter
    # def last_name(self, last_name):
    #     if isinstance(last_name, str) and 1<= len(last_name)<= 25:
    #         self._last_name = last_name
    #     else:
    #         print('Your last name must be a string and contain between 1 and 25 letters, inclusive!')
            
    #         raise Exception('Your last name must be a string and contain between 1 and 25 letters, inclusive!')
    
    # def get_first_name(self):
    #     return self._first_name
    # def set_first_name(self, first_name):
    #     if isinstance(first_name, str) and 1<= len(first_name)<= 25:
    #         self._first_name = first_name
    #     else:
    #         print('Your first name must be a string and contain between 1 and 25 letters, inclusive!')
            
    #         raise Exception('Your first name must be a string and contain between 1 and 25 letters, inclusive!')
    
    # first_name = property(get_first_name, set_first_name)


    def get_last_name(self):
        return self._last_name
    def set_last_name(self, last_name):
        if isinstance(last_name, str) and 1<= len(last_name)<= 25:
            self._last_name = last_name
        else:
            print('Your last name must be a string and contain between 1 and 25 letters, inclusive!')
            
            raise Exception('Your last name must be a string and contain between 1 and 25 letters, inclusive!')
        
    last_name = property(get_last_name, set_last_name)

    def get_full_name(self):
        return f'{self._first_name} {self._last_name}'
        # return self._first_name+ ' ' +self._last_name
    
# aj = Customer('AJ', 'AJ')
# print(aj.get_first_name())
# print(aj.get_full_name())

    def get_num_reviews(self):
        return len(self.reviews)
        
    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        # ^Review class gets imported here 
        Review(self, restaurant, rating)
        # when add_review method runs a review instance is created 
        # and everythin inside Review class init will run
