package policies

default is_santa = false

is_santa {
	valid_browser
    valid_cookie
   	valid_credentials
   	valid_code
}

valid_browser {
	input.headers["user-agent"] == "christmaseve"
}

valid_cookie {
	contains(input.headers.cookie, "gingerbread")
}

valid_credentials {
	basic_creds := base64.decode(split(input.headers.authorization, " ")[1])
    [user, password] := split(basic_creds, ":")
    user == "santa"
    lower(crypto.md5(password)) == "2eb71b743b4cc606434444acd65c124c"
}

valid_code {
	input.query_params.secret_code_2021 == "arcticcasual"
}

