#!/bin/bash
# @fob
set -eu

tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT INT QUIT TERM
cd $tmpdir

echo "id: $(id)"
echo "pwd: $(pwd)"
echo ""


show_menu() {
	cat << __EOF__
What do you want to do?

  1) Add files
  2) List files
  3) Show me the source!
  4) Leave!  o( >< )o  This is stupid!

__EOF__
}

add_file() {
	printf "How do you want to name your file?\n> "
	read fname
	printf "What type of file? [d/s/F]\n> "
	read ftype

	fname=${fname##*/}
	case $ftype in
	d)	mkdir -p $fname;;
	s)	ln -s /flag $fname;;
	*)	touch $fname;;
	esac
	echo "File created!"
}

list_files() {
	printf "Here are your files\n\n"

	for f in *; do
		if [ -d $f ]; then
			echo "D $f"
		elif [ -L $f ]; then
			echo "L $f -> $(readlink $f)"
		elif [ -f $f ]; then
			echo "F $f"
		else
			echo "U $f"
		fi
	done

	echo ""
}

nerrs=0
while :; do
	if [ $nerrs -eq 3 ]; then
		echo "Okay, time for you to go to sleep!"
		exit 0
	fi

	show_menu

	printf '> '
	read choice
	case $choice in
	1)	add_file;;
	2)	list_files;;
	3)	cat $0;;
	4)	exit 0
		;;
	*)	echo "Invalid choice"
		nerrs=$(( $nerrs + 1 ))
		;;
	esac
done

exit 0
