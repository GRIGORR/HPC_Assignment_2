import shutil
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time


def copy_file(src, dest):
	shutil.copy2(src, dest)
	
def main():
	
	t1 = time.time()
	copy_file('./filename.txt', './new_dest/new_file.txt_1')
	t2 = time.time()
	print(f'Without threading took {t2-t1} seconds')
	
	t3 = time.time()
	executor = ThreadPoolExecutor(5)
	future = executor.submit(copy_file, './filename.txt', './new_dest/new_file.txt_2')
	t4 = time.time()
	print(f'ThreadPoolExecutor took {t4-t3} seconds')
	
	t5 = time.time()
	executor = ProcessPoolExecutor(5)
	future = executor.submit(copy_file, './filename.txt', './new_dest/new_file.txt_3')
	t6 = time.time()
	print(f'ProcessPoolExecutor took {t6-t5} seconds')
	
if __name__ == '__main__':
	main()
