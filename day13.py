from aocd import data

def get_scan_loc(scanner, step):
    range = ranges.get(scanner, None)
    if range is None:
        return -1
    halfperiod = range-1
    if step%(2*halfperiod)>halfperiod:
        return halfperiod-(step%halfperiod)
    elif step%(2*halfperiod)==halfperiod:
        return halfperiod
    else:
        return step%halfperiod



def test_severity(simulation_step, packet_loc):
    if get_scan_loc(packet_loc, simulation_step)==0:
        severity=ranges[packet_loc]*packet_loc
    else:
        severity=0
    return severity


ranges = {int(key):int(value) for key, value in (x.replace(" ", "").split(":") for x in data.splitlines())}

def simulate(delay):
    severities = []
    for packet_loc,simulation_step in enumerate(range(delay, max(ranges.keys())+1+delay)):
        severities.append(test_severity(simulation_step, packet_loc))
    return sum(severities)

counter=-1
while True:
    counter+=1
    if simulate(counter)==0:
        break
print(counter)












