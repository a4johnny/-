<html>
<head>
<title>xxxxx</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <?php
    $aa = 'https://www.ptt.cc/bbs/Gamesale/index.html';
    $link = mysqli_connect("127.0.0.1","","","test") or die("no");
    mysqli_query($link,"SET NAMES 'utf8' ");
    for($i=0;$i<=5;$i++){
      $u = fopen ($aa,"r");
      $contact = "";

      while ($buf = fgets($u, 1024)){
          //echo $buf;
          $contact .= $buf;
      }
      $k=-1;
      $pos = stripos($contact, "上頁",$k+1);
      //echo $pos;
      $lastnet = substr($contact,$pos -39,28);
      $lastnet = "https://www.ptt.cc".$lastnet;
      //echo $lastnet."<br>";

      $pos2 = stripos($contact, "class=\"search-bar\"",$k+1);
      $j=$pos2;
      while($j = stripos($contact, "<a href=\"",$j+700))
      {   
          $w = stripos($contact,"[",$j);
          $w1 = stripos($contact,"]",$j);
          $l = stripos($contact,'</a>',$w);
          
          $net = substr($contact,$w-39 ,37);
          $class = substr($contact,$w ,$w1 -$w+1);
          $str = substr($contact,$w1+1 ,$l -$w1-1);
          $str2 = substr($contact,$w1+1,4);
          
          $newnet = "https://www.ptt.cc".$net;
          /*if(strncmp($net,"/bbs",4) == 0)
            echo $newnet."<br>";*/
          //$nnewnet = $newnet;
          //$sss = strlen($net);
          //echo ($net)."<br>\n";
          /*if (isset($sss)){
            echo "123".$newnet.$sss."<br>";
          }*/
          
          
          if(strncmp($net,"/bbs",4) == 0){
            $u1 = fopen ($newnet,"r");
            $pas = "";
            while ($buf = fgets($u1, 1024)){
              $pas .= $buf;
            }
            $p = -1;
            $p = stripos($pas,"地",0);
            $p1 = stripos($pas,"：",$p);
            $p2 = stripos($pas,"【",$p1);
            $local = substr($pas,$p1+3 ,$p2-$p1-3);

            if (strlen($local) < 70 && $p > 100){
              echo $p.$class." ".$str." ".$newnet." ".$local."<br>";
              mysqli_query($link, "INSERT INTO `xxxxx` (`class`,`title`,`net`,`state`,`location`) VALUES (N'".$class."',N'".$str."','$newnet',N'".$str2."',N'".$local."')");
            }
          }
      }
      $aa = $lastnet;
      echo $lastnet."<br>";
    }
      echo "<center>";
      echo "<input type=\"submit\" value=\"返回\" onclick=\"location.href='show.php'\">";
      echo "</center>";
     ?>
</body>
</html>