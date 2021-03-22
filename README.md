# dotsies-visualiser
Little function to display the conlang dotsies in the python console
https://dotsies.org/

### `string_to_array(string, char_tup = ('░░', '██'))`

Will take the input string and return a printable version of the dotsies version
*(can only accept alphabetic characters)*
\n
`string_to_array('hello world')` will return
```
░░░░░░░░██░░██████░░░░\n░░░░░░░░░░░░██░░░░░░░░\n██░░████░░░░░░░░████░░\n██░░░░░░░░░░░░░░██░░██\n░░████████░░████░░██░░\n
```

which can be printed to show
```
░░░░░░░░██░░██████░░░░
░░░░░░░░░░░░██░░░░░░░░
██░░████░░░░░░░░████░░
██░░░░░░░░░░░░░░██░░██
░░████████░░████░░██░░
```
(This may not appear correctly on GitHub, but will be monospaced in python)
