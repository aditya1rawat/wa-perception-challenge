import cv2
import numpy as np

# Function that draws the line on the image
def drawLine(image):
    # Set the min and max red color values to be identified as cones
    lowest_red_left_1, highest_red_right_1 = np.array([0, 175, 175]), np.array([5, 255, 255])
    lowest_red_right_2, highest_red_right_2 = np.array([175, 175, 175]), np.array([180, 255, 255])
     
    # Set the color mask
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(hsv, lowest_red_left_1, highest_red_right_1) + cv2.inRange(hsv, lowest_red_right_2, highest_red_right_2)

    # Find the contours of the cones
    countours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    centers = []

    # Loop through every identified cone and append their centers to a list
    for i in countours:
        cones = cv2.moments(i)
        if cones["m00"] != 0:
            centers.append((int(cones["m10"] / cones["m00"]), int(cones["m01"] / cones["m00"])))
    
    # Get the average center of the cones
    mean_x, mean_y = sum(x for x, y in centers) / len(centers), sum(y for x, y in centers) / len(centers)

    # Get the total change in x and y to determine the slope and the intercept
    rise, run = sum((x - mean_x) * (y-mean_y) for x, y in centers), sum((x - mean_x) ** 2 for x, y in centers)

    # Calculate the slope and intercept for the line
    slope = rise / run
    intercept = mean_y - slope * mean_x

    # Draw the line on the image
    cv2.line(image, (0, int(intercept)), (image.shape[1], int(slope * image.shape[1] + intercept)), (0, 0, 255), 5)
    return image


# OpenCV reads the image
img = cv2.imread("red.png")

# Deteremine the total width of the image
width = img.shape[1] // 2

# Divide the image into two halves
first_half, second_half = img[:, :width], img[:, width:]

# Draw the lines on each half of the image
first_half, second_half = drawLine(first_half), drawLine(second_half)

# Put the two halves back together
img = np.concatenate((first_half, second_half), axis=1)

# Save the image
cv2.imwrite("answer.png", img)

# Display the image
cv2.namedWindow("answer", cv2.WINDOW_NORMAL)
cv2.imshow("answer", img)
cv2.waitKey(0)
cv2.destroyAllWindows()