<?php 
    session_start();
?>
<html>
<head>
<title>xxxxx</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <?php
    if (isset($_POST['b']) != false){
        $aa = $_POST['b'];
    }
    else{
        $aa = $_SESSION['ns'];
    }

    $_SESSION['ps4']=0;
    $_SESSION['xone']=0;
    $_SESSION['3ds']=0;
    $_SESSION['ns']=$aa;

    if (isset($_GET["p"]) != false){
        $page=$_GET["p"];
    }
    else{
        $page = 0;
    }
    //echo $aa;
    $link = mysqli_connect("127.0.0.1","","","test") or die("no");
    mysqli_query($link,"SET NAMES 'utf8' ");

    $sql = "SELECT * from `xxxxx` WHERE `class` LIKE '%NS%'";
    $result = mysqli_query($link,$sql);
    $count = 0;

    echo "<input type=\"submit\" value=\"返回\" onclick=\"location.href='show.php'\">";

    echo "<table border=\"1\" width=\"100%\">";
    echo "<tr>";
        echo "<td>加入清單</td>";
        echo "<td>狀態</td>";
        echo "<td>種類</td>";
        echo "<td>標題</td>";
        echo "<td>網址</td>";
        echo "<td>地點</td>";
        echo "<td>地圖</td>";
        echo "</tr>";
    while($row = mysqli_fetch_row($result))
    {   
        if ($count < 10){
            if ($aa == '1'){
                if (strpos($row[4], '徵') == false && $row[0]>$page){
                    echo "<tr>";
                    echo "<td><form action=\"plus.php\" method=\"post\">";
                    echo "<input type=\"submit\" value=\"新增\" onclick=\"location.href='plus.php'\"><input type='hidden' name='add' value='$row[0]'>";
                    echo "</form></td>";
                    echo "<td>".$row[4]."</td>";
                    echo "<td>".$row[1]."</td>";
                    echo "<td>".$row[2]."</td>";
                    echo "<td>".$row[3]."</td>";
                    echo "<td>".$row[5]."</td>";
                    echo "<td><iframe width=\"350\" height=\"150\" frameborder=\"0\" style=\"border:0\" src=\"https://www.google.com/maps/embed/v1/place?key=AIzaSyBFrddMMyl0WPe0rdtzHN7By69yPG0zAdU&q=".$row[5]."\" allowfullscreen></iframe></td>";
                    echo "</tr>";
                    $count++;
                    $last = $row[0];
                }
            }

            else if ($aa == '2'){
                if (strpos($row[4], '徵') != false && $row[0]>$page){
                    echo "<tr>";
                    echo "<td><form action=\"plus.php\" method=\"post\">";
                    echo "<input type=\"submit\" value=\"新增\" onclick=\"location.href='plus.php'\"><input type='hidden' name='add' value='$row[0]'>";
                    echo "</form></td>";
                    echo "<td>".$row[4]."</td>";
                    echo "<td>".$row[1]."</td>";
                    echo "<td>".$row[2]."</td>";
                    echo "<td>".$row[3]."</td>";
                    echo "<td>".$row[5]."</td>";
                    echo "<td><iframe width=\"350\" height=\"150\" frameborder=\"0\" style=\"border:0\" src=\"https://www.google.com/maps/embed/v1/place?key=AIzaSyBFrddMMyl0WPe0rdtzHN7By69yPG0zAdU&q=".$row[5]."\" allowfullscreen></iframe></td>";
                    echo "</tr>";
                    $count++;
                    $last = $row[0];
                }
            }
        }
    }
    echo "</table>";

    echo "<center>";
        if( $count >= 10 && $page != $last)
        {
            echo "<h1><a href=\"nss.php?p=".$last."\">下一頁</a></h1>";
        }
        else {
            echo "<h1>最後一頁</h1>";
        }
    echo "</center>"; 

    ?>
</body>
</html>