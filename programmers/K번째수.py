def solution(array, commands):
    answer = []

    for command in commands :
        start = command[0] -1
        end = command[1]
        target = command[2] -1

        new_array = array[start:end]
        print(new_array)
        new_array.sort()
        answer.append(new_array[target])
    return answer
