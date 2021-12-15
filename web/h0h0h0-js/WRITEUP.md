# Writeup

The goal of the challenge is to showcase how JS regexes with the *global* flag can be abused to return different values when called without reinitializing the regex.

    const anti_injection_pattern = /'/g; // 1 quoty boi vs 1 hacker...

This line is declared once at the start of the `POST` handler, which means it can be used more than once per lifecycle. The regex can be easily tested in the console. As you can see, using the regex more than once makes it evaluate to true, then false, repeatedly. 

    ```js
    const anti_injection_pattern = /'/g;
    anti_injection_pattern.test("test'"); // -> true
    anti_injection_pattern.test("test'"); // -> false
    anti_injection_pattern.test("test'"); // -> true
    ```

An attacker noticing the global flag on a *blacklist* regex can look for ways to use it more than once per lifecycle in order to get different result. This could be more complicated if the regex had more than 1 caracter in the blacklist, but it would work in the same way.

In this challenge, there is only one other place where the regex is called. We have to set the `X-Mas-Debug` header to `is-name-on-list` in order to call the `isForbidden`. We need to feed it a string containing a single-quote in order to increment the `lastIndex` property of the regex, whic will make the regex evaluate to false in the next call. For more details, see the documentation on the [`lastIndex` property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex).

Once the `X-Mas-Debug` header is set to `is-name-on-list`, we can pass the value `'` to the param `nameOnList` to make the regex evaluate to True. Our next call to the Regex will return false, which means we can exploit our SQL injection with a basic payload, like `' or 1=1--`.

The final payload looks like this : `name=a'%20or%201=1--&nameOnList=a'`. Don't forget the header!