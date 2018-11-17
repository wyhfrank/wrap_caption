def test(filename='sample.srt'):
    cut_bond = 50
    with open(filename, 'r') as f:
        content = f.readlines()
        for line in content:
            line = line.strip()
            bucket = len(line)
            front = []
            back = []
            count = 0
            if bucket > cut_bond:
                for item in line.split():
                    count += len(item)
                    if count < (bucket * 1/2):
                        front.append(item)
                    else:
                        back.append(item)
                    count += 1
                print("{}\n{}".format(" ".join(front), " ".join(back)))
            else:
                print(line)

if __name__ == '__main__':
    test()