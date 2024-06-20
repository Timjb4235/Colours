#pragma once

class Colour
{
public:
	Colour(int r, int g, int b);
	int getRed() {
		return red;
	}
	int getGreen() {
		return green;
	}
	int getBlue() {
		return blue;
	}
	std::string getHexCode() const;
	Colour lerp(Colour &other, float f) const;

private:
	int red, green, blue;
};

