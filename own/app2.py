a=input("enter the number")

start=0
end=1
for i in a:
    answer=start+end
    start=end
    end=answer

print(answer)
