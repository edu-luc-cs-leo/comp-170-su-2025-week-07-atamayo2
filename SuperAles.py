###These are all classes from original file

class Ale:
    def __init__(self, name: str, abv: float):
        self.name = name  # Name of the ale "IPA"
        self.abv = abv #Alcohol in decimal form 

    def alcohol_content(self, volume_in_oz: float) -> float:
        return self.abv * volume_in_oz #Calculation of amount of pure alcohol in volumes 

    def description(self) -> str:
        return f"{self.name}: {self.abv * 100:.1f}% ABV" #Return string that describes the ale with ABV %

## THis bottom section are the same alcohol but doing the super float they
# are all subclasses inheritis from the Ale but made own name and ABV
class PaleAle(Ale): #
    def __init__(self):
        super().__init__("Pale Ale", 0.055)
class IPA(Ale):
    def __init__(self):
        super().__init__("IPA", 0.065)
class Stout(Ale):
    def __init__(self):
        super().__init__("Stout", 0.07)
class Porter(Ale):
    def __init__(self):
        super().__init__("Porter", 0.06)




#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#

if __name__ == "__main__":
    pale_ale = PaleAle()
    print(pale_ale.description())                  # Prints: 5.5% ABV
    print(pale_ale.alcohol_content(12))            # Prints: 0.66 (12 oz × 0.055)
    
    ipa = IPA()
    print(ipa.description())                        # Prints: 6.5% ABV
    print(ipa.alcohol_content(12))                  # Prints: 0.78

