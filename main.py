import osxphotos

# Initialize variable with the photo library object
photo_library = osxphotos.PhotosDB()

# Initialize variable with all photos from that library
all_photos = photo_library.photos()

# Initialize dictionary to hold photo information
photo_dict = {}

# Add Information about Each Photo to Dictionary
 # :50 is used to ensure only 50 pictures are put into the dictionary 
for photo in all_photos[:50]:
    photo_dict[photo.original_filename] = {
        "file_name": photo.original_filename,
        "date_taken": photo.date,
        "current_path": photo.path if photo.path else "No Path Available"
    }

# Use this print statement to see what the total size of the dictionary is when all photos are added
# print(len(photo_dict))

for photo, photo_info in photo_dict.items():
    print(f"Photo: {photo}\n, File Name: {photo_info['file_name']}\n, Date Taken: {photo_info['date_taken']}\n, Current Path: {photo_info['current_path']}\n")


