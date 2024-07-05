import re

print("A POP DEMAND TWEAK")
pop_need_multiplier = 2
# pop_need_multiplier = input("hello, please add multiplier: ")

new_lines = []
with open("A_00_buy_packages.backup_txt", 'r') as file_pop_needs:
     Lines = file_pop_needs.readlines()
     
     for line in Lines:
        if  "popneed_basic_food" in line and line != "":
            test = re.findall("\\d+",line)
            number = test.pop()
            number = int(number) * pop_need_multiplier
            line = re.sub("\\d+", str(number), line)
        if  "popneed_luxury_food" in line and line != "":
            test = re.findall("\\d+",line)
            number = test.pop()
            number = int(number) * pop_need_multiplier
            line = re.sub("\\d+", str(number), line)
        new_lines.append(line)
f= open("00_price_employ_buy_packages.txt","w+")
f.writelines(new_lines)

