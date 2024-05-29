with open("day1.txt") as fin:
    lines = fin.readlines()

def get_calibration(line):
    digits = [int(d) for d in list(line) if d.isdigit()]
    if len(digits) == 1:
        return digits[0] * 10 + digits[0]
    return digits[0] * 10 + digits[-1]


calibration_total = sum([get_calibration(line) for line in lines if line])
print(calibration_total)
