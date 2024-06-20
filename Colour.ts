class Colour {
    red: number;
    green: number;
    blue: number;
    alpha: number;

    constructor(r: number, g: number, b: number, alpha: number = 1) {
        // Creates a colour instance defined by three integers
        this.red = r;
        this.green = g;
        this.blue = b;
        this.alpha = alpha;
    }

    toHexString(): string {
        // Converts a set of three byte values to a six character hexadecimal string.
        const hexRed: string =  this.red.toString(16);
        const hexGreen: string =  this.green.toString(16);
        const hexBlue: string =  this.blue.toString(16);
        return hexRed.padStart(2,"0") + hexGreen.padStart(2,"0") + hexBlue.padStart(2,"0");
    }

    lerp(secondColour: Colour, float: number): Colour {
        // A float of zero should return the starting colour (this), while a float of 1 should return the second colour (hex_string).
        // Declaring the change vector from the starting colour to the second colour:
        const colourVector: number[] = [secondColour.red - this.red, secondColour.green - this.green, secondColour.blue - this.blue];
        // Calculating the rbg vector of the final colour:
        const finalColour: number[] = [this.red + float * colourVector[0], this.green + float * colourVector[1], this.blue + float * colourVector[2]];
        return new Colour(finalColour[0], finalColour[1], finalColour[2]);
    }
}
