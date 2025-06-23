import argparse
def main():
    parser=argparse.ArgumentParser()
    parse=parser.add_mutually_exclusive_group(required=True)
    parse.add_argument("--c",type=float,help="Temperature in celsius")
    parse.add_argument("--f",type=float,help="Temperature in fahrenheit")
    arg=parser.parse_args()
    if arg.c is not None:
        fahrenheit=convert1(arg.c)
        print(f"{arg.c} in celsius converted into {fahrenheit} fahrenheit")
    else:
        celsius=convert2(arg.f)
        print(f"{arg.f} in fahrenheit converted into {celsius} celsius")
def convert1(c):
    return (c * 9/5)+32
def convert2(f):
    return (f-32)*5/9
main()
