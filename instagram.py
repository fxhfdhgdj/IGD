import os
if __name__ == "__main__":
        try:
                __import__("instaxrex").checkin()
        except Exception as e:
                exit(str(e))
