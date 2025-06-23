import argparse
def main():
    parse=argparse.ArgumentParser()
    parse.add_argument("celsius",type=float,help="Temperature in celsius")
    arg=parse.parse_args()
    fahrenhiet=convert(arg.celsius)
    print(f"The Temperature is converted from {fahrenhiet} to {arg.celsius}")
def convert(c):
    return (c * 9/5)+32
main()
