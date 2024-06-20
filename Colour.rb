class Colour
    # Define getters and setters:
    attr_accessor :red, :green, :blue
    
    def initialize(red, green, blue)
      @red = red
      @green = green
      @blue = blue
    end
    
    def to_hex_string
      hex_red = @red.round.to_s(16).upcase
      hex_green = @green.round.to_s(16).upcase
      hex_blue = @blue.round.to_s(16).upcase
      hex_red.rjust(2, '0') + hex_green.rjust(2, '0') + hex_blue.rjust(2, '0')
    end
    
    def lerp(second_colour, float)
        # A float of zero should return the starting colour (self), while a float of 1 should return the second colour (hex_string).
        # Declaring the change vector from the starting colour to the second colour:
        colour_vector = [second_colour.red - @red, second_colour.green - @green, second_colour.blue - @blue]
        # Calculate final colour:
        final_red = @red + float * colour_vector[0]
        final_green = @green + float * colour_vector[1]
        final_blue = @green + float * colour_vector[2]
        Colour.new(final_red, final_green, final_blue)
    end
  end
