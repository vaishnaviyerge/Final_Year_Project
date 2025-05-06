import cv2
import os
import random
import numpy as np
from glob import glob

def apply_gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

def apply_high_pass_filter(image):
    # Kernel for edge detection (high-pass filter)
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def apply_low_pass_filter(image, kernel_size=(5, 5)):
    return cv2.blur(image, kernel_size)

def flip_image(image):
    return cv2.flip(image, 1)  # Horizontal flip

def rotate_image(image, angle):
    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def augment_image(image):
    # Randomly apply filters
    aug_list = [
        apply_gaussian_blur,
        # apply_high_pass_filter,
        # apply_low_pass_filter,
        flip_image,
        lambda img: rotate_image(img, random.choice([90, 180, 270]))
    ]
    
    # Randomly pick a transformation
    aug_choice = random.choice(aug_list)
    return aug_choice(image)

def augment_data(input_folder, output_folder, num_images):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_paths = glob(os.path.join(input_folder, "*"))
    total_images = len(image_paths)

    if total_images == 0:
        print("No images found in the input folder.")
        return

    for i in range(num_images):
        # Randomly pick an image from the input folder
        img_path = random.choice(image_paths)
        image = cv2.imread(img_path)

        if image is None:
            print(f"Could not read image: {img_path}")
            continue

        # Augment the image
        augmented_image = augment_image(image)

        # Save the augmented image to the output folder
        output_path = os.path.join(output_folder, f"{output_folder}_{i}.jpg")
        cv2.imwrite(output_path, augmented_image)
        print(f"Saved {output_path}")

if __name__ == "__main__":
    input_folder = "temp"  # Path to your input folder
    output_folder = "Odonil Red"  # Path to save augmented images
    num_images = 50  # Number of images to generate

    augment_data(input_folder, output_folder, num_images)
