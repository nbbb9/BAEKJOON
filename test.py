#백준2번
# a, b = map(int, input().split())
# print(a+b)

#백준3번
# a, b = map(int, input().split())
# print(a - b)

#백준6번
# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)

#백준7번
def CheckDuplicate(id):
    if id.isalpha():
        if id.islower():
            if len(id) <= 50:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

id = input()
result = CheckDuplicate(id)
if result:
    print(id + "??!")