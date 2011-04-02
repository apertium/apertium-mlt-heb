#!/bin/sh
lt-comp lr apertium-mt-he.mt-he.dix mt-he.automorf.bin
lt-comp lr apertium-mt-he.mt.dix mt-he.automorf.bin
lt-comp rl apertium-mt-he.he.dix mt-he.autogen.bin
lt-comp lr apertium-mt-he.he.dix he-mt.automorf.bin
lt-comp rl apertium-mt-he.mt.dix he-mt.autogen.bin
lt-comp lr apertium-mt-he.mt-he.dix mt-he.autobil.bin
lt-comp rl apertium-mt-he.mt-he.dix he-mt.aotobil.bin
apertium-preprocess-transfer apertium-mt-he.mt-he.t1x mt-he.t1x.bin

