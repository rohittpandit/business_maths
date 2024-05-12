class Indices:
    def pow(self, base, power):
        b = base
        if power != int(power):
            for i in range(12):
                base = base ** 0.5
            base = (((base -1)*power)+1)

            for i in range(12):
                base = base * base
            
           
        else:
            for i in range(power-1):
                base = base * b
        return base
    
    def root(self, base, power):
        for i in range(12):
            base = base ** 0.5
        base = (((base -1)/power)+1)

        for i in range(12):
            base = base * base
        
        return base
    

instance1 = Indices()
print(instance1.pow(2,2))
print(instance1.root(9,2))
                

