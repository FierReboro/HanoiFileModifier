# HanoiFileModifier
Copy and truncates lines from a file to another and back again.

The purpose is to save disk space when modifying the lines from a large file which may take up too much space when making a new copy.

The algorithm works like this:

the first file(sfile) may contain this:
```
sfile:
 a
 bb
 ccc
 dddd
 eeeee
```
it seeks the final lines from sfile, appends it to the empty 2nd file(tempfile), and truncates the line from itself(sfile)
```
 sfile:  |  tempfile:

  a      |   eeeee
  bb     |   dddd
         |   ccc
```
->>>>
```
sfile:   |  tempfile:
             eeeee
             dddd
             ccc
             bb
             a
```
the lines maybe modified while this is being done.

then the same thing happens but in reverse. Tempfile truncate its final lines one by one as it copies the lines from itself to sfile.

b'a\nbb\nccc\ndddd\neeeee\n'

Make sure to make copy of your file before testing this. This was done on android phone, it might be os-specific


