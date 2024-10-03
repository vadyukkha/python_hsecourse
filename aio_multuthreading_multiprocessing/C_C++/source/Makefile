.PHONY: help

all: naive transposition vectorization kernel blocking optimization

help:
	@printf "\n"
	@grep -E '^[a-z].*:.*'  Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done
	@printf "\n"

naive: naive.cpp
	g++ -O3 -march=native -ffast-math -funroll-loops -std=c++20 -o ../executable_files/naive naive.cpp

transposition: transposition.cpp
	g++ -O3 -march=native -ffast-math -funroll-loops -std=c++20 -o ../executable_files/transposition transposition.cpp

vectorization: vectorization.cpp
	g++ -O3 -march=native -ffast-math -funroll-loops -std=c++20 -o ../executable_files/vectorization vectorization.cpp

kernel: kernel.cpp
	g++ -O3 -march=native -ffast-math -funroll-loops -std=c++20 -o ../executable_files/kernel kernel.cpp

blocking: blocking.cpp
	g++ -O3 -march=native -ffast-math -funroll-loops -std=c++20 -o ../executable_files/blocking blocking.cpp

optimization: optimization.cpp
	g++ -O3 -march=native -ffast-math -funroll-loops -std=c++20 -o ../executable_files/optimization optimization.cpp

clean:
	rm -f hash_map tests