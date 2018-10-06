<?php 
    session_start();
    echo "hi ".$_SESSION['now']."   ";
    echo "<input type=\"submit\" value=\"登出\" onclick=\"location.href='logout.php'\">";
    echo "<br>"."<br>"."<br>";
?>
<html>
<head>
<title>xxxxx</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <table border="1">
        <tr>
            <td colspan='4'>
                PTT gamesale版 爬蟲結果顯示
            </td>
            <td>
                <input type="submit" value="重新爬蟲" onclick="location.href='main.php'">
            </td>
        </tr>
        <tr>
            <td>
                分類選項
            </td>
            <td>
                <form action="ps4s.php" method="post">
                    <p><input type="submit" value="PS4賣" onclick="location.href='ps4s.php?p=0'"><input type='hidden' name='a' value='1'></p>
                </form>
                <form action="ps4s.php" method="post">
                    <p><input type="submit" value="PS4收" onclick="location.href='ps4s.php?p=0'"><input type='hidden' name='a' value='2'></p>
                </form>
            </td>
            <td>
                <form action="nss.php" method="post">
                    <p><input type="submit" value="NS賣" onclick="location.href='nss.php?p=0'"><input type='hidden' name='b' value='1'></p>
                </form>
                <form action="nss.php" method="post">
                    <p><input type="submit" value="NS收" onclick="location.href='nss.php?p=0'"><input type='hidden' name='b' value='2'></p>
                </form>
            </td>
            <td>
                <form action="3dss.php" method="post">
                    <p><input type="submit" value="3DS賣" onclick="location.href='3dss.php?=0'"><input type='hidden' name='c' value='1'></p>
                </form>
                <form action="3dss.php" method="post">
                    <p><input type="submit" value="3DS收" onclick="location.href='3dss.php?=0'"><input type='hidden' name='c' value='2'></p>
                </form>
            </td>
            <td>
                <form action="xones.php" method="post">
                    <p><input type="submit" value="XBOX賣" onclick="location.href='xones.php?=0'"><input type='hidden' name='d' value='1'></p>
                </form>
                <form action="xones.php" method="post">
                    <p><input type="submit" value="XBOX收" onclick="location.href='xones.php?=0'"><input type='hidden' name='d' value='2'></p>
                </form>
            </td>
        </tr>
    </table>
    <?php
        $link = mysqli_connect("127.0.0.1","","","test") or die("no");
        mysqli_query($link,"SET NAMES 'utf8' ");

        $user = $_SESSION['now'];

        $sql = "SELECT * from `xxxxx` WHERE `owner` LIKE '%$user%' ";
        $result = mysqli_query($link,$sql);

        echo "<br>"."<br>"."<br>";
        echo "<h1>願望清單:</h1>";

        echo "<table border=\"1\" width=\"100%\">";
        echo "<tr>";
        echo "<td>刪除</td>";
        echo "<td>狀態</td>";
        echo "<td>種類</td>";
        echo "<td>標題</td>";
        echo "<td>網址</td>";
        echo "<td>地點</td>";
        echo "<td>地圖</td>";
        echo "</tr>";
        
        while($row = mysqli_fetch_row($result))
        {   
            echo "<tr>";
            echo "<td><form action=\"del.php\" method=\"post\">";
            echo "<input type=\"submit\" value=\"刪除\" onclick=\"location.href='del.php'\"><input type='hidden' name='add' value='$row[0]'>";
            echo "</form></td>";
            echo "<td>".$row[4]."</td>";
            echo "<td>".$row[1]."</td>";
            echo "<td>".$row[2]."</td>";
            echo "<td>".$row[3]."</td>";
            echo "<td>".$row[5]."</td>";
            echo "<td><iframe width=\"350\" height=\"150\" frameborder=\"0\" style=\"border:0\" src=\"https://www.google.com/maps/embed/v1/place?key=AIzaSyBFrddMMyl0WPe0rdtzHN7By69yPG0zAdU&q=".$row[5]."\" allowfullscreen></iframe></td>";
            echo "</tr>";
        }
        echo "</table>";
    ?>
</body>
</html>