<?php
session_start();

include('secret.php');

function parse_token($token) {
    $params = explode('&', $token);
    $parsed = array();
    foreach ($params as $param) {
        $key = explode('=', $param, 2)[0];
        $value = explode('=', $param, 2)[1];
        if (!isset($parsed[$key])) {
            $parsed[$key] = $value;
        }
    }
    return $parsed;
}

$password = $_POST['password'];
$method = "aes-256-cbc";

if (isset($password)) {
    if(strpos($password, '&') !== false) {
        $errorMsg = "Invalid characters used...";
    } else {
        $iv = bin2hex(random_bytes(8));
        $token = "username=guest&password=$password&auth=false";
        $crypted_token = openssl_encrypt($token, $method, $key, 0, $iv);
        $crypted_token = $iv . ".:." . $crypted_token;
        setcookie('token', $crypted_token, time() + (3600 * 24), "/");
    }
} else {
    $crypted_token = $_COOKIE['token'];
}

if (isset($crypted_token)) {
    $iv = explode(".:.", $crypted_token, 2)[0];
    $crypted_token = explode(".:.", $crypted_token, 2)[1];

    $token = openssl_decrypt($crypted_token, $method, $key, 0, $iv);
    $params = parse_token($token);
    
    $username = $params['username'];
    $password = $params['password'];
    $auth = $params['auth'];

    if ($password === 'Un10N') {
        $logged_in = true;
        if ($username === 'admin' && $auth === 'true') {
            $is_admin = true;
        } else {
            $is_admin = false;
        }
    } else {
        $errorMsg = "Milicia won't penetrate us ! You might have mistyped the password, but we're watching you !";
        $logged_in = false;
    }
}

?>

<HTML>
<link rel="stylesheet" href="style.css" type="text/css" />
<BODY>
	<h1>Protect, attack, but most importantly, hack back</h1>
    <div align='center'>
        <p>See what you can do against big brother !</p>
        <hr>
        <?php if(!$logged_in) { ?>
            <form method="post">
                <input type="password" name="password" placeholder="Password" />
                <input type="submit" value="Login" />
            </form>
            </br>
            <small>If you're really part of the revolution, you should have received the password to log in...</small>
        <?php } elseif (!$is_admin) { ?>
            <h3>Hi comrade !</h3>
            <p>If we reached to you it's because you know how to hack.</p>
            <p>The government wants us to stop using technology, but they keep using it for their operations...</p>
            <p>Their propaganda must stop, their reign shall end !</p>
            <p>Bring truth to the world ! Leak everything you can !</p>
        <?php } elseif ($is_admin) { ?>
            <h3>We bow to you, comrade leader !</h3>
            <p>Raise your flag above in the air and people will follow you !</p>
            <p>With your lead, we'll bring down their disguised dictatorship !</p>
            <p><?php echo $flag; ?></p>
        <?php } ?>
    </div>
    <?php if(isset($errorMsg)) { ?>
    <hr>
	<div class='error'>
        <small><?php echo $errorMsg; ?></small>
    </div>
    <?php } ?>
</BODY>
</HTML>
