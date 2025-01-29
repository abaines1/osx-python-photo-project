# osx-python-photo-project

Python OSX Module Guide: https://github.com/abaines1/osxphotos 

```markdown
# Photo Library Metadata Extraction

This Python script extracts metadata from a local photo library using the `osxphotos` library. The script retrieves the first 50 photos from the library and stores key information about each photo in a dictionary.

## Requirements

- Python 3.x
- `osxphotos` library

To install the required `osxphotos` library, run:

```bash
pip install osxphotos
```

## Usage

1. Initialize a photo library object using `osxphotos.PhotosDB()`.
2. Retrieve all photos from the library.
3. Loop through the first 50 photos and collect their metadata:
   - **Original filename**
   - **Date taken**
   - **Current path** (if available)

The script stores this information in a dictionary `photo_dict` where the key is the photo's original filename, and the value is another dictionary containing the metadata.

## Script Overview

```python
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

# Print the dictionary to see the extracted metadata
print(photo_dict)
```

### Output Example:

The output will be a dictionary containing the metadata of the first 50 photos in the library. Each photo's metadata will be stored with the following structure:

```python
{
    "photo1.jpg": {
        "file_name": "photo1.jpg",
        "date_taken": "2021-01-01 12:00:00",
        "current_path": "/path/to/photo1.jpg"
    },
    "photo2.jpg": {
        "file_name": "photo2.jpg",
        "date_taken": "2021-01-02 14:00:00",
        "current_path": "No Path Available"
    }
    # ... up to 50 photos
}
```

## License

This project is licensed under the MIT License.
```

This `README.md` explains the usage and structure of the Python script while also providing installation instructions. Let me know if you need further adjustments!