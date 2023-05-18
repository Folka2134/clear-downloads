import os
import shutil
from datetime import datetime, timedelta


def move_old_files_to_review_deleted(downloads_folder_path):
    review_deleted_folder = os.path.join(downloads_folder_path, "delete_review")

    # Calculate the date 14 days ago
    forteen_days_ago = datetime.now() - timedelta(days=14)

    # Define the time delta for 7 days
    seven_days_ago = datetime.now() - timedelta(days=7)

    # Create the "review-deleted" folder if it doesn't exist
    if not os.path.exists(review_deleted_folder):
        os.makedirs(review_deleted_folder)

    # Get the list of files and folders in the downloads folder
    items = os.listdir(downloads_folder_path)

    # Iterate over each item
    for item in items:
        item_path = os.path.join(downloads_folder_path, item)
        # Check if the item is a file or folder
        if os.path.isfile(item_path) or os.path.isdir(item_path):
            # Get the creation or modification date of the item
            timestamp = os.path.getctime(item_path)
            # Check for DALLE images and move them to a DALLE directory
            if "DALL" in item.upper():
                # Move the item to the dalle directory
                shutil.move(item_path, os.path.join(review_deleted_folder, item))
            # Check if the item is an .exe or .zip fil
            elif item.lower().endswith((".exe", ".zip", ".rar")):
                # Check if the item is older than 7 days
                if datetime.fromtimestamp(timestamp) < seven_days_ago:
                    # Delete the item
                    os.remove(os.path.join(downloads_folder_path, item))
            # Compare the date with 20 days ago
            elif datetime.fromtimestamp(timestamp) < forteen_days_ago:
                # Move the item to the "review-deleted" folder
                shutil.move(item_path, os.path.join(review_deleted_folder, item))
                print(f"Moved {item} to 'delete_review' folder.")


# Prompt the user for the downloads folder path
# downloads_folder = input("Enter the path of your downloads folder: ")

# Call the function with the provided path
move_old_files_to_review_deleted("E:/downloads")
