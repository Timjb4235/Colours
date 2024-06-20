public class Colour {
    
    private int red;
    private int blue;
    private int green;


    public Color(int r, int g, int b) {
        // Initialises a colour instance, ensuring values are between 0 and 255
        red = Math.max(Math.min(r, 255), 0);
        green = Math.max(Math.min(g, 255), 0);
        blue = Math.max(Math.min(b, 255), 0);
    }

    public int getRed() {
        return red;
    }

    public int getGreen() {
        return green;
    }

    public int getBlue() {
        return blue;
    }

    public String toHexString() {
        // Returns the six character hexstring of a colour
        return String.format("%02X", red) + String.format("%02X", green) + String.format("%02X", blue);
    }

    public Colour lerp(Color other, float f) {
        // Returns a colour somewhere between two colour instances.
        // If f is near zero then the output will be closer to 'self'
        // If f is near 1, the output will be closer to 'other'
        int redChange = other.getRed() - red;
        int greenChange = other.getGreen() - green;
        int blueChange = other.getBlue() - blue;
        return new Colour(Math.round(red + f * redChange), Math.round(green + f * greenChange), Math.round(blue + f * blueChange));
    }

    public Colour lerp(Color other, double d) {
        // Returns a colour somewhere between two colour instances.
        // If d is near zero then the output will be closer to 'self'
        // If d is near 1, the output will be closer to 'other'
        int redChange = other.getRed() - red;
        int greenChange = other.getGreen() - green;
        int blueChange = other.getBlue() - blue;
        return new Colour((int) Math.round(red + d * redChange), (int) Math.round(green + d * greenChange), (int) Math.round(blue + d * blueChange));
    }

    /*
    public static void main(String[] args) {
        Color red = new Color(255, 0, 0);
        System.out.println(red.toHexString());
        Color blue = new Color(0, 0, 255);
        System.out.println(blue.toHexString());
        Color purple = red.lerp(blue, 0.5f);
        System.out.println(purple.toHexString());
        Color purple2 = red.lerp(blue, 0.5);
        System.out.println(purple2.toHexString());
    }
    */
}
