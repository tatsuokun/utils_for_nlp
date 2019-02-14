import nltk
import sys

def para2sent(input_filename, output_filename, lowercase=True):
    sent_detector = nltk.RegexpTokenizer(u'[^　！？。]*[！？。.\n]')
    with open(input_filename, 'r') as f, open(output_filename, 'w') as w:
        for line in f:
            for sent in sent_detector.tokenize(line):
                sent = sent.replace('\n', '').strip().lower()
                if sent:
                    w.write(sent+'\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('python this-file input-filename output-filename')
        quit()
    print(sys.argv)
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    para2sent(inputfile, outputfile)
