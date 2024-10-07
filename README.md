# HanoiFileModifier

This transfers each last line from a file to a temporary file like the moves from a Hanoi Tower.

The purpose is to save disk space when modifying the lines from a large file which may take up too much space when making a new copy. 

Since the truncate() function only removes the bytes from the farthest file pointer position(last byte of a file), if you do readline() from the beginning and copy it to a file, doing truncate() on the original file will remove the last bytes, causing the data to be destroyed.

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
it seeks the final line from sfile, appends it to the empty 2nd file(tempfile), and truncates the line from itself(sfile)
```
 sfile:  |  tempfile:

  a      |   eeeee
  bb     |   dddd
         |   ccc
```
the lines can be modified before the transfer happens
```
sfile:   |  tempfile:

         |   eeeee
         |   dddd
         |   ccc
         |   bb
         |   a
```

then the same thing happens but in reverse. Tempfile truncate its final lines one by one as it copies the last lines from itself to sfile.
```
sfile:   |  tempfile:

 a       |
 bb      |
 ccc     |
 dddd    |
 eeeee   |
```
Make sure to make copy of your file before testing this. This was done on android phone, it might be os-specific


