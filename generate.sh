#!/bin/bash

# 3 genre directories
text=(society.txt sports.txt goverment.txt)

# all remove 3 genre text files
rm -v *.txt

echo "---------------------------------------------------------"
echo "Generating ...\n"
# generate text files
for txt in ${text[@]}
do
	touch $txt
	chmod 755 $_
  echo $txt
done

exit 0