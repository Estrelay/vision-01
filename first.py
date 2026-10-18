import cv2
img_path="../images/test.jpg.jpg"
img = cv2.imread(img_path)
if img is None:
    print()
else:
    print(img.shape)
    cv2.imshow("test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    out_path="/output/test.jpg.jpg"
    cv2.imwrite(out_path,img)