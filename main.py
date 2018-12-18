import io
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', type=str, help="files to process.")
    parser.add_argument("-s", "--suffix", default='wrapped', help="suffix for res files.")
    parser.add_argument("-t", "--threshold", type=int, default=55, help="maximum characters per line.")
    parser.add_argument("-p", "--preview", action="store_true", help="preview result without modifying the file.")
    parser.add_argument("--encoding", default="utf-8", help="encoding of the files.")

    args = parser.parse_args()
    suffix = args.suffix
    threshold = args.threshold
    preview = args.preview
    files = args.files
    encoding = args.encoding

    for f in files:
        wrap_captions(f, suffix, threshold, preview, encoding)


def wrap_captions(filename, suffix, threshold, preview, encoding):
    results = []
    # https://stackoverflow.com/a/50872028/1938012
    with io.open(filename, 'r', encoding=encoding) as f:
        lines = f.readlines()
        for line in lines:
            res = process_line(line, threshold)
            results.append(res)
    new_contents = u"\n".join(results)
    if preview:
        print('-'*10)
        print(filename)
        print('-'*10)
        print(new_contents)
    else:
        new_filename = gen_filename(filename, suffix)
        print(u"{0} --> {1}".format(filename, new_filename))
        with io.open(new_filename, 'w', encoding=encoding) as fo:
            fo.write(new_contents)

def gen_filename(filename, suffix):
    return u"{0}.{2}{1}".format(*os.path.splitext(filename) + (suffix,))

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
        res = u"{0}\n{1}".format(u" ".join(front), u" ".join(back))
    else:
        res = line
    return res


if __name__ == '__main__':
    main()