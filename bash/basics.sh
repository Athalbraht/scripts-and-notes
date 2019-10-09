# var
###################
test="test"
cmm=`whoami`
cmm2=$(whoami)

echo "$test $cmm $cmm2"

# ARGS and loop
#######################

for i in $1 $2 $3; do
	echo "$i"
done

echo "#: $# ?: $?"

# FUNCTIONS
####################

function test1
{
echo "function test1 $1"
}

test2()
{
echo "function test2 $1"
}

test1 "x"
test2 "y"

# IF
##################

if [ 10 -ne 10 ]; then
	echo "IF"
else
	echo "else"
fi

# WHILE
########################
c=0
while [ $c -lt 2 ]; do
	let c+=1
	echo "c: $c"
done

