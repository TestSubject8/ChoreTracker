#include <sys/stat.h>
#include <signal.h>
#include <stdio.h>

#include "fbg/src/fbgraphics.h"
#include "fbg/custom_backend/fbdev/fbg_fbdev.h" // insert any backends from ../custom_backend/backend_name folder

int keep_running = 1;

void int_handler(int dummy) {
   keep_running = 0;
    // This kills the process continuously drawing onto the FB
    // The image stays on, radical!
}

int main(int argc, char* argv[]) {
    printf("Beginning");
    signal(SIGINT, int_handler);
    // open "/dev/fb0" by default, use fbg_fbdevSetup("/dev/fb1", 0) if you want to use another framebuffer
    // note : fbg_fbdevInit is the linux framebuffer backend, you can use a different backend easily by including the proper header and compiling with the appropriate backend file found in ../custom_backend/backend_name
    struct _fbg *fbg = fbg_fbdevInit();
    if (fbg == NULL) {
        return 0;
    }

    printf("Init done");

    //struct _fbg_img *texture = fbg_loadPNG(fbg, argv[1]);
    struct _fbg_img *texture = fbg_loadPNG(fbg, "OW-sc2.png");
    
    //struct _fbg_imgReached clear *texture = fbg_loadImage(fbg, argv[1]);
    struct _fbg_img *bb_font_img = fbg_loadPNG(fbg, "fbg/examples/bbmode1_8x8.png");
    printf("Images loaded");

    struct _fbg_font *bbfont = fbg_createFont(fbg, bb_font_img, 18, 18, 33);

    do {
        fbg_clear(fbg, 0); // can also be replaced by fbg_background(fbg, 0, 0, 0);

        fbg_draw(fbg);

        // you can also use fbg_image(fbg, texture, 0, 0)
        // but you must be sure that your image size fit on the display
        fbg_imageClip(fbg, texture, 0, 0, 0, 0, fbg->width, fbg->height);

        fbg_write(fbg, "Outer Wilds", 4, 2);
        fbg_write(fbg, fbg->fps_char, 32 + 8, 2 + 8);

        fbg_flip(fbg);

    } while (keep_running);

   // fbg_clear(fbg, 0); // can also be replaced by fbg_background(fbg, 0, 0, 0);
   // fbg_draw(fbg);

   // fbg_imageClip(fbg, texture, 0, 0, 0, 0, fbg->width, fbg->height);
   // //fbg_write(fbg, "Picture go brrrrrrrrrr", 4, 2);
   // fbg_write(fbg, "Outer Wilds", 4, 2);

   // fbg_draw(fbg);

    fbg_freeImage(texture);
    fbg_freeImage(bb_font_img);
    fbg_freeFont(bbfont);

    fbg_close(fbg);

    return 0;
}
