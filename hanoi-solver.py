
def hanoi_solver(disks: int, printType: str) -> str:
    left = list(range(disks, 0, -1))
    mid = []
    right = []
    history = []

    # makes the list of arrays more readable 
    arrayNames = {
        id(left): "left",
        id(mid): "mid",
        id(right): "right"
    }

    def addToReturn(disk_num: int, source: list, target: list) -> None:
        if printType == "array":
            history.append(f"{left} {mid} {right}")
        else:
            sourceName = arrayNames[id(source)]
            targetName = arrayNames[id(target)]
            history.append(f"Move disk {disk_num} from {sourceName} to {targetName}")

    def solve(n: int, source: list, target: list, auxiliary: list) -> None:
        if n == 0:
            return

        # move n-1 disks from source to auxiliary using target
        solve(n - 1, source, auxiliary, target)

        # move the current disk n from source to target
        target.append(source.pop())
        addToReturn(n, source, target)

        # move n-1 disks from auxiliary to target using source
        solve(n - 1, auxiliary, target, source)

    solve(disks, left, right, mid)
    return "\n".join(history)

def main() -> None:
    answer = input("Enter the number of disks: ")
    printType = input("Do you want to see the steps in array or text? (Type array or text): ").strip().lower()

    try:
        disks = int(answer)
        if disks < 1:
            print("Enter a positive integer")
            main()
            return
        if disks > 9:
            print("The amount of disks is too high. Please enter a number less than or equal to 9.\n")
            print("(Max limit is editable in the code but can cause issues with performance)")
            main()
            return
    except ValueError:
        print("Enter a positive integer")
        main()
        return

    if printType not in ["array", "text"]:
        print(f"Invalid input for the print type: {printType}. Defaulting to 'array'.")
        printType = "array"

    result = hanoi_solver(disks, printType)
    
    print(f"\nSolution for {disks} disks:\n")
    print("The lower the number, the shorter the disc. The higher the number, the longer the disc.\n")
    print(result)
    print(f"\nTotal moves: {2**disks - 1}")


if __name__ == "__main__":
    main()