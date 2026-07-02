from os import name
import sqlite3


conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
    ID INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    time TEXT NOT NULL
) 
               ''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(ID, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE ID = ?", (name, time, ID))
    conn.commit()

def delete_video(ID):
    cursor.execute("DELETE FROM videos WHERE ID = ?", (ID,))
    conn.commit()

def main ():
    while True:
        print("\n Youtube Video Manager")
        print("1. List a favouraite videos ")
        print("2. Add a new YouTube videos  ")
        print("3. Update a YouTube video ")
        print("4. Delete a YouTube video ")
        print("5. Exit ")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_videos()
            
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
            
        elif choice == '3':
            video_ID = input("Enter video ID to update: ")
            update_video(video_ID, name, time)
           
        elif choice == '4':
            video_ID = input("Enter video ID to delete: ")
            delete_video(video_ID)
            
        elif choice == '5':
            print("Exiting Youtube Video Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
       
    conn.close()
     
if __name__ == "__main__":
    main() 