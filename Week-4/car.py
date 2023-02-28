class car :
    def __init__(self,model,make,year,engine_capacity):
        self.model = model
        self.make = make
        self.year = year 
        self.engine_capacity = engine_capacity


    def get_model(self):        
        return self.model
    def get_make(self):        
        return self.make
    def get_year(self):        
        return self.year
    def get_engine_capacity(self):        
        return self.engine_capacity
    


Car1 = car("demio","Nissan","2018",1300) 
Car2 = car("hilux","Toyota","2015",3800) 
Car3 = car("passat","VW","2009",2600) 


print(Car1.get_model()) 
print(Car1.get_make()) 
print(Car1.get_year())
print(Car1.get_engine_capacity()) 

print(Car2.get_model()) 
print(Car2.get_make()) 
print(Car2.get_year())
print(Car2.get_engine_capacity()) 


print(Car3.get_model()) 
print(Car3.get_make()) 
print(Car3.get_year())
print(Car3.get_engine_capacity()) 