<?php

$conn = mysqli_connect('localhost', 'jayse', 'privetpoka', 'test');
$sql = "SELECT name, image FROM images WHERE id=4";
$result = $conn->query($sql);

while($row = $result->fetch_assoc()) {
    $name = $row["name"];
    $image = $row["image"];
    $im = file_put_contents($name, $image);
    echo "Done!";
}
?>