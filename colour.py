class Colour:
    def __init__(self, r, g, b, alpha = 1):
        ## Creates a colour instance defined by three integers
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = alpha
        
    def toHexString(self):
        ## Converts a set of three byte values to a six character hexadecimal string.
        hex_red = hex(self.red)
        hex_green = hex(self.green)
        hex_blue = hex(self.blue)
        return hex_red[2:].zfill(2) + hex_green[2:].zfill(2) + hex_blue[2:].zfill(2)
    
    def lerp(self, second_colour, float):
        ## A float of zero should return the starting colour (self), while a float of 1 should return the second colour (hex_string).
        ## Declaring the change vector from the starting colour to the second colour:
        colour_vector = (second_colour.red - self.red, second_colour.green - self.green, second_colour.blue - self.blue)
        ## Calculating the rbg vector of the final colour:
        final_colour = (self.red + float * colour_vector[0], self.green + float * colour_vector[1], self.blue + float * colour_vector[2])
        return Colour(final_colour[0], final_colour[1], final_colour[2])
    
    def create_packed_integer(self):
        ## Packs red, green and blue values into a single packed integer
        return self.red << 24 | self.green << 16 | self.blue << 8 | self.alpha
