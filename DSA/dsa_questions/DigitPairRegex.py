import re
import DSA
import logging

logger = logging.getLogger('__main__')

def digit_pair_pattern(inputStr):
    digit_pair_regext = r'(\d)(?=\d\1)'
    groups = re.findall(digit_pair_regext, inputStr)
    logger.info(f"groups {groups}")
    print(len(groups) < 2)

if __name__ == "__main__":
    digit_pair_pattern("1212")
    digit_pair_pattern("1213")