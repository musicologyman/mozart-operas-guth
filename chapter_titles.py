from argparse import ArgumentParser
import csv
import os
import sys

LDQUO = u'\u201C'
RDQUO = u'\u201D'


def make_chapter_title(row):
    title = ""
    if row[0]:
        title += row[0] + ": "
    title += LDQUO + row[1] + RDQUO
    if row[2]:
        title += " (" + row[2] + ")"
    return title
    

def check_file(filename):
    return os.path.exists(filename)


def read_csv_file(filename):
    with open(filename, newline='') as fp:
        return list(csv.reader(fp))


def write_csv_file(filename, rows):
    with open(filename, newline='', mode='w') as fp:
        writer = csv.writer(fp)
        for i, title in enumerate(rows):
            writer.writerow([i+1, title])
            

def make_chapter_titles(rows):
    for row in rows:
        yield make_chapter_title(row)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist.")

    rows = read_csv_file(input_file)
    chapter_titles = list(make_chapter_titles(rows))
    print(chapter_titles)
    write_csv_file(output_file, chapter_titles)

