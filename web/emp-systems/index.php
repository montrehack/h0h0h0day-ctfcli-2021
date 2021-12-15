<?php
session_start();

$salt = bin2hex(random_bytes(35));
$options = [ 'cost' => 5 , 'salt' => $salt ];

// Options needed to hash the secret password. TODO: Add that to a database...
include('secret.php');

// Change that horrific technology that is json, let's go back to the real bliss that is XML
if ($_SERVER['CONTENT_TYPE'] == 'application/json') {
    $data = json_decode(file_get_contents('php://input'), true);
    $username = $data['username'];
    $password = $data['password'];
} elseif (isset($_POST['username']) && isset($_POST['password'])) {
	$username = $_POST['username'];
	$password = $_POST['password'];
}

if (isset($username) && isset($password)) {
    $logged_in = false;
    if ($username == $secret_admin) {
        if(password_hash($salt . $password, PASSWORD_BCRYPT, $options) == $secret_admin_hash) {
            $logged_in = true;
        }
    } else {
        $error = "Wrong user.... Are you sure you know what you're doing ?"; 
    }
}
?>

<HTML>
<link rel="stylesheet" href="style.css" type="text/css" />
<BODY>
	<h1>EMP Nuking System</h1>
    <div align='center'>
    <?php if(!isset($logged_in) || !$logged_in) { ?>
		<form method='POST'>
			<input type='text' name='username' placeholder='Username' autofocus />
			<input type='password' name='password' placeholder='Password' />
			<input type='submit' value='Login'/>
        </form>
    <?php } else { ?>
        <script>
            var i = 0;
            function move() {
              if (i == 0) {
                i = 1;
                var elem = document.getElementById("empBar");
                var width = 1;
                var id = setInterval(frame, 10);
                function frame() {
                  if (width >= 100) {
                    clearInterval(id);
                    i = 0;
                  } else {
                    width++;
                    elem.style.width = width + "%";
                  }
                }
              }
              document.getElementById("flag").innerText = "<?php echo $flag; ?>";
            }
        </script>
        <button onclick="move()" >Launch EMP</button>
        <div id="empProgress">
            <div id="empBar"></div>
        </div>
        <div id="flag"></div>        
    <?php } ?>
        <hr>
        <p>Only governments have access to this system !</p>
        <p>Sending an EMP to everybody's system will be at some point an obligation...</p>
        <p>This shall be done here !</p>
        <p>May the darkness bless our path to brightness !</p>
    </div>
    <?php if(isset($logged_in) && !$logged_in) { ?>
    <hr>
	<div class='error'>
    <?php if(isset($error)) { 
        echo "<small>$error</small><br>";        
    }?>
        <small>Access denied....</small>
	</div>
	<?php } ?>
</BODY>
</HTML>

