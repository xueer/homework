stuff = {:name => "Rob", :age => 30, :height => 5*12+10}
puts stuff[:name]
puts stuff[:age]
puts stuff[:height]
stuff[:city] = "New York"
puts stuff[:city]
stuff[1] = "Wow"
stuff[2] = "Neato"
puts stuff[1]
puts stuff[2]
puts stuff
stuff.delete(:city)
stuff.delete(1)
stuff.delete(2)
puts stuff