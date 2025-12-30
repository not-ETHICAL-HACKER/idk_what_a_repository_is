# import threading
# import time


# def task(name: str) -> None:
#     """Simulates an I/O operation (e.g., download)"""
#     print(f"Thread {name}: starting...")
#     time.sleep(2+len(name))  # Simulate variable-length task
#     print(f"Thread {name}: finishing.")


# # Create threads
# thread_a = threading.Thread(target=task, args=("ABCcdkcdomco",))
# thread_b = threading.Thread(target=task, args=("B",))
# thread_c = threading.Thread(target=task, args=("LONG_TASK",))

# # Start the threads
# thread_c.start()
# thread_a.start()
# thread_b.start()

# print("Main thread: doing other work concurrently.")

# # Wait for both threads to finish
# thread_a.join()
# thread_b.join()
# thread_c.join()

# print("Main thread: all done.")
# import tkinter as tk

# root = tk.Tk()
# root.title("Window 1")
# root.configure(bg="black")
# root.geometry("400x300")

# root.iconbitmap("favicon.ico")

# label = tk.Label(root, text="Hello", fg="lime", bg="black", font=("Consolas", 16))
# label.pack(expand=True)

# # root.mainloop()
import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("PySide6 works!")
label.resize(300, 200)
label.show()

sys.exit(app.exec())