
def apfd(prioritization, fault_matrix):
    """INPUT:
    (list)prioritization: list of prioritization of test cases
    (dict)fault_matrix: key=tcID, val=[detected faults]

    OUTPUT:
    (float)APFD = 1 - (sum_{i=1}^{m} t_i / n*m) + (1 / 2n)
    n = number of test cases
    m = number of faults detected
    t_i = position of first test case revealing fault i in the prioritization
    Average Percentage of Faults Detected
    """

    detected_faults = set()
    numerator = 0.0  # numerator of APFD
    position = 1
    for tc_ID in prioritization:
        for fault in fault_matrix[tc_ID]:
            if fault not in detected_faults:
                detected_faults.add(fault)
                numerator += position
        position += 1

    n, m = len(prioritization), len(detected_faults)
    apfd = 1.0 - (numerator / (n * m)) + (1.0 / (2 * n)) if m > 0 else 0.0

    return apfd


def apbd(prioritization, truebugs):
    """INPUT:
    (list)prioritization: list of prioritized violations
    (list)truebugs: list of violation IDs that are truebugs

    OUTPUT:
    (float)APBD = 1 - (sum_{i=1}^{m} t_i / n*m) + (1 / 2n)
    n = number of violations
    m = number of violations that are truebugs
    t_i = position of a violation that is a truebug
    Average Percentage of Bugs Detected
    """

    detected_bugs = set()
    numerator = 0.0  # numerator of APBD
    position = 1
    for vio in prioritization:
        if vio in truebugs:
            detected_bugs.add(vio)
            numerator += position
        position += 1

    n, m = len(prioritization), len(detected_bugs)
    apbd = 1.0 - (numerator / (n * m)) + (1.0 / (2 * n)) if m > 0 else 0.0

    return apbd


def apbd_norm(prioritization, truebugs):
    """INPUT:
    (list)prioritization: list of prioritized violations
    (list)truebugs: list of violation IDs that are truebugs

    OUTPUT:
    (float)APBD = 1 - (sum_{i=1}^{m} t_i / n*m) + (1 / 2n)
    n = number of violations
    m = number of violations that are truebugs
    t_i = position of a violation that is a truebug
    (NORMALIZED) Average Percentage of Bugs Detected
    """

    def _get_optimal_apbd(prioritization, truebugs):
        tb = set(prioritization).intersection(set(truebugs))
        nb = set(prioritization).difference(set(truebugs))
        optimal_p = list(tb)+list(nb)
        return apbd(optimal_p, truebugs)

    apbd_ = apbd(prioritization, truebugs)
    #print("APBD: {}".format(apbd_))

    optimal_apbd = _get_optimal_apbd(prioritization, truebugs)
    #print("Optimal APBD: {}".format(optimal_apbd))    

    return apbd_ / optimal_apbd


def precision_at_k(prioritization, truebugs_list, k_list, mode="percentage"):
    precision = []
    for k in k_list:
        prio = prioritization[:k]        
        inter = set(prio).intersection(set(truebugs_list))
        if mode == "absolute":
            precision_k = len(inter)/float(k)
        elif mode == "percentage":
            precision_k = len(inter)/float(len(truebugs_list))
        #print("prioritization: {} | inter: {} | precision: {}".format(prio, inter, precision_k))
        precision.append(precision_k)
    return precision


if __name__ == '__main__':
    fault_matrix = {'a': [1, 5],
                    'b': [6, 7],
                    'c': [1, 2, 3, 4, 5, 6, 7],
                    'd': [5],
                    'e': [8, 9, 10]}


    prioritization = ['a', 'b', 'c', 'd', 'e']
    actual = apfd(prioritization, fault_matrix)
    expected = 0.5
    assert(actual == expected), "actual: {} | expected: {}".format(actual, expected)


    prioritization = ['e', 'd', 'c', 'b', 'a']
    actual = apfd(prioritization, fault_matrix)
    expected = 0.64
    assert(actual == expected), "actual: {} | expected: {}".format(actual, expected)
    

    prioritization = ['c', 'e', 'b', 'a', 'd']
    actual = apfd(prioritization, fault_matrix)
    expected = 0.84
    assert(actual == expected), "actual: {} | expected: {}".format(actual, expected)

    prioritization = ['b', 'a', 'c', 'd', 'e']
    actual = apfd(prioritization, fault_matrix)
    expected = 0.5
    assert(actual == expected), "actual: {} | expected: {}".format(actual, expected)
    
    #-----
    prioritization = [1,2,3,4,5,6,7,8,9,10]
    truebugs = [6,8,10]
    res = apbd(prioritization, truebugs)
    print(res)

    #-----
    prioritization = [10,2,3,4,5,6,7,8,9,1]
    truebugs = [6,8,10]
    print(apbd(prioritization, truebugs))
    print(apbd_norm(prioritization, truebugs))


    #-----
    prioritization = [3, 30, 78, 16, 27, 40, 50, 52, 55, 57, 73, 80, 106, 14, 15, 16, 17, 18, 19, 20]
    truebugs = [3,40, 20]
    #precision_at_k(prioritization, truebugs, [5,10,15,20])