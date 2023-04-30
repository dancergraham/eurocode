## Eurocode
Structural wind loading according to Eurocode EN1991-1-4.

Initial proof of concept of an OOP approach using Python.  Adapted from a [longer functional module](https://github.com/dancergraham/eurocode_EN1991_1_4). Initial commit includes a 'Site' class allowing calculation of the dynamic wind pressure at a given height.

By **Graham Knapp**

Please get in touch if you are interested in developing this together with me.

### Monkey Patched Variant
In the `ec1_monkey` subfolder is an experiment using monkey patching to implement the national annexes.  
I am not very happy with the current implementation because it is not very explicit : 
you cannot tell from the source code that an object has been monkey patched.  Maybe a decorator would be a better solution...
