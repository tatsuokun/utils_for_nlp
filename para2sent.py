import sys
import gzip
from nltk.tokenize import word_tokenize, sent_tokenize


def para2sent(input_filename, output_filename, is_gzip, lowercase=True):
    def write_paragraph_lines(paragraph_lines, file_obj):
        paragraph_str = ' '.join(paragraph_lines)
        for sent in sent_tokenize(paragraph_str):
            if lowercase:
                sent = sent.lower()
            file_obj.write(' '.join(word_tokenize(sent))+'\n')

    def writer(input_file):
        paragraph_lines = []
        for i, line in enumerate(input_file):
            if len(line.strip()) == 0 and len(paragraph_lines) > 0:
                write_paragraph_lines(paragraph_lines, output_file)
                paragraph_lines = []
            else:
                paragraph_lines.append(line)
        if len(paragraph_lines) > 0:
            write_paragraph_lines(paragraph_lines, output_file)
        print('Read {} lines'.format(i))

    print('Read files from', input_filename)
    print('Output file to', output_filename)
    with open(output_filename, mode='w') as output_file:
        if is_gzip:
            with gzip.open(input_filename, mode='rt', errors='ignore') as input_file:
                writer(input_file)
        else:
            with open(input_filename, mode='r', errors='ignore') as input_file:
                writer(input_file)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('Usage:: python para2sent inputfile outputfile')
        quit()
    input_file = args[1]
    output_file = args[2]
    is_gzip = True if input_file.endswith('.gz') else False
    para2sent(input_file, output_file, is_gzip=is_gzip)
