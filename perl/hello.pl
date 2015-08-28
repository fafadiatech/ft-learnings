#!/usr/bin/perl

#When using strict, you will absolutely need to write "my" before any var
use 5.014;
#use strict;
use warnings;

#This is how you define and process functions
sub BitchAboutOtherLanguages{
    foreach my $item (@_){
	#Good thinkg about this is you can embed variables in strings
	print "$item is so not cool language\n";
    }
    
}

#This is how a print line works
print "Hello world\n";

#This is how a for loop works
for(my $i=0; $i<10; $i++){
    print $i, " ", "Hello World\n";
}

#This is how you call a sub-routine
BitchAboutOtherLanguages("Python", "Ruby", "Golang");

#This is how you define a array one of the three different datastructures
#1. Scalar -> these are simple variables
#2. Array -> No explaination needed here
#3. Hash -> Its like dictionaries in python 
my @names = ("Sidharth", "Manan");

foreach my $name (@names){
    print "Welcome $name\n";
}

#This is how you find length of an array
print "There are " ,scalar @names ," elements in array\n";

#This is how you push elements into array, pop function is used to remove element from an array
push(@names, "Jayshree");

print "Folks I know @names\n";

#This is how you remove an element at a position
my @array = (44,55,66);
splice @array, 2, 1; # 66

print @array , "\n";

#This is how you define a hash
my %fav_colors = ("Sidharth", "Red", "Manan", "White");

#This is how you iterate over hash
foreach my $person (keys %fav_colors){
    print $person, " likes ", $fav_colors{$person}, " color very much\n";
}
