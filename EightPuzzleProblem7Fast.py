#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import sys
import collections
import time
import random
def allStates(numbers, states):
    l = list()
    index = numbers.find("_")
    for place in states[index]:
        newNum = numbers[:index] + numbers[place] + numbers[index + 1:]
        newNum = newNum[:place] + "_" + newNum[place + 1:]
        l.append(newNum)
    return l

def puzzling(start, theList, states, goal):
    keysSeen = set()
    alreadySeen = dict()
    alreadySeen[start] = ""
    keysSeen.add(start)
    parseMe = collections.deque()
    parseMe.append(start)
    while len(parseMe) > 0:
        element = parseMe.popleft()
        newList = allStates(element,states)
        for i in newList:
            if i not in keysSeen:
                alreadySeen[i] = element
                if i == goal:
                    return alreadySeen
                parseMe.append(i)
                keysSeen.add(i)
    return []

def createStates():
    states = dict()
    states[0] = {1,3}
    states[1] = {0,2,4}
    states[2] = {1,5}
    states[3] = {0,4,6}
    states[4] = {1,3,5,7}
    states[5] = {2,4,8}
    states[6] = {3,7}
    states[7] = {4,6,8}
    states[8] = {5,7}
    return states

def printer(numbers):
    numbers = numbers[:3] + "\n" + numbers[3:6] + "\n" + numbers[6:]
    return numbers

def findIndex(d, element):
    for key in d:
        if element in d[key]:
            return key

def findStepsPrint(goal):
    states = createStates()
    finalStates = dict()
    where = set()
    count = 0
    finalStates[count] = {goal}
    where.add(goal)
    while len(finalStates[count]) > 0:
        eSet = set()
        for element in finalStates[count]:
            eSet = eSet.union(allStates(element,states))
        eSet = newSet(eSet, where)
        for thing in eSet:
            where.add(thing)
        finalStates[count + 1] = eSet
        if count + 1 == 31:
            print(eSet)
            break
        #print("Steps:",count + 1, "Number of States:", len(finalStates[count +1]),"States:",finalStates[count + 1])
        print(count + 1,":",len(finalStates[count + 1]))
        count += 1
    return finalStates

def newSet(eSet, where):
    anotherSet = set()
    for thing in eSet:
        if thing not in where:
            anotherSet.add(thing)
    return anotherSet

def makeRandom():
    nums = set()
    test = ""
    for index in range(1,9):
        nums.add(str(index))
    nums.add("_")
    while len(nums) > 0:
        test += nums.pop()
    return test

goal = sys.argv[1]
findStepsPrint(goal)
# goal = "12345678_"
# totalTime = 0
# totalSteps = 0
# totalSolutions = 0
# for num in range(1000):
#     startTime = time.clock()
#     # print("keys:",d.keys())
#     # print("startKey:",startKey)
#     # print("d[startKey]:",d[startKey])
#     start = makeRandom()
#     l = list()
#     if start == goal:
#         totalTime += time.clock() - startTime
#         totalSolutions += 1
#     else:
#         states = createStates()
#         dic = puzzling(start, allStates(start, states), states, goal)
#         if len(dic) == 0:
#             totalTime += time.clock() - startTime
#         else:
#             key = goal
#             l.append(key)
#             while len(dic[key]) > 0:
#                 l.append(dic[key])
#                 key = dic[key]
#             totalTime += time.clock() - startTime
#             totalSteps += len(l) - 1
#             totalSolutions += 1
#     print("Total Time:", totalTime)
#     print("Total Steps:", totalSteps)
#     print("Total Solutions:", totalSolutions)
# print("Average Time:",totalTime/1000,"Average Steps:",totalSteps/totalSolutions, "Total Solutions:",totalSolutions)