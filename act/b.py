angoosht = int(input())
dast = int(input())

jam = int(input()) + int(input())

tedadekol = angoosht * dast

if jam % tedadekol == 0:
    print(tedadekol)
else:
    print(jam % (angoosht * dast))
