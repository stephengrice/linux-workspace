#!/bin/bash

WARNED=false

for f in `ls -A home`; do
	if [ -e ~/$f ] && ! $WARNED; then
		echo Warning: Files will be overwritten if you continue.
		while true; do
			echo -n "Continue? (y/n): "
			read user_in
			if [ "$user_in" = "y" ]; then
				WARNED=true
				break
			elif [ "$user_in" = "n" ]; then
				exit 0
			fi
		done
	fi
	echo Copying home/$f into place...
	cp home/$f ~
done

echo Done
