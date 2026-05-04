import pandas as pd


def add(x: int, y: int) -> int:
    return x + y


def main():
    df = pd.DataFrame(
        {"a": [add(1, 2), add(1, 4), add(1, 7)]}
    )
    result_dict = df.to_dict()
    print(f"result_dict: {result_dict}")
    return result_dict


if __name__ == '__main__':
    main()
