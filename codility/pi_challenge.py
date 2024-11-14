from collections import Counter

def solution(P, Q):
   
    first = list(P)
    second = list(Q)


    counter = 0
    words = []

    word = ''

    while counter < len(P):

        if first[counter] == second[counter]:
            word += first[counter]

        elif first[counter] in common_keys\
        and first[counter] in Counter(word):
            word += first[counter]

        elif second[counter] in common_keys\
        and second[counter] in Counter(word):
            word += second[counter]

        elif first[counter] in common_keys\
        and a[first[counter]] > b[second[counter]]:
            word += first[counter]

        elif second[counter] in common_keys\
        and b[second[counter]] > a[first[counter]]:
            word += second[counter]

        elif a[first[counter]] > b[second[counter]]:
            word += first[counter]

        else:
            word += second[counter]
        counter += 1
    
    words.append(word)
    
    word = ''

    while counter < len(P):

        if first[counter] == second[counter]:
            word += first[counter]

        elif first[counter] in common_keys\
        and first[counter] in Counter(word):
            word += first[counter]

        elif second[counter] in common_keys\
        and second[counter] in Counter(word):
            word += second[counter]

        elif first[counter] in common_keys\
        and a[first[counter]] > b[second[counter]]:
            word += first[counter]

        elif second[counter] in common_keys\
        and b[second[counter]] > a[first[counter]]:
            word += second[counter]

        elif a[first[counter]] >= b[second[counter]]:
            word += first[counter]

        else:
            word += second[counter]
        counter += 1




    a = Counter(P)
    b = Counter(Q)

    common_keys = set(a.keys()).intersection(set(b.keys()))    