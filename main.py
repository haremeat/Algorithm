# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


n = 210

def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        if i < 100:
            cnt += 1
        else:
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt += 1
    return cnt

print(hansu(n))


n = int(input())

def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        if i < 100:
            cnt += 1
        else:
            nums = list(map(int,str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt += 1

    return cnt

print(hansu(n))