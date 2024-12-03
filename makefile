all: ac
	./ac

ac: ac.cc
	clang++ -std=c++20 -o ac ac.cc
