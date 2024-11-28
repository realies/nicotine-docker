import os
from inotify_simple import INotify, flags
# makes your downloads owned by your host user
# config
TARGET_DIR = "/root/nicotine-downloads"
UID = 1000
GID = 1000

def change_ownership(path):
    if os.path.islink(path):
        return
    os.chown(path, UID, GID)
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for item in dirs + files:
                change_ownership(os.path.join(root, item))

def main():
    inotify = INotify()
    watch_flags = flags.CREATE | flags.MOVED_TO
    wd = inotify.add_watch(TARGET_DIR, watch_flags)

    # initially, make sure
    change_ownership(TARGET_DIR)
    
    try:
        while True:
            for event in inotify.read():
                for flag in flags.from_mask(event.mask):
                    if flag in {flags.CREATE, flags.MOVED_TO}:
                        full_path = os.path.join(TARGET_DIR, event.name)
                        change_ownership(full_path)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        inotify.rm_watch(wd)

if __name__ == "__main__":
    main()
