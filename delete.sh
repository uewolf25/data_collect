#!/bin/bash

# 3 genre directories
directory=(general sports business)

# all remove 3 genre text files
rm -v *.txt

echo "---------------------------------------------------------"

# all remove dir
for dir in ${directory[@]}
do
	rm -r -v $dir
	# echo  $dir
done

exit 0

