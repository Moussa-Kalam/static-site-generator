import os
import shutil
from copy_static_from_source_to_destination import copy_files_recursive

static_dir_path = "./static"
public_dir_path = "./public"

def main():
	print('Deleting "public" directory...')
	if os.path.exists(public_dir_path):
		shutil.rmtree(public_dir_path)

	print('Copying "static" files... to "public" directory...')
	copy_files_recursive(static_dir_path, public_dir_path)

main()
