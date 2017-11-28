<!DOCTYPE html>
<html>
<head>
	<title>online</title>

</head>
<body style="  background: url(highscore.png) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
   background-color: #cccccc;">
%for x in listi:
	<h2>Name:</h2>
	{{x[0][0]}}

	<h2>Score:</h2>
	{{x[0][1]}}<br>
	----------------------------------------------------
%end





<form action="/">
	<button name="baka" type="submit">tilbaka</button>
</form>

</body>
</html>