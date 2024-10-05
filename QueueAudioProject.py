
import time
from playsound import playsound


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.Front = None
        self.Rear = None

    def EnQueue(self, data):
        NewNode = Node(data)
        if self.Front is None:
            self.Front = NewNode
            self.Rear = NewNode
            NewNode.next = NewNode
        else:
            self.Rear.next = NewNode
            self.Rear = NewNode
            NewNode.next = self.Front

    def DeQueue(self):
        if self.IsEmpty():
            print("Queue is Empty")
            return
        temp = self.Front
        self.Front = self.Front.next
        self.Rear.next = self.Front
        return temp.data

    def Peek(self):
        if self.IsEmpty():
            print("Queue Is Empty")
            return
        return self.Front.data

    def Size(self):
        count = 0
        temp = self.Front
        while temp:
            count += 1
            temp = temp.next
            if temp.next == self.Front:
                break
        print(count)

    def Display(self):
        temp = self.Front
        while temp:
            print(f"|{temp.data}|<--->", end='')
            temp = temp.next
            if temp.next == self.Front:
                print(f"|{temp.data}|<--->", end='')
                break
        print(f"|{temp.next.data}|")
        print()

    def IsEmpty(self):
        return self.Front is None

def play_audio_with_timeout(file_path, timeout):
    """Plays audio synchronously."""
    try:
        print(f"Now playing: {file_path}")
        playsound(file_path)  # Blocking, waits until the song finishes
        print(f"Finished playing: {file_path}")
    except FileNotFoundError:
        print(f"Error: Audio file '{file_path}' not found.")

def main():
    CQ = CircularQueue()

    CQ.EnQueue("/Users/vishnu/Downloads/AUDIO-2024-10-02-07-40-42.mp3")
    CQ.EnQueue("/Users/vishnu/Downloads/AUDIO-2024-10-02-07-40-41.aac")
    # ... Add more audio file paths to the queue

    CQ.Display()

    while not CQ.IsEmpty():
        file_path = CQ.DeQueue()
        play_audio_with_timeout(file_path, 60)  # Play each song until it completes

        # Optional: Add a small delay between songs if needed
        time.sleep(1)  # 2-second delay between songs

if __name__ == "__main__":
    main()
