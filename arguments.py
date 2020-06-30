from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--path", help="The directory path of the files to be searched *** Default(./)", default="./")
parser.add_argument("--show_filter", help="Shows the filtered number of results in descending order of score *** Default(10)", default="10")

opt = parser.parse_args()