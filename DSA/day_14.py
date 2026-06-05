def longest_run(codes: list[str], k: int) -> int:
    counts = {}
    left = 0
    best = 0

    for right in range(len(codes)):
        right_code = codes[right]
        counts[right_code] = counts.get(right_code, 0) + 1
        
        while len(counts) > k :
            left_code = codes[left]
            counts[left_code] -=1
            if counts[left_code] == 0:
                del counts[left_code]
            left +=1
    
        window_size = right - left + 1
        if window_size > best:
            best = window_size

    return best

if __name__ == "__main__":
    codes = ["A", "B", "A", "C", "C", "A", "B", "B"]
    k =2
    result = longest_run(codes, k)
    print(f"codes = {codes}")
    print(f"k     = {k}")
    print(f"answer= {result}")