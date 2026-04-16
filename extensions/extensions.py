
s = input("File name:").strip().lower()
if "." in s:
    s = s.split(".")

    if s[-1] == "gif":
        print(f"image/{s[-1]}")
    elif s[-1] == "jpg":
        print("image/jpeg")
    elif s[-1] == "jpeg":
        print(f"image/{s[-1]}")
    elif s[-1] == "png":
        print(f"image/{s[-1]}")
    elif s[-1] == "pdf":
         print(f"application/{s[-1]}")
    elif s[-1] == "txt":
        print("text/plain")
    elif s[-1] == "zip":
        print(f"application/{s[-1]}")
    else:
        print("application/octet-stream")

else:
    print("application/octet-stream")
