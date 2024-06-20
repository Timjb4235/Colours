#include "Colour.h"
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

Colour::Colour (int r, int g, int b) {
	red = std::max(std::min(r, 255), 0);
	green = std::max(std::min(g, 255), 0);
	blue = std::max(std::min(b, 255), 0);
	}

std::string Colour::getHexCode() const {
	std::stringstream stream;
	stream << std::setfill('0') << std::hex << std::setw(2) << red << std::setw(2) << green << std::setw(2) << blue;
	std::string result(stream.str());
	return result;
}
Colour Colour::lerp(Colour &other, float f) const {
	int redChange = other.getRed() - red;
	int greenChange = other.getGreen() - green;
	int blueChange = other.getBlue() - blue;
	return Colour(round(red + f * redChange), round(green + f * greenChange), round(blue + f * blueChange));
}



