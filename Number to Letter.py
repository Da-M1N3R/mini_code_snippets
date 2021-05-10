''' abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    48  3   1     0   57     2'''

def change(all):
    all = all.upper()
    all = all.replace("A", "4")
    all = all.replace("B", "8")
    all = all.replace("E", "3")
    all = all.replace("I", "1")
    all = all.replace("O", "0")
    all = all.replace("S", "5")
    all = all.replace("T", "7")
    all = all.replace("Z", "2")
    return all

print(change("Intelligence is the ability to adapt to surroundings"))

