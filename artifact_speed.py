import sys
import datetime
import artifact

def main():
    begin = datetime.datetime.now()
    print(artifact.Artifact())
    print(datetime.datetime.now() - begin)


if __name__ == "__main__":
    sys.exit(main())
