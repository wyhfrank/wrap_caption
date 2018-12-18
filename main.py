import in_place
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', type=str, help="files to process.")
    parser.add_argument("-b", "--backup", default='.bak', help="backup file extension.")
    parser.add_argument("-t", "--threshold", type=int, default=55, help="maximum characters per line.")
    parser.add_argument("-p", "--preview", action="store_true", help="preview result without modifying the file.")

    args = parser.parse_args()
    bak = args.backup
    threshold = args.threshold
    preview = args.preview
    files = args.files

    for f in files:
        print('-'*10)
        print(f)
        print('-'*10)
        wrap_captions(f, bak, threshold, preview)
    

def wrap_captions(filename, bak, threshold, preview):
    if preview:
        with open(filename, 'r') as f:
            for line in f:
                output = process_line(line, threshold)
                print(output)
    else:
        with in_place.InPlace(filename, backup_ext=bak) as f:        
            for line in f:
                output = process_line(line, threshold)
                f.write("{}\n".format(output))


def process_line(line, threshold):
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
        output = "{}\n{}".format(" ".join(front), " ".join(back))
    else:
        output = line
    return output


def test(filename, bak='.bak'):
    with in_place.InPlace(filename, backup_ext=bak) as f:
        for line in f:
            f.write("{}\n{}".format(line,line))


if __name__ == '__main__':
    main()