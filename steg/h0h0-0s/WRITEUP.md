# H0H0-0S Writeup

> Author: alexandre-lavoie

The `gr1nch.txt` gives us a hint:

```
Ftp Open - Lves Don't Even Remember Security
```

Which we can use the first letter of each word to get:

```
FOLDERS
```

Therefore we should focus on folders. If we navigate through the folders, we notice numbered folders. It seems to be some kind of encoding, but maybe not clear. I would expect a few going for the hint: `Esolang`. With previous hint, we can look up `Folders Esolang`. This will link us to this esolang entry: https://esolangs.org/wiki/Folders.

There is a clean Python interpreter that can be installed with:

```
pip3 install Folders
```

And can be run on the root folder:

```
Folder ./H0H0-0S
```

To give the output:

```
The flag is: `FLAG-{y0u_s4v3d_th3_313v35}`
```
