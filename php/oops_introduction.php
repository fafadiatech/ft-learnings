<?php 

/*
This is how multiple lines are written
*/

class Calc{
    // Inline comments are written like so
    public function add($val1, $val2){
        return $val1 + $val2;
    }

    public function is_even($num){
        if($num % 2 == 0){
            return true;
        }
        return false;
    }
}

$calc = new Calc();
echo $calc->add(10, 200);
?>