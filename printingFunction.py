def printModels(designs, completed):
    while designs:
        currentDesign = designs.pop()
        completed.append(currentDesign)
        print(f"Printing Design: {currentDesign}")


def showCompleted(completed):
    print("Following are the completed designs:")
    for design in completed:
        print(design)