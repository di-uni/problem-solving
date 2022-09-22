def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    h = 1
    
    for cit in sorted_citations:
        if h == cit:
            return h
        elif h > cit:
            return h - 1
        h += 1
            
    return h - 1