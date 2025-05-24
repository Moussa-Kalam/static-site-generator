import os
import shutil


def copy_files_recursive(source_dir_path, destination_dir_path):
	if not os.path.exists(destination_dir_path):
		os.makedirs(destination_dir_path)

	for filename in os.listdir(source_dir_path):
		from_path = os.path.join(source_dir_path, filename)
		destination_path = os.path.join(destination_dir_path, filename)
		if os.path.isfile(from_path):
			shutil.copy(from_path, destination_path)
		else:
			copy_files_recursive(from_path, destination_path)