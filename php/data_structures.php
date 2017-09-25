<?php
    
    // This is how you import external files
    include("oops_introduction.php");

    // Sample function 
    function add($val1, $val2){
        return $val1 + $val2;
    }

    // All variable names are started with $ sign
    // This is how arrays are define
    $cars = array("Nissan", "Honda");

    // & is similar to c value is assigned by reference
    // foreach is used to loop through the array
    foreach($cars as &$current_car){
        // . operator is used for concatenation
        echo $current_car . "\n";
    }

    // Dictionaries/Maps are called Associate Arrays in PHP
    $fav_colors = array("sidharth" => "blue", "khyati" => "pink");
    echo "Sidharth's fav colors is" . $fav_colors["sidharth"] . "\n";

    // This is how iterating through PHP works
    foreach($fav_colors as $person => $color){
        echo $person . "->" . $color . "\n";
    }

    // Remember to terminate all lines with a semi-colon
    $random_nums = array(2, 3, 0, 10, -1);
    sort($random_nums);
    foreach ($random_nums as &$current_num) {
        echo $current_num . "\n";
    }

    // Calling a function
    echo "Call made to add function yielded result:" . add(3, 40) . "\n";

    // Lets use class defined in external file
    $calc = new Calc();
    echo "Call made to add function {from oops_introduction.php} yielded:" . $calc->add(50, 5) . "\n";

    if($calc->is_even(2)){
        echo "Yup is_even method works fine\n";
    }
?>