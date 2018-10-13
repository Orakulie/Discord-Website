<html>
<body>

<?php

error_reporting(E_ALL);
echo $undef9306;
$txt = $_POST["text"];
echo "$txt";
if($txt != "")
{
$fh = fopen("/home/pi/Schreibtisch/Send.txt","w");
fwrite($fh, $txt);
fclose($fh);
}
header("Location:index.php");
?>
</body>
</html>
