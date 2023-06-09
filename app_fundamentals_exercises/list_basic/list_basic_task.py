def invert_values():
    return "Invert Values:\n You need add a numbers that is" \
           "positive and negative numbers separated by a single space. " \
           "Your result is a list containing the opposite of each number. " \
           "\n\nExample:\nInput: 1 2 -3 -3 5\nOutput: [-1, -2, 3, 3, -5] "


def multiples_list():
    return "Multiples List:\nYou need add two numbers (factor and count). It should get a list " \
           "with a length of the given count that contains only numbers, which are multiples of the given " \
           "factor. The numbers should be only positive, and they should be arranged in ascending order, starting" \
           " from the value of the factor.\n\nExample:\nInput:\n2\n5\nOutput:\n[2, 4, 6, 8, 10]"


def football_cards():
    return """Football Cards:\nMost football fans love it for the goals and excitement. Well, this problem does not. You are up to 
    handle the referee's little notebook and count the players who were sent off for fouls and misbehavior. The rules:
     Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. Any player
      may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining, the
       referee stops the game immediately, and the team with less than 7 players loses. The card is a string with the 
       team's letter ("A" or "B") followed by a single dash and the player's number. e.g., the card "B-7" means player
        #7 from team B received a card\n\nExample:\nInput:\nA-1 A-5 A-10 B-2\nOutput:\nTeam A - 8; Team B - 10 """


def number_beggars():
    return "Number Beggars:\nYou need add 2 both lines. On the first line, you need add numbers, " \
           "separated by a comma and a space ", ". On the second line, you add a count of beggars. Your result" \
                                                " is a list with the sum of what each beggar brings home, assuming " \
                                                "they all take regular turns, from" \
                                                " the first to the last number in the list.\n\nExample:\nInput:" \
                                                "\n3, 4, 5, 1, 29, 4\n6" \
                                                "\nOutput:\n[3, 4, 5, 1, 29, 4]"


def seize_the_fire():
    return """A program that calculates the water needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water. 
First, you will be given the level of fire inside the cell with  value of the cell, which represents the needed water to put out the fire.  They will be given in the following format: 

                                        typeOfFire= valueOfCell#typeOfFirE = valueOfCell# … typeOfFirE = valueOfCell

Afterward you will receive the amount of water you have for putting out the fires. There is a range of fire for each fire type, and if a cell's value is below or exceeds it, it is invalid, and you do not need to put it out. 
                                                                Type of Fire 	                                    Range 
                                                                    
                                                                High 	                                            81 - 125 
                                                                Medium              	                            51 - 80 
                                                                Low 	                                            1 - 50 

                                                                                            Example:
                               Input 	                                                                                                                        Output: 
High = 89#Low = 28#Medium = 77#Low = 23                                                                                   Cells:                                          
1250                                                                                                                                                        -	89  
                                                                                                                                                                 -	28 
                                                                                                                                                                 -	77 
                                                                                                                                                                 -	23 
                                                                                                                                                                 Effort: 54.25 
                                                                                                                                                                 Total Fire: 217 
"""