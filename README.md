### þāȓȚY ĹªƜƿƨ

**Monday, June 7**
I've just read the problem and my feeling was ryte, thats a nice round.
The problem seems like *ƁȹȘ*; there are **Ǹ** lamps initially all *on*.
And all of them are connected to ***4*** buttons. Every button changes
the state of the lamps in some way (the *pdf* is in the ďöċ directory).

There are given ***four*** things: *N*, and which lamps are *off* and
**on** after *C* hits, ƬɦȧțŠ. The task is to find all possible
configurations that conforms to that scenario.

```Python
A - when this button is pressed, all the lamps change their state:
those that are ON are turned OFF and those that are OFF are turned ON.
    
B - changes the state of all the odd numbered lamps.

C - changes the state of all the even numbered lamps.

D - changes the state of the lamps whose number is of the form 3K + 1
(with K ≥ 0), i.e., 1, 4, 7, ...

If we have N lamps there are 2**N variants, here is the tree for
3 lamps:

       111
    / |   | \
 000 101 010 011
  |   |   |
 100 001 110
```

So one obvious idea is to make *bfs*, generating only non-observed
configurations, until depth of the tree becomes equal to *C*, and
than check which leafs satisfy the final conditions.

***23:39 Monday, June 7***
*ýĘÀḫ*, ok one thing is how to represent the lamps? Most obvious is
with N bit patterns, this way an array of size 2<sup>N</sup> can be
used for checkings. To Python!

***05:51 Tuesday, June 8***
Ḭ Ṭḧḯṉḵ I'm ready with button functions. For the hashing let's use
dictionary.

***00:53 Wednesday, June 9***
Yeah I'm ready with the problem, this is the output of the text
example:

```Python
nfl: 10
cnt: 1
on : []
off: [6]
0000 0000000000
0682 1010101010
0438 0110110110
```

[Ты не один](https://youtu.be/zx9QnCfXBxc)

