# Gr1nch's Code Writeup

> Author: alexandre-lavoie

We start by reverse engineer the circuit, which is relatively simple. We can look up both chips:

- `74HC80`: A quad NAND.
- `74HC08`: A quad AND.

If we follow the wiring, we see that the circuit comes down to:

```python
def circuit(bits):
    left = land(nand(bits[0], bits[1]), nand(bits[2], bits[4]))
    right = land(left, bits[3])
    return left, right
```

We can notice that the left one is always on when the right one is on. This seems to indicate 3 states: none, short, and long. Usually, this is Morse Code, but if we were unsure the hint tells us we are on the right track. We can convert LED states to dots and dashes and map them to ASCII. This was done in the `decode` method in `./challenge.py`. This gives the flag:

```
1T5-4LW4Y5-M0R53-C0D3
```
