import in_place
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', type=str, help="files to process.")
    parser.add_argument("-b", "--backup", default='.bak', help="backup file extension.")
    parser.add_argument("-t", "--threshold", type=int, default=55, help="maximum characters per line.")
    args = parser.parse_args()
    bak = args.backup
    threshold = args.threshold

    files = args.files

    for f in files:
        print(f)
        wrap_captions(f, bak, threshold)


def wrap_captions(filename, bak, threshold):

    #with open(filename, 'r') as f:
    with in_place.InPlace(filename, backup_ext=bak) as f:        
        content = f.readlines()
        for line in content:
            line = line.strip()
            line_length = len(line)
            front = []
            back = []
            count = 0
            if line_length > threshold:
                for item in line.split():
                    count += len(item)
                    if count < (line_length * 1/2):
                        front.append(item)
                    else:
                        back.append(item)
                    count += 1
                #print("{}\n{}".format(" ".join(front), " ".join(back)))
                output = "{}\n{}".format(" ".join(front), " ".join(back))
                
            else:
                output = line
            f.write("{}\n".format(output))


def test(filename, bak='.bak'):
    with in_place.InPlace(filename, backup_ext=bak) as f:
        for line in f:
            f.write("{}\n{}".format(line,line))


if __name__ == '__main__':
    main()