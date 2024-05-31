import os
import pickle

def input_scores():
    sc = []
    a = 0
    i = 1
    while a >= 0:
        a = int(input(f"#{i}? "))
        if a >= 0:
            sc.append(a)
        i += 1
    return sc

def get_average(k):
    a = 0
    for i in range(len(k)):
        a += k[i]
    return a / len(k)

def show_list(nn):
    for d in nn:
        print(d, end=" ")

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename='score.bin'):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return []

def main():
    scores = load_scores()
    if scores:
        print("[파일 읽기]")
        print("[점수 출력]")
        print("개인점수: ", end="")
        show_list(scores)
        print(f"\n평균: {get_average(scores):.1f}")
    else:
        print("[점수 입력]")
        scores = input_scores()
        if scores:
            print("\n[점수 출력]")
            print("개인점수: ", end="")
            show_list(scores)
            print(f"\n평균: {get_average(scores):.1f}")
        
        save_scores(scores)

if __name__ == "__main__":
    main()
