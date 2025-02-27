import os

def replace_seven(foldername):
    filenames = []
    for root, dirs, files in os.walk(foldername):
        for file in files:
            if ".7." in file:
                filename = file.replace(".7.", ".7z.") 
                try:
                    os.rename(os.path.join(root, file), os.path.join(root, filename))
                    print(f"Success replace name {filename}!")
                except FileNotFoundError:
                    print(f"파일 {file}이 존재하지 않습니다.")
                except FileExistsError:
                    print(f"같은 이름의 파일{filename}이 이미 존재합니다.")
                except PermissionError:
                    print("권한이 부족합니다.")
                except Exception as e:
                    print(f"오류 발생: {e}")
                filenames.append(os.path.join(root, filename))
    return filenames

# Example usage:
foldername = '\\TestFolder'
print(replace_seven(foldername))