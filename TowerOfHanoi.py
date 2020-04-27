def tower_of_Hanoi(num_disks):
    return towerrecur(num_disks,'S','A', 'D')

def towerrecur(num_disks, source, auxiliary, destination):
    if num_disks > 0:
        towerrecur(num_disks-1,source,destination,auxiliary)
        print(source, destination)
        towerrecur(num_disks-1,auxiliary,source,destination)
    else:
        return

print(tower_of_Hanoi(4))