#!python
from format_otr.export_otr import get_txt
import sys

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1][-4:] == '.otr':
        print(get_txt(sys.argv[1]))