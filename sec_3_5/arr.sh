#########################################################################
# File Name: arr.sh
# Author: lw3968
# mail: cainiao367@163.com
# Created Time: 2018年03月01日 星期四 10时54分25秒
#########################################################################
#!/bin/bash

ar=(A "B" C D)

echo ${ar[1]}
echo ${ar[@]}
echo ${ar[*]}

echo ${#ar[*]}
echo ${#ar[@]}

good_man(){
    echo $1
    echo $2
    echo $3
}

for item in ${ar[@]};
do
    echo $item
done


good_man w x y
echo $1 $2 $3

