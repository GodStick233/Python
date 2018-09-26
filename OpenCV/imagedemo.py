import cv2
def toppos(img):
    for i in range(0,71):
        for j in range(0,192):
            if img[i][j] < 50:
                return i
                break

def bottompos(img):
    for i in range(71,-1,-1):
        for j in range(0,192):
            if img[i][j] < 50:
                return i
                break

def leftpos(img):
    for i in range(0,192):
        for j in range(0,71):
            if img[j][i] < 50:
                return i
                break

def rigihtpos(img):
    for i in range(192,-1,-1):
        for j in range(0,72):
            if img[j][i] < 50:
                return i
                break

if __name__ == '__main__':
    img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
    top = toppos(img)
    bottom = bottompos(img)
    left = leftpos(img)
    right = rigihtpos(img)
    newimg = img[top:bottom,left:right+1]
    cv2.imwrite('newimg.png',newimg)
    cv2.imshow('hi',newimg)
    cv2.waitKey(0)