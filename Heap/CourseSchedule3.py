# There are n online courses labeled from 1 to n. Each course is represented as courses[i] = [durationi, lastDayi],
# where durationi is the number of days required to complete the course and lastDayi is the last day by which 
# the course must be finished.
#
# You start on day 1 and can only take one course at a time (no overlapping courses allowed).
#
# Return the maximum number of courses you can complete.
#
# ex:- courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# O/P -> 3
#
# Explanation:
# Take course [100,200] -> finish on day 100
# Take course [1000,1250] -> finish on day 1100
# Take course [200,1300] -> finish on day 1300
# Cannot take [2000,3200] as it would exceed its deadline
import heapq

def scheduleCourse(courses) :
    total_duration=0;courses_duration=[];max_heap=[];result=0;maxi=0
    courses.sort(key=lambda x: x[1])
    for i in range(len(courses)):
        current_course=courses[i]
        if total_duration + current_course[0]<= current_course[1]:
            total_duration+=current_course[0]
            heapq.heappush(max_heap, -current_course[0])
            result+=1
            maxi = max(maxi, result)
        else:
            if not len(max_heap) or current_course[0] > -max_heap[0]:
                continue
            while len(max_heap):
                total_duration-=-heapq.heappop(max_heap)
                result-=1
                if total_duration+current_course[0]<= current_course[1]:
                    total_duration+=current_course[0]
                    heapq.heappush(max_heap, -current_course[0])
                    result+=1
                    maxi = max(maxi, result)
                    break
    return maxi

print(scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]])) # O/P -> 3