# 5분이 지나기 전에 중지했다면 실제로 공부한 시간에 포함x
#  최소 5분 최대 1시간 45분

from datetime import datetime

# def list_chunk(lst, n):
#     return [lst[i:i+n] for i in range(0, len(lst), n)]

# list_chunked = list_chunk(log, 2)

log = ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]


def solution(log):
    answer = ''

    study_time = 0

    for i in range(len(log) // 2):

        if i == 0:
            time_1 = datetime.strptime(log[0], "%H:%M")
            time_2 = datetime.strptime(log[1], "%H:%M")
        else:
            time_1 = datetime.strptime(log[2 * i], "%H:%M")
            time_2 = datetime.strptime(log[2 * i + 1], "%H:%M")

        time_interval = time_2 - time_1

        times = str(time_interval).split(":")

        hour = int(times[0])
        minute = int(times[1])

        total_bun = int((hour * 60) + minute)

        if total_bun < 5:
            total_bun = 0
        elif total_bun >= 105:
            total_bun = 105

        # print(total_bun)

        study_time += total_bun

    hours = int(study_time) // 60
    minutes = int(int(study_time) - int(hours * 60))

    if hours < 10:
        answer = "0" + str(hours) + ":" + str(minutes)
    else:
        answer = str(hours) + ":" + str(minutes)

    return answer
