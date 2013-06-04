tax_rate = 0.1
month = 15
puts "How much you earn every month?"
sal = gets.chomp()
salary = sal.to_f
base_tax_salary = 1000

tax = (salary - base_tax_salary) * tax_rate
years_tax = tax * month
puts "you have #{salary} pay tax #{tax} a month ."
puts "you should pay tax #{years_tax} a year ."


