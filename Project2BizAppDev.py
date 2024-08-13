import FileIO

def title():
    print("Baseball Team Management Program")
    
def displayMenu():
    print("\nMENU OPTIONS")
    print("1. Display lineup")
    print("2. Add player")
    print("3. Remove player")
    print("4. Move player")
    print("5. Edit player position")
    print("6. Edit player stats")
    print("7. Exit program")
    
    print("POSITIONS:", FileIO.VALID_POSITIONS)

def validatePosition():
    while True:
        position = input("Position: ").upper()
        if position not in FileIO.VALID_POSITIONS:
            print("Invalid position. Please enter a valid position.")
        else:
            return position

def validateNumber(message):
    while True:
        try:
            number = int(input(message))
            if number < 0:
                print("Invalid number. Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def displayLineup(lineup):
    if not lineup:
        return
    print("\nLINEUP:") 
    for battingOrder, player in enumerate(lineup):
        try:
            name, position, at_bats, hits = player
            at_bats = int(at_bats)
            hits = int(hits)
            average = round(hits / at_bats, 3) if at_bats > 0 else 0
            print(f"{battingOrder+1}. {name} ({position}) {at_bats}, {hits}, {average}")
        except ValueError:
            continue
        
def addPlayer(lineup):
    name = input("Name: ")
    position = validatePosition()
    at_bats = validateNumber("At bats: ")
    hits = validateNumber("Hits: ")
    while hits > at_bats:
        print("Invalid number of hits. The number of hits can't be greater than the number of at bats.")
        hits = validateNumber("Enter number of hits: ")
    player = [name, position, at_bats, hits, average]
    lineup.append(player)
    print(f"{name} was added.")
    FileIO.writePlayers(lineup)

def removePlayer(lineup):
    if not lineup:
        print("The lineup is currently empty.")
        return
    displayLineup(lineup)
    lineup_num = validateNumber("Enter a lineup number to remove: ")
    if not 1 <= lineup_num <= len(lineup):
        print("Invalid lineup number.")
        return
    name = lineup[lineup_num - 1][0]
    lineup.pop(lineup_num - 1)
    print(f"{name} was deleted.")
    FileIO.writePlayers(lineup)

def movePlayer(lineup):
    if not lineup:
        print("The lineup is currently empty.")
        return
    displayLineup(lineup)
    currentPosition = validateNumber("Enter a current lineup number to move: ")
    if not 1 <= currentPosition <= len(lineup):
        print("Invalid position.")
        return
    else: 
        for battingOrder, player in enumerate(lineup):
            name, position, at_bats, hits = player
            if battingOrder == currentPosition - 1:
                print(f"{name} was selected.")
    newPosition = validateNumber("Enter a new lineup number: ")
    if not 1 <= newPosition <= 9:
        print("Invalid position.")
        return
    player = lineup.pop(currentPosition - 1)
    lineup.insert(newPosition - 1, player)
    print(f"{name} was moved.")
    FileIO.writePlayers(lineup)
    
def editPlayerPosition(lineup):
    if not lineup:
        print("The lineup is currently empty.")
        return
    displayLineup(lineup)
    lineupPosition = validateNumber("Enter a lineup number to edit: ")
    if not 1 <= lineupPosition <= len(lineup):
        print("Invalid position.")
        return
    else:
        name, position, at_bats, hits = lineup[lineupPosition-1]
        print(f"You selected {name}: Position = {position}")
        newPosition = validatePosition()
        lineup[lineupPosition-1][1] = newPosition
        print(f"{name} was updated.")
        FileIO.writePlayers(lineup)
    
def editPlayerStats(lineup):
    lineupPosition = validateNumber("Enter player lineup position to edit stats: ")
    if lineupPosition < 1 or lineupPosition > len(lineup):
        print("Invalid lineup position.")
        return
    player = lineup[lineupPosition - 1]
    print("What do you want to edit?")
    print("1. At bats")
    print("2. Hits")
    choice = validateNumber("Enter 1 or 2: ")
    if choice == 1:
        at_bats = validateNumber("At bats: ")
        hits = validateNumber("Hits: ")
        while hits > at_bats:
            print("Invalid because hits is greater than at bats. Please try again.")
            hits = validateNumber("Enter number of hits: ")
        average = round(hits / at_bats, 3) if at_bats > 0 else 0
        player[2] = at_bats
        player[3] = hits
        player[4] = average
        print(f"{lineupPosition} was updated.")
        FileIO.write_players(lineup)
    elif choice == 2:
        hits = validateNumber("Hits: ")
        at_bats = player[2]
        while hits > at_bats:
            print("Invalid because hits is greater than at bats. Please try again.")
            hits = validateNumber("Hits: ")
        average = round(hits / at_bats, 3) if at_bats > 0 else 0
        player[3] = hits
        player[4] = average
        print(f"{lineupPosition} was updated.")
        FileIO.write_players(lineup)
    else:
        print("Invalid menu option. Please try again.")
        
def main():
    title()
    displayMenu()
    lineup = FileIO.readPlayers()
    if not lineup:
        print("The lineup is currently empty.")
    while True:
        choice = validateNumber("Menu option: ")
        if choice == 1:
            if not lineup:
                print("There is noone in the lineup.")
            else:
                displayLineup(lineup)
        elif choice == 2:
            addPlayer(lineup)
        elif choice == 3:
            removePlayer(lineup)
        elif choice == 4:
            movePlayer(lineup)
        elif choice == 5:
            editPlayerPosition(lineup)
        elif choice == 6:
            editPlayerStats(lineup)
        elif choice == 7:
            FileIO.writePlayers(lineup)
            print("Bye!")
            break
        else:
            print("Invalid menu option. Please try again.")
            displayMenu()
            
if __name__ == "__main__":
    main() 
    