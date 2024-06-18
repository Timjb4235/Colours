class Colour {
    constructor(r, g, b, alpha = 1) {
        // Creates a colour instance defined by three integers
        this.red = r;
        this.green = green;
        this.blue = blue;
        this.alpha = alpha;
    }

    toHexString(){
        // Converts a set of three byte values to a six character hexadecimal string.
        const hexRed =  this.red.toString(16);
        const hexGreen =  this.green.toString(16);
        const hexBlue =  this.blue.toString(16);
        return hexRed.padStart(2,"0") + hexGreen.padStart(2,"0") + hexBlue.padStart(2,"0");
    }

    lerp(secondColour, float) {
        // A float of zero should return the starting colour (this), while a float of 1 should return the second colour.
        // Declaring the change vector from the starting colour to the second colour:
        const colourVector = [secondColour.red - this.red, secondColour.green - this.green, secondColour.blue - this.blue];
        // Calculating the rbg vector of the final colour:
        const finalColour = [self.red + float * colourVector[0], self.green + float * colourVector[1], self.blue + float * colourVector[2]];
        return new Colour(finalColour[0], finalColour[1], finalColour[2]);
    }
}
