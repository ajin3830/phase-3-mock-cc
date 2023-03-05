import statistics
class Restaurant:
    all = []

    def __init__(self, name):
        if isinstance(name, str):
            # this is an edge case: _ here bc we don't wanna change after initialization, 
            # acting almost like a setter, initially we named it then we 
            # don't wanna change it ever afterwards
            self._name = name
            # when a new restaurant is created add it to the list 'all'
            Restaurant.all.append(self)
        else:
            print('The restaurant name must be a string!')
            raise Exception('The restaurant name must be a string!')
        self.reviews = []
        self.customers = []

    @property
    def name(self):
        return self._name
    
    # def get_name(self):
    #     return self._name
    # name = property(get_name) #no setter here

# restaurant = Restaurant('Mels')
# restaurant2 = Restaurant('2')
# restaurant3 = Restaurant('3')
# print(restaurant.name)
# print(Restaurant.all)
# print(Restaurant.name)

    def get_average_rating(self):
        # sum = 0
        # for review in self.reviews:
        #     sum += review.rating
        # ave = sum / len(self.reviews)
        # return ave

        # return sum([review.rating for review in self.reviews]) / len(self.reviews)
        
        return statistics.mean([review.rating for review in self.reviews])

    # @classmethod
    # def get_all_restaurants(cls):
    #     return cls.all

    def get_all_restaurants():
        return Restaurant.all  
    
