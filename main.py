from tools import jmlmtools
from models import models


def main():
    jmlmtools.clear()
    print("")
    args = jmlmtools.parse_arguments()
    if args.db == "create":
        models.fill_database()
    elif args.db == "test":
        models.test_database()



if __name__ == "__main__":
    main()