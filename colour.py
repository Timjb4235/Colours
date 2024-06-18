class Colour:
    def __init__(self, r, g, b, alpha = 1):
        ## Creates a colour instance defined by three integers
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = alpha

    def getRed(self):
        ## Returns a byte value for the red component of a colour instance.
        return self.red
    
    def getGreen(self):
        ## Returns a byte value for the green component of a colour instance. 
        return self.green

    def getBlue(self):
        ## Returns a byte value for the blue component of a colour instance. 
        return self.blue
        
    def toHexString(self):
        ## Converts a set of three byte values to a six character hexadecimal string.
        hex_red = hex(self.r)
        hex_green = hex(self.g)
        hex_blue = hex(self.b)
        return hex_red[2:].zfill(2) + hex_green[2:].zfill(2) + hex_blue[2:].zfill(2)
    
    def lerp(self, second_colour, float):
        ## A float of zero should return the starting colour (self), while a float of 1 should return the second colour (hex_string).
        ## Declaring the change vector from the starting colour to the second colour:
        colour_vector = (second_colour.getRed() - self.getRed(), second_colour.getGreen() - self.getGreen(), second_colour.getBlue() - self.getBlue())
        ## Calculating the rbg vector of the final colour:
        final_colour = (self.getRed() + float * colour_vector[0], self.getGreen() + float * colour_vector[1], self.getBlue() + float * colour_vector[2])
        return Colour(final_colour[0], final_colour[1], final_colour[2])
    
    def create_packed_integer(self):
        ## Packs red, green and blue values into a single packed integer
        return self.red << 24 | self.green << 16 | self.blue << 8 | self.alpha
