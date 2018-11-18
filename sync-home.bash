#!/bin/bash

for f in `ls -A home`; do
	echo Copying home/$f into place...
	cp home/$f ~
done

echo Done
