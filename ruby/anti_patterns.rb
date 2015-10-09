#This is based on an article: http://www.sitepoint.com/how-to-solve-coding-anti-patterns-for-ruby-rookies/

name = "Sidharth Shah"


#1. String interpolation
puts "1. String interpolation:"
puts "Hello " + name + ", how are you doing today? Time now is:" + Time.now.to_s 
puts "Hello #{name}, how are you doing today? Time now is:#{Time.now}" #More elegant

#Formatted interpolation, %w is used for word array
puts "\n2.Formatted interpolation:"
pets = %w{dog cat rabbit}
puts "My first pet is %s, second pet is %s and thrid one is %s" % pets
