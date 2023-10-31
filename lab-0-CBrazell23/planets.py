# float string -> float
# Given earth weight and planet, returns weight on provided planet
def weight_on_planets(pounds, planet):
   if(planet == "Mars"):
      return 0.38 * pounds
   elif(planet == "Jupiter"):
      return 2.34 * pounds
   elif(planet == "Venus"):
      return 0.91 * pounds
   else:
      raise ValueError


if __name__ == '__main__':
   pounds = float(input("What do you weigh on earth? "))
   print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.")
