#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET

PATENTS = 'patent.data'


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    <?xml version="1.0" encoding="UTF-8"?>
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    with open(filename) as xml:
        whole_doc = xml.read()
    # print(len(whole_doc.split('<?xml version="1.0" encoding="UTF-8"?>')))
    splitted_files = whole_doc.split('<?xml version="1.0" encoding="UTF-8"?>')
    for i, file in enumerate(splitted_files):
        if i != 0:
            file_name = "{}-{}".format(filename, i-1)
            with open(file_name, 'w') as write_file:
                first_doc = '<?xml version="1.0" encoding="UTF-8"?>' + file
                write_file.write(first_doc)


def test():
    split_file(PATENTS)
    for n in range(4):
        print(n)
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print("You have not split the file {} in the correct boundary!".format(fname))
            f.close()
        except:
            print("Could not find file {}. Check if the filename is correct!".format(fname))


test()
