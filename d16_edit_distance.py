# Edit distance, Levenshtein distance
# Minimum number of operations

def edit_distance(s1, s2):
    """
    Return the minimum number or operations required to transform one string into the other.
    Operations - insert, remove and replace.
    """
    dist1 = list(range(len(s2) + 1))
    for i in range(len(s1)):
        dist2 = [i + 1]
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dist2.append(dist1[j])
            else:
                dist2.append(1 + min((dist1[j], dist1[j + 1], dist2[-1])))
        dist1 = dist2
    return dist1[-1]


print(edit_distance("Monday", "Tuesday"))  # -> 4
