# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
# There are two types of logs:
# 1. Letter-logs: all words except the identifier consist of lowercase English letters
# 2. Digit-logs: all words except the identifier consist of digits
#
# Reorder the logs so that:
# 1. All letter-logs come before any digit-log
# 2. Letter-logs are sorted lexicographically by their contents
# 3. If two letter-logs have the same contents, sort them by identifier
# 4. Digit-logs stay in the same relative order
#
# Return the final reordered list.
#
# ex:- logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# O/P -> ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

def reorderLogFiles(logs):
    result=[]
    digitLogs=[]
    letterLogs=[]
    for i in range(len(logs)):
        temp = logs[i].split(" ", 1)   
        if temp[1][0].isdigit():
            digitLogs.append(logs[i])
        else:
            partialVal = temp[1]       
            letterLogs.append((partialVal, temp[0], logs[i]))
    letterLogs.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(letterLogs)):
        result.append(letterLogs[i][2])
    result.extend(digitLogs)
    return result

print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
#O/P -> ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']