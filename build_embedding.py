from gensim.models import word2vec
import logging
import argparse


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--window', '-w', default=5, type=int)
    parser.add_argument('--epoch', '-e', default=5, type=int)
    parser.add_argument('--min_count', '-m', default=0, type=int,
                        help='train or not')
    parser.add_argument('--input-file', '-i',  type=str,
                        help='specify input file')
    parser.add_argument('--output-file', '-o', type=str,
                        help='specify input file')
    parser.add_argument('--negative', '-n', default=10, type=int,
                        help='specify config toml file')
    parser.add_argument('--dim', '-d', default=300, type=int)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    PATH = args.input_file
    sentences = word2vec.LineSentence(PATH)
    print("learning")
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',  level=logging.INFO)
    model = word2vec.Word2Vec(sentences,
                              size=args.dim,
                              sg=1,
                              min_count=args.min_count,
                              negative=args.negative,
                              iter=args.epoch,
                              window=args.window,
                              workers=6)
    model.save(args.output_file)
