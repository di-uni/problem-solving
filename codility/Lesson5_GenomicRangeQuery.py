# First Trial
# 62% (Correctness 100%, Performance 0%)

def solution(S, P, Q):
    DNA = {"A": 1, "C": 2, "G": 3, "T": 4}
    result = []

    for p, q in zip(P, Q):
        minimal = 4
        for i in range(p, q + 1):
            minimal = min(DNA[S[i]], minimal)
            if minimal == 1:
                break
        result.append(minimal)

    return result


# ====================================
# Other's solution
# 문자별로 prefixSum 구하기

def solution(S, P, Q):
    cnt = {"A": 0, "C": 0, "G": 0, "T": 0}
    impactA = [0] * len(S)
    impactC = [0] * len(S)
    impactG = [0] * len(S)
    impactT = [0] * len(S)
    result = []


    for i, s in enumerate(S):
        cnt[s] += 1
        impactA[i] = cnt["A"]
        impactC[i] = cnt["C"]
        impactG[i] = cnt["G"]
        impactT[i] = cnt["T"]

    for p, q in zip(P, Q):
        if p == 0:
            if impactA[q] > 0:
                result.append(1)
                continue
            elif impactC[q] > 0:
                result.append(2)
                continue
            elif impactG[q] > 0:
                result.append(3)
                continue
            else:
                result.append(4)
                continue
        if impactA[q] - impactA[p - 1] > 0:
            result.append(1)
            continue
        elif impactC[q] - impactC[p - 1] > 0:
            result.append(2)
            continue
        elif impactG[q] - impactG[p - 1] > 0:
            result.append(3)
            continue
        else:
            result.append(4)
            continue

    return result


