<!DOCTYPE html>
<html>
<head>
	<title>online</title>
</head>
<body>
%for x in listi:
	<h2>Name:</h2>
	{{x[0][0]}}

	<h2>Score:</h2>
	{{x[0][1]}}<br>
	----------------------------------------------------
%end




<form action="/eyda">
	<button name="Nytt" type="submit" >eyða</button>
</form>

<form action="/">
	<button name="baka" type="submit">tilbaka</button>
</form>

</body>
</html>