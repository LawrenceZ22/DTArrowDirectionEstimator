import cv2
import numpy as np
import sys

def find_arrow_direction(image_path):
    # Load the image in grayscale and in color
    image_gray = cv2.imread(image_path, 0)
    original_image = cv2.imread(image_path)

    assert original_image is not None, "image not found"

    _, binary = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY_INV)

    dist_transform = cv2.distanceTransform(binary, cv2.DIST_L2, 5)

    # Normalize the distance transform for visualization.
    normalized_dist_transform = cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX)
    normalized_dist_transform = np.uint8(normalized_dist_transform)

    dist_transform_rgb = cv2.cvtColor(normalized_dist_transform, cv2.COLOR_GRAY2RGB)

    # Find the maximum point in DT image.
    _, _, _, max_loc = cv2.minMaxLoc(dist_transform)


    # Compare the relative position of maxpoint location with image centre to tell arrow direction.
    h, w = dist_transform.shape
    x, y = max_loc

    direction = ""
    if x < w / 4:
        direction = "Left"
    elif x > 3 * w / 4:
        direction = "Right"
    elif y < h / 4:
        direction = "Up"
    else:
        direction = "Down"

    # Concatenate the original image and distance transform
    cv2.hconcat([original_image, dist_transform_rgb])

    return direction, cv2.hconcat([original_image, dist_transform_rgb])

def main(image_filename):
    direction, concatenated_image = find_arrow_direction(image_filename)
    cv2.imshow(f"Arrow Direction: {direction}", concatenated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 detect.py <image_filename>")
    else:
        image_filename = sys.argv[1]
        main(image_filename)
