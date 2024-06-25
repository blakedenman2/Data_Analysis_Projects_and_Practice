def main():
    filename = input("File name: ").strip().casefold()
    if filename.endswith(".gif") == True :
        print("image/gif")
    elif filename.endswith(".jpg") == True :
        print("image/jpeg")
    elif filename.endswith(".jpeg") == True :
        print("image/jpeg")
    elif filename.endswith(".png") == True :
        print("image/png")
    elif filename.endswith(".pdf") == True :
        print("application/pdf")
    elif filename.endswith(".txt") == True :
        print("text/plain")
    elif filename.endswith(".zip") == True :
        print("application/zip")
    else : print("application/octet-stream")

main()
