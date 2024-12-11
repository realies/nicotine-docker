import os
import logging
from inotify_simple import INotify, flags
# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('/root/ownership_changes.log'),
        logging.StreamHandler()
    ]
)
# makes your downloads owned by your host user
# config
TARGET_DIR = "/root/nicotine-downloads"
UID = 1000
GID = 1000

def change_ownership(path):
    try:
        if os.path.islink(path):
            logging.info(f"Skipping symlink: {path}")
            return
        os.chown(path, UID, GID)
        if os.path.isdir(path):
            add_watch(path)
            for root, dirs, files in os.walk(path):
                for item in dirs + files:
                    change_ownership(os.path.join(root, item))
    except Exception as e:
        logging.error(f"Error processing {path}: {e}")

inotify = INotify()
inotify_numbers_to_path = {}
inotify_path_to_numbers = {}
# for any directory found, starting with the first one
def add_watch(dir):
    if dir in inotify_numbers_to_path:
        logging.debug(f"add_watch already: {dir}")
        return
    wd = inotify.add_watch(dir, flags.CREATE | flags.MOVED_TO)
    inotify_numbers_to_path[wd] = dir
    inotify_numbers_to_path[dir] = wd
    logging.debug(f"add_watch {wd}: {dir}")

def main():
    try:
        # initially, make sure
        change_ownership(TARGET_DIR)
        while True:
            for event in inotify.read():
                for flag in flags.from_mask(event.mask):
                    if flag in {flags.CREATE, flags.MOVED_TO}:
                        dir = inotify_numbers_to_path[event.wd]
                        full_path = os.path.join(dir, event.name)
                        logging.info(f"Detected event: {full_path} (flag: {flag})")
                        change_ownership(full_path)
    except KeyboardInterrupt:
        logging.info("Stopping ...")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        inotify.rm_watch(wd)

if __name__ == "__main__":
    main()
