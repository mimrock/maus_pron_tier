import argparse
import os.path
import sys

## Creates the Canonical Pronunciation Tier for MAUS
#
#  @param Continuous text in SAMPA notation. The words should be separated with spaces or linebreaks, but not
#    with punctuations.
#  @return Canonical Pronunciation Tier for MAUS.
#  @see http://http://www.bas.uni-muenchen.de/Bas/BasFormatseng.html#KAN
def canonical_p(text):
    words = text.split()
    tier = ''
    last_row = len(words) - 1

    for i, word in enumerate(words):
        if word:
            tier += 'KAN: ' + str(i) + '  ' + word
        if last_row > i:
            tier += '\r\n'

    return tier


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create Canonical Pronunciation Tier for MAUS. '
                                                 'Check the documentation at: '
                                                 'http://http://www.bas.uni-muenchen.de/Bas/BasFormatseng.html#KAN')
    parser.add_argument('-input', type=str, help='Text file to open', required=True)
    parser.add_argument('-out', type=str, help='Pronunciation Tier will be generated in this file.', required=True)
    args = parser.parse_args()

    if os.path.isfile(args.out):
        print("Output file already exists!")
        sys.exit()

    try:
        with open(args.input, "r") as infile:
            text = infile.read()
    except IOError:
        print("Error: Could not read input file.")
        sys.exit()

    tier = canonical_p(text)
    print(tier)

    try:
        with open(args.out, "w") as outfile:
            outfile.write(tier)
    except IOError:
        print("Error: Could not create file. Check the path and permissions.")
        sys.exit()
