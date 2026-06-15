import time
import re


def main():
    passports = [{field.split(":")[0]: field.split(":")[1] for field in re.split(r"[\s\n]+", passport)} for passport in open("Inputs/input04.txt").read()[:-1].split("\n\n")]
    t = time.time()

    total1, total2 = solve(passports)

    print(total1)
    print(total2)
    print(time.time()-t)


def solve(passports: list) -> int:
    colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    total1 = 0
    total2 = 0
    for passport in passports:
        amount = len(passport)
        if amount == 8 or (amount == 7 and "cid" not in passport):
            total1 += 1
            if 1920 <= int(passport["byr"]) <= 2002 and 2010 <= int(passport["iyr"]) <= 2020 and 2020 <= int(passport["eyr"]) <= 2030 and passport["ecl"] in colours and\
            ((passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193) or (passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76)) and\
            (passport["pid"].isnumeric() and len(passport["pid"]) == 9) and (passport["hcl"][0] == "#" and len(passport["hcl"]) == 7 and\
            (re.sub("[abcdef]", "", passport["hcl"][1:]).isnumeric() or re.sub("[abcdef]", "", passport["hcl"][1:]) == "")):
                total2 += 1

    return total1, total2


if __name__ == "__main__":
    main()
