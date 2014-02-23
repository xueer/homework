#coding=UTF-8

formatter = "%r %r %r %r"   #可以换成%s 可以看出区别了.
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"so I said goodnight."
)