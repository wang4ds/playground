from tqdm_batch import batch_process
import random
import time

def batch_process_function(row, some_var):
    time.sleep(0.01)
    return row + random.randint(0, some_var)


def main():
    N = 1_000
    items = range(N)

    result = batch_process(
        items,
        batch_process_function,
        some_var=42,
        n_workers=6,
        sep_progress=True,
    )
    
    
if __name__ == '__main__':
    main()