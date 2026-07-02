
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
     
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print("\n" + "*" * 70)
        print(f"{index}. {video['title']} - {video['url']}")

def add_video(videos):
    name = input("Enter video title: ")
    url = input("Enter video URL: ")
    videos.append({'title': name, 'url': url})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter new video title: ")
        url = input("Enter new video URL: ")
        videos[index - 1] = {'title': name, 'url': url}
        save_data(videos)
    else:
        print("Invalid index.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data(videos)
    else:
        print("Invalid index.")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Video Manager")
        print("1. List a favouraite videos ")
        print("2. Add a new YouTube videos  ")
        print("3. Update a YouTube video ")
        print("4. Delete a YouTube video ")
        print("5. Exit ")
        choice = input("Enter your choice: ")
        print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
                
            case '2':
                add_video(videos)
                
            case '3':
                update_video(videos)
                
            case '4':
                delete_video(videos)
                
            case '5':
                print("Exiting Youtube Video Manager. Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main()