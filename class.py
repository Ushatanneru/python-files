#creating class and object
class MyClass:
    x=5
p1=MyClass()
print(p1.x)

#using _init_()
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("jhon",36)
print(p1.name)
print(p1.age)

#intance method
#class method
#static methods


#intance method
class Car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)
carObj=Car()
carObj.sample_car_instance_method("hello again!")

carObj2=Car()
carObj.sample_car_instance_method(2)



class CarSample:
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displayCarDetails(self):
        print(self.name)
        print(self.model)
carObj=CarSample("Audi","A5")
carObj.displayCarDetails()

#static method

class StaticClass:
    @staticmethod
    def sample_static_method_addition(x,y):
        return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y
staticObj=StaticClass()
output_add=staticObj.sample_static_method_addition(2,3)
output_mul=staticObj.sample_static_method_addition(2,3)
print(output_add,output_mul)

#class method

class ClassMethodExample:
    classVar1=False
    classVar2="ON"
    @classMethod
    def sample_class_method(cls):
        cls.classVar1=True
        cls.classVar2="OFF"
ClassMethodExample.sample_class_method()
print(ClassMethodExample.classVar1)
print(ClassMethodExample.classVar2)

#instance method-This is used to deal with instance objects.It is usually used to get and set instance objects
#_init()_: a instance method
#any calss you create inside pythonclass is an instance method,unless you specific it with an decorator
#in order to call an instance method you havee to create a object/instance of an class
#__init()__=constructor
#self=current object.

class animal:
    def __init__(self,species,gender):
        self.species=species
        self.gender=gender
animalObj=animal("Dog","Male")
print(animalObj.species)
print(animalObj.gender)


class my_class:
    dummyVar="Test"
    def instance_method_example(self,a):
        print(a)
        print(self.dummyVar)
myclassObj=my_class()
myclassObj.instance_method_example("helo!")

class my_instance_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sample_instance_class(self):
        print(self.a,self.b)

obj=my_instance_class("Cap","IronMan")
obj.sample_instance_class()

#class methods

class ClassMethods:
    @classmethod
    def class_method(cls):
        print("this is class method")
obj=ClassMethods()
obj.class_method()
ClassMethods.class_method()

#static method
#used as utility classes
#self sufficient classes


class StaticMethod:
    @staticmethod
    def static_method():
        print("this is static method")
obj=StaticMethod()
obj.static_method()

StaticMethod.static_method()


#when to use what?

#instance methods-handle instance objects
#static methods-utility classes

class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    @classmethod
    def price(cls,name,year):
        return cls(name,"2022")
Car.price("Audi",2015)

#Car class should have the following attributes and methods
#attributes and methods
#attributes
#color,max_speed,acceleration,tyre_friction,start_engine,current_speed
#methods:
#start_engine:when this method is called should set the value of attribute is_engine_started to True
#which indicates taht the car engine is turned on
#stop_engine:when this method is called should set the value of attribute is_engine_started to False
#which indicates that the car engine is turned off
#wwhen a new car is created the engine should be off by default
#apply _breaks:
#_decrease the current_speed value according to the tyre_friction value
#_current_speed should never go below 0
#sound_horn:
# -print "beep beep" if car engine is on
# -print "car has not started yet" if car engine is off

class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction,current_speed):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.current_speed=current_speed
        self.is_engine_started=False
    def start_engine(self):
        self.is_engine_started=True
    def stop_engine(self):
        self.is_engine_started=False
    def apply_brakes(self):
        if self.current_speed >= self.tyre_friction:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed=0
        print(self.current_speed)
    def sound_horn(self):
        if self.is_engine_started==True:
            print("BEEP BEEP")
        else:
            print("Car has not started")
    def acceleration(self,speed):
        self.speed=speed
        if self.current_speed >= self.max_speed:
            print("max speed reached")
        else:
            self.current_speed += speed
            print(self.current_speed)
obj=Car("pink",120,80,70,80)
obj.start_engine()
obj.sound_horn()
obj.apply_brakes()
obj.stop_engine()
obj.acceleration(30)
obj.sound_horn()




