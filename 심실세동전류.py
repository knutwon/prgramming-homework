import math

def calculate_vf_current(T):
    if T <= 0:
        raise ValueError("통전 시간은 0보다 커야 합니다.")
    I = 165 / math.sqrt(T)
    return I

def main():
    while True:
        try:
            T = float(input("통전 시간을 초 단위로 입력하세요 (0보다 큰 값, 종료하려면 음수 입력): "))
            if T < 0:
                print("프로그램을 종료합니다.")
                break
            I = calculate_vf_current(T)
            print(f"통전 시간 {T}초에 대한 심실세동전류는 {I:.2f} mA입니다.")
        except ValueError as e:
            print(f"입력 오류: {e}")
        except Exception as e:
            print(f"알 수 없는 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
