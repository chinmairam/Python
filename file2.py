import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
        # print(line) # Gives Space between Lines
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])

# import file2
# print(main('wasteland.txt'))
