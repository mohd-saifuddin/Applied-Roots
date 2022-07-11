# Time slots to practice Take Charge of Time course exercises.

def write_time_slots(start=0, end=24):
    """
    This function writes the time slots in txt file.
    """
    slots = list()
    for t in range(start, end-1):
        slots.append('{:02d}:00 - {:02d}:00\n'.format(t, t+1))
    slots.append('{:02d}:00 - {:02d}:00'.format(t+1, 0))

    with open(file='time_slots.txt', mode='w') as ts_file:
            ts_file.writelines(slots)
    print('Time slots are published!')

write_time_slots()
