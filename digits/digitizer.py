import csv
import os, sys

__author__ = 'haakon'


def parse_training_data(data):
    info = []
    for row in data:
        info.append(row)

    return info


def parse_test_data(data):
    pass


def main():

    train_data = []
    with open('train.csv') as csvfile:
        print "Opened file"
        fr = csv.reader(csvfile)
        for row in fr:
            train_data.append(row)

    #test = csv.reader('test.csv')

    #train_data = parse_training_data(train)
    #test_data = parse_test_data(test)

    print len(train_data)


if __name__ == "__main__":
    main()
