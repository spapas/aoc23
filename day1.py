with open("day1.txt") as fin:
    lines = fin.readlines()


def get_calibration(line):
    print(line)
    line = (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    print(line)
    digits = [int(d) for d in list(line) if d.isdigit()]
    if len(digits) == 1:
        return digits[0] * 10 + digits[0]
    return digits[0] * 10 + digits[-1]


calibration_total = sum([get_calibration(line) for line in lines if line])
print(calibration_total)
