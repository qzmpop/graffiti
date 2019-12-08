import argparse

parser = argparse.ArgumentParser()

parser.add_argument("start_date", help="starting point to lookup")
parser.add_argument("final_date", help="ending point to lookup")
parser.add_argument("-e", "--enable", action="store_true",
                    help="enable option which read txt and lookup elements in txt")
parser.add_argument("-r", "--range", type=int, choices=[0, 1, 2],
                    help ="attribute select")


args = parser.parse_args()

print(args.start_date)
print(args.final_date)
print(args.enable)
print(args.range)
    
