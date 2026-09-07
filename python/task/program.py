import os
import shutil

def create_directory():
    print("\n==============================")
    print("      CREATE DIRECTORY")
    print("==============================")

    directory_name = input("Enter Directory Name: ").strip()

    if directory_name == "":
        print("Directory name cannot be empty!")
        return

    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")

    folder_name = input("Enter Folder Name: ").strip()

    if folder_name == "":
        print("Folder name cannot be empty!")
        return

    folder_path = os.path.join(directory_name, folder_name)

    os.mkdir(folder_path)

    print(f"Folder '{folder_name}' created successfully.")

    choice = input("Do you want to create a file? (Y/N): ").strip().lower()

    if choice == "y":
        file_name = input("Enter File Name: ").strip()

        if file_name == "":
            print("File name cannot be empty!")
            return

        file_path = os.path.join(folder_path, file_name)

        note = input("Enter your note: ")

        with open(file_path, "w") as file:
            file.write(note)

        print(f"File '{file_name}' created successfully.")
        print("Note saved successfully.")

    elif choice == "n":
        print("File was not created.")

    else:
        print("Invalid choice!")


def delete_directory():
    print("\n==============================")
    print("      DELETE DIRECTORY")
    print("==============================")

    directory_name = input("Enter Directory Name to Delete: ").strip()

    if os.path.exists(directory_name):

        confirm = input(
            f"Are you sure you want to delete '{directory_name}'? (Y/N): "
        ).strip().lower()

        if confirm == "y":
            shutil.rmtree(directory_name)
            print(f"Directory '{directory_name}' deleted successfully.")

        elif confirm == "n":
            print("Directory was not deleted.")

        else:
            print("Invalid choice! Please enter Y or N.")

    else:
        print("Directory does not exist!")
def main():

    while True:

        print("\n==============================")
        print("       DIRECTORY TOOL")
        print("==============================")

        print("1. Create Directory")
        print("2. Delete Directory")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_directory()

        elif choice == "2":
            delete_directory()

        elif choice == "3":
            print("Program exited successfully.")
            break

        else:
            print("Invalid choice! Please try again.")


main()