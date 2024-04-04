import glob

def get_parser():
    
    all_files = [x for x in glob.glob("./*") if ".py" in x]
    print(all_files)


if __name__ == "__main__":
    get_parser()