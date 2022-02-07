import sys
import datetime
import artifact

def main():
    begin = datetime.datetime.now()
    test_artifact = artifact.Artifact()
    print(datetime.datetime.now() - begin)


if __name__ == "__main__":
    sys.exit(main())
