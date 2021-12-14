# h0h0h0
### Description

Host your web gifts here temporarily, I'm sure nothing bad will happen ;)

### How to run
`docker-compose up`

### Writeup

It is pretty straight forward, there's a command injection in the port field when creating a new session.
1. Set the port field to `31337 -v /:/host`, you might need burp for this one.
2. Set the image to a custom webshell that has a healthcheck and runs as user 1000 eg: `kptcheesewhiz/phpwebshell`.
3. Run the command `sudo cat /host/flag` in the input field.
