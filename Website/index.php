<html>
<head>
<link rel="stylesheet" type="text/css" href="styles.css">
<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
<title>DIE GRUPPE</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>  

<body >
    <div class="ueberschrift" id="header">
        <div id="button">DIE GRUPPE: <form action ="send.php" method="post"><input type="text" name="text" ><input type="submit" value="Senden"></form></div>
    </div>
<?php
$handle = fopen("/home/pi/Schreibtisch/Chat.txt","r");
while($inhalt = fgets($handle,4096))
{
echo "<div class='inhalt'>$inhalt</div><br>";
}
fclose($handle);
?>



<script>
    
function detectmob() { 
 if( navigator.userAgent.match(/Android/i)
 || navigator.userAgent.match(/webOS/i)
 || navigator.userAgent.match(/iPhone/i)
 || navigator.userAgent.match(/iPad/i)
 || navigator.userAgent.match(/iPod/i)
 || navigator.userAgent.match(/BlackBerry/i)
 || navigator.userAgent.match(/Windows Phone/i)
 ){
    return true;
  }
 else {
    return false;
  }
}
   



window.onscroll = function() {myFunction()};
var header = document.getElementById("header");
var sticky = header.offsetTop;
if(detectmob() == false){    
      setTimeout(sleep,3000);
        function sleep()
        {
            header.style.display ="flex";

            header.style.whiteSpace = "pre-wrap";
        }
 }else{
header.style.display ="flex";
header.style.whiteSpace = "pre-wrap";
}   
function myFunction() {
  if (window.pageYOffset >= sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

 var button = document.getElementById("button");
    var posC;
    button.addEventListener("mousedown",function()
        {
        
        var sa = window.getComputedStyle(button).getPropertyValue("margin-left").split("p");
              
        posC = event.clientX - sa[0];
        window.addEventListener('mousemove',move);
        window.addEventListener("mouseup",function(){
        window.removeEventListener("mousemove",move);
        });
        });
        button.addEventListener("dblclick",topScroll);
    
    
        
         function topScroll(){
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
        
    }
    
function move(){
   
       
        var pos = event.clientX - posC;
        button.style.marginLeft = pos + "px";
            
            }
    
    
    
</script>
</body>
</html>




