import matplotlib.pyplot as plt

class PlotVectors:
    """PLotting several vectors in cartesian coordinate system"""
    
    def __init__(self, *vectors) -> None:
        X, Y = [], []

        for vector in vectors:
            X.append(vector[0])
            Y.append(vector[1])

        self.X, self.Y = X, Y # tuple unpacking
        self.originX = self.originY = tuple(0 for _ in range(len(X)))

    def plot(self) -> None:
        """Visiualize vectors"""



        plt.quiver(self.originX, self.originY, self.X, self.Y, scale=1, scale_units="xy", angles="xy")
        
        plt.show(0)