#!/usr/bin/env python

import sys

def collapse_brackets(s):
    count = 0
    r = ""
    for c in s:
        if c == '<':
            if count == 0:
                r += "<…"
            count += 1
        else:
            count -= (c == '>')
            if count == 0:
                r += c
    return r

def simplify(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        for l in f:
            stack, count = l.rsplit(" ", 1)
            stack = stack.split(";")
            count = count.strip()
            stack_c = map(collapse_brackets, stack)
            print((";".join(stack_c)) + " " + count)
    return

DEBUG = True and False

if __name__ == "__main__":
    if DEBUG:
        t = "CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr::CRrrrr<> > > > > > > > > > > >::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr>::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr::CRrrrr<> > > > > > > > > > >, CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr::CRrrrr<CRrrrr, CRrrrr> > > >> > > > > >::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr CRrrrr>, CRrrrr::CRrrrr, CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr> > >, CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr>::CRrrrr, CRrrrr::CRrrrr<CRrrrr, CRrrrr> > >(CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr> >, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr, CRrrrr::CRrrrr> > CRrrrr&, CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr CRrrrr>, CRrrrr::CRrrrr, CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr::CRrrrr> > >, CRrrrr::CRrrrr<CRrrrr::CRrrrr::CRrrrr, CRrrrr::CRrrrr>::CRrrrr, CRrrrr::CRrrrr<CRrrrr, CRrrrr> > CRrrrr&)"
        print(collapse_brackets(t))
        exit(0)
    if len(sys.argv) != 2:
        exit(1)
    simplify(sys.argv[1])
