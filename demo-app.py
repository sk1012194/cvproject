import streamlit as st
import numpy as np
from PIL import Image
import cv2

def load_image(file_uploader):
    try:
        # Load image from file uploader
        image = Image.open(file_uploader)
        return np.array(image)
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

def brighten_image(image, amount):
    try:
        # Adjust brightness using OpenCV
        img_bright = cv2.convertScaleAbs(image, beta=amount)
        return img_bright
    except Exception as e:
        st.error(f"Error adjusting brightness: {e}")
        return None

def blur_image(image, amount):
    try:
        # Apply Gaussian blur using OpenCV
        blur_img = cv2.GaussianBlur(image, (11, 11), amount)
        return blur_img
    except Exception as e:
        st.error(f"Error applying blur: {e}")
        return None

def enhance_details(img):
    try:
        # Enhance details using OpenCV
        hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
        return hdr
    except Exception as e:
        st.error(f"Error enhancing details: {e}")
        return None

def main_loop():
    st.title("OpenCV Demo App")
    st.subheader("Play with Image Filters using OpenCV and Streamlit")
    
    # Sidebar controls
    st.sidebar.header("Filter Controls")
    blur_rate = st.sidebar.slider("Blurring", min_value=0.5, max_value=3.5, step=0.1, value=1.0, help="Adjust the blurring effect.")
    brightness_amount = st.sidebar.slider("Brightness", min_value=-50, max_value=50, value=0, help="Adjust the image brightness.")
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details', help="Apply an enhancement filter to bring out details in the image.")

    # Image upload
    st.header("Upload Image")
    image_file = st.file_uploader("Choose an image (jpg, png, jpeg)", type=['jpg', 'png', 'jpeg'])

    if image_file:
        # Load original image
        original_image = load_image(image_file)

        if original_image is not None:
            # Apply filters
            processed_image = blur_image(original_image, blur_rate)
            processed_image = brighten_image(processed_image, brightness_amount)

            if apply_enhancement_filter:
                processed_image = enhance_details(processed_image)

            # Display images
            st.image([original_image, processed_image], caption=['Original Image', 'Processed Image'], channels="BGR", use_container_width=True)
    else:
        st.warning("Please upload an image.")

if __name__ == '__main__':
    main_loop()

