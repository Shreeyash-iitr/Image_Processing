import mahotas


class ZernikeMoments:
    def __init__(self,radius):
        self.radius = radius
        #The larger the radius, the more pixels will be included in the computation.

    def describe(self, image):
        return mahotas.features.zernike_moments(image, self.radius)