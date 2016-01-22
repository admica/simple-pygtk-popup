#!/usr/bin/env python

import gtk

class Popup(object):
    """Standalone Message Info dialog with Ok Button"""

    def __init__(self, title, msg, img, size):
        dialog = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, msg)
        dialog.set_title(title)
        dialog.set_position(gtk.WIN_POS_CENTER)

        try:
            pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(img, size, size)
            image = gtk.Image()
            image.set_from_pixbuf(pixbuf)
            image.show()
            dialog.set_image(image)
        except:
            pass

        dialog.run()
        dialog.destroy()

    def _quit(self, *args):
        gtk.main_quit()
        

if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'DEBUG':
        title = 'Test Title'
        msg = 'This is a test message.'
        img = 'icon.png'
        size = 42

    else:
        # read stdin lines for data, you could do it as inline arguments too
        title = sys.stdin.readline().strip() # Dialog Title
        msg = sys.stdin.readline().strip()  # Dialog Label
        img = sys.stdin.readline().strip() # Dialog Image Filename
        size = int(sys.stdin.readline().strip()) # Desired image pixel size

    Popup(title, msg, img, size)

    sys.exit(0)
