<?php
session_start();
error_reporting(0);

	if (!isset($_SESSION["items"])) {
		$_SESSION["items"] = 0;
	}

	if (!isset($_SESSION["done"])) {
		$_SESSION["done"] = false;
	}

	if (!isset($_SESSION["time"])) {
		$_SESSION["time"] = 0;
	}

	$message = "";

	if ($_SESSION["done"] === true) {
		$message = "Your order was already processed.";
	}

	switch($_POST['action']) {
		case 'addcoupon': 
		if ($_POST['coupon'] === "FREE-TUQUE") {
			if ($_SESSION["items"] < 1 || abs(microtime(true) - $_SESSION["time"]) < 0.002) {
				$_SESSION["items"] = $_SESSION["items"] + 1;
			} else {
				$message = "You already made use of this coupon. No more than 1 free item of this type is allowed!";
			}
			$_SESSION["time"] = microtime(true);
		} else {
			$message = "This coupon is invalid. Try again.";
		}
		break;
		case 'executeorder':
			if ($_SESSION["items"] != 0) {
				$message = "Thank you for ordering! Santa will deliver your item on Christmas.";
				$_SESSION["done"] = true;
			}
		break;
	}
?>
<html>
	<head>
		<title>Free Montrehack Swag!!!</title>
	<head>
	<style>
		body {
		  background-color: rgb(16,16,16);
		  color: white;
		  font-family: sans-serif;
		}
		label {
		  background-color: indigo;
		  color: white;
		  padding: 0.5rem;
		  font-family: sans-serif;
		  border-radius: 0.3rem;
		  cursor: pointer;
		  margin-top: 1rem;
		}
		#file-chosen{
		  margin-left: 0.3rem;
		  font-family: sans-serif;
		}
		.animage {
		  height: 200px;
		  max-width: 300px;
		  margin: 50px;
		}
		footer {
		  color: gray;
		  text-align: center;
		  font-size: xx-small;
		}
		#page-container {
		  position: relative;
		  min-height: 100vh;
		}
		#content-wrap {
		  padding-bottom: 2.5rem;
		}
		#footer {
		  position: absolute;
		  bottom: 0;
		  width: 90%;
		  left: 5%;
		  height: 2.5rem;
		}
	</style>
	<script>
		async function script() {
			const actualBtn = document.getElementById('upfile');
			const fileChosen = document.getElementById('file-chosen');
			actualBtn.addEventListener('change', function(){
			  fileChosen.textContent = this.files[0].name;
			})

			document.getElementById("upfile").onchange = function() {
			    setTimeout(function () {
				document.getElementById("form").submit();
			    }, 1000);
			};
		}
	</script>

	<body onload="script();">
		<div id="page-container">
			<div id="content-wrap">
				<center><img src="tuque.webp" width="460px"/>

				<h1>Free Montrehack Swag</h1>

				<h2>Your Cart</h2>
				<table border="2" width="300" bgcolor="#181818">
					<tr>
						<th>Item</th>
						<th>Price</th>
					</tr>
<?php
	if ($_SESSION["items"] === 0) {
		echo "<tr><td colspan=2><center>Empty!</center></td></tr>";
	} else {
		for ($i = 0; $i < $_SESSION["items"]; $i++) {
			echo "<tr><td>Tuque</td><td>Free</td></tr>";
		}
		if ($_SESSION["items"] > 9) {
			echo "<tr><td>FLAG-</td><td>$1448.69</td></tr>";
		}
	}
?>

				</table>

<?php
	if ($message != "") {
		echo "<h3>$message</h3>";
	} else {
		echo "<br/>";
	}

	if ($_SESSION["done"] === false) {
?>

				Got a coupon? Use it here to get free stuff.<br/>
				<form enctype="multipart/form-data" id="form" method="POST">
					<input type="hidden" name="action" value="addcoupon">
					<input type="text" name="coupon">
					<input type="submit">
				</form>

				<br/>Have you reviewer your order?<br/>
				<form enctype="multipart/form-data" id="form" method="POST">
					<input type="hidden" name="action" value="executeorder">
					<input type="submit" value="Submit order">
				</form>
<?php
	}
?>
				</center>
			</body>
		</div>
		<footer id="footer">
			<p>Terms and conditions: We bear no responsibility if you don't actually receive anything. We do our best to deliver everything, but you really do need to have faith in Santa Claus if you expect to receive anything. Also, Santa gets the last word on who had a bad behavior this year. Use this web site at your own risk. All we can guarantee is that you get what you paid for. All orders are void for residents of Cuba, Quebec, North Korea, Syria and Sudan.</p>
		</footer>
	</div>
</html>
