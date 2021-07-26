CC=gcc
STANDARD_FLAGS=-Werror -std=c11 -pedantic -D_GNU_SOURCE -D_POSIX_SOURCE
DEBUG_FLAGS=-DDEBUG -g -Wall
RELEASE_FLAGS=-O2 -Wall
DEFP=-DFBG_PARALLEL
SRC_LIBS=fbg/src/lodepng/lodepng.c fbg/src/nanojpeg/nanojpeg.c fbg/src/fbgraphics.c fbg/custom_backend/fbdev/fbg_fbdev.c
LIBS1=-lm
LIBS2=-lm -lpthread
LIBS3=-lm -lpthread
LIBS_LFDS_711=liblfds711.a
LIBS_LFDS_720=liblfds720.a
INCS=-I fbg/src/ -I. -I fbg/custom_backend/fbdev
INCS3=-I fbg/src/ -I. -I fbg/custom_backend/fbdev
INCS_LFDS_711=-Iliblfds711
INCS_LFDS_720=-Iliblfds720

SRC1=$(SRC_LIBS) show_image.c
OUT1=show_image

all:
	$(CC) $(SRC1) $(INCS) $(STANDARD_FLAGS) $(RELEASE_FLAGS) $(LIBS1) -o $(OUT1)
