class bike:
    def __init__(self,wheel,diskbreak,engine):
        self.wheels = wheel
        self.diskbreaks = diskbreak
        self.enginetype = engine

        def enginetype(self):
            print("wheels:{}, diskbreaks:{}, enginetype:{}".format(wheel,diskbreak,engine))

bike = bike(2,4,"Petrol")
print(bike.diskbreaks, bike.enginetype, bike.wheels,  sep=', ')






