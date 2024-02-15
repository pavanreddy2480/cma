import random
import matplotlib.pyplot as plt

class Dice():
    def __init__(self,args=None) -> None:
        if args is not None:
            if isinstance(args,int):
                if args>4:
                    self.numSides=args
                else:
                    raise ValueError('Input value must be greater than 4')
            else:
                raise Exception('Invalid input type. Integer expected.')
        else:
            self.numSides=6 #default number of sides for dice
        self.prob=(1/6 for i in range(0,self.numSides))

    def setProb(self,arg):
        if  len(arg)==self.numSides and all([isinstance(i,float) for i in arg]):
            p=0
            for i in arg:
                p+=i
            if p==1:
                self.prob=arg
            else:
                raise Exception('Invalid probability values')
        else:
            raise Exception('Invalid input')
        
    def __str__(self) -> str:
        s= f'Dice with {self.numSides} faces and probability distribution {self.prob}'
        return s
    
    
    def rolls(self):
           return random.choices(range(1,self.numSides+1),weights=self.prob)[0] 
    
    def roll(self,arg):
        if arg<0:
            raise Exception('Invalid argument')
        
        
        results = {face: 0 for face in range(1, self.numSides+1)}

        for _ in range(arg):
            result = self.rolls()
            results[result] += 1

        # Print the results
        faces = list(results.keys())
        counts = list(results.values())
        onemore=[int(((self.prob)[i-1])*arg) for i in range(1,self.numSides+1)]
        bar_wide=0.30

        # Create a bar graph
        plt.bar(faces, counts, color='skyblue')
        faces=[i+bar_wide for i in faces]
        plt.bar(faces, onemore, color='red')

        # Add labels and title
        plt.xlabel('Face')
        plt.ylabel('Occurrences')
        plt.title('Biased Die Simulation Results')

        # Display the graph
        plt.show()
        


d=Dice(5)
d.setProb((0.2,0.3,0.1,0.1,0.3))
d.roll(10000)