''' Plugin for CudaText editor
Authors:
    heXor    (heXor on bitbucket)
Version:
    '1.0.0 2016-11-01'

ToDo:
1. operation on only selected lines (need check select diap. if no selection - then work on all file).
2. func: split by char and aligment spaces
3. add to menu "edit"
4. localization
5. func: trim spaces
6. add "interface lock" if text too big (lock/unlock function)

'''
#! /usr/bin/env python3

# import os, json, re, collections, itertools
#import  cudatext            as app
from    cudatext        import ed
from    itertools       import groupby

# WIP:
#import  cudax_lib           as apx
# I18N
#_       = get_translation(__file__)

class Command:
    def lineops_remove_empty(self):
        ed.set_text_all( "\n".join(list(filter(None, ed.get_text_all().split("\n")))) )

    def lineops_sort_asc(self):
        ed.set_text_all("\n".join( sorted(ed.get_text_all().split("\n")) ))

    def lineops_sort_desc(self):
        ed.set_text_all("\n".join( sorted(ed.get_text_all().split("\n"), reverse=True) ))

    def lineops_remove_dup_all(self):
        ed.set_text_all("\n".join( list(set(ed.get_text_all().split("\n"))) ))

    def lineops_remove_dup(self):
        ed.set_text_all("\n".join( list([i[0] for i in groupby()]) ))

    def lineops_trim_all(self):
        ed.set_text_all("\n".join( map(lambda x: x.strip(), ed.get_text_all().split("\n")) ))

    def lineops_trim_left(self):
        ed.set_text_all("\n".join( map(lambda x: x.lstrip(), ed.get_text_all().split("\n")) ))

    def lineops_trim_right(self):
        ed.set_text_all("\n".join( map(lambda x: x.rstrip(), ed.get_text_all().split("\n")) ))


