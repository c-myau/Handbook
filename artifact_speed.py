import artifact
import sys
import datetime

def main():
    begin = datetime.datetime.now()
    a = artifact.Artifact()
    txt = "{type} {main} {stat}\n".format(type = a.get_type(), main = a.get_mainstat(), stat = a.get_substats())
    print(txt)
    print(datetime.datetime.now() - begin)


if __name__ == "__main__":
    sys.exit(main())